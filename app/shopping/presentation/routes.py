import itertools
from itertools import combinations
from typing import List

from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends

from auth.presentation.utils import get_current_user
from location.application.usecases.get_enable_location import get_enable_location
from market.application.usecases import get_available_markets_count, get_product_prices
from shopping.application.usecases import (
    create_list,
    create_or_update_items,
    create_purchase_list,
    delete_list,
    detail_list,
    edit_list,
    get_best_route_info,
    list_items,
    list_lists,
    remove_deleted_items,
)
from shopping.application.usecases.complete_purchase_list import complete_purchase_list
from shopping.application.usecases.list_purchase_lists import list_purchase_lists
from shopping.domain import EstablishmentProduct, ListEstablishmentProduct, PurchaseList

from .schemas import BuySetting, ListCreate, ListEdit, ListItemCreate

router = APIRouter()


@router.post("/lists", name="shopping:create_list")
@router.post("/lists/", name="shopping:create_list", include_in_schema=False)
def post_list(user=Depends(get_current_user), list_obj: ListCreate = None):
    """
    Create list
    """

    list_obj.user_id = user.id
    list_obj = create_list(list_obj=list_obj)

    return list_obj


@router.get("/lists", name="shopping:list_lists")
@router.get("/lists/", name="shopping:list_lists", include_in_schema=False)
def get_list(user=Depends(get_current_user)):
    """
    List lists
    """

    lists = list_lists(user_id=user.id)

    return {"results": lists}


@router.patch("/lists/{id}", name="shopping:edit_list")
@router.patch("/lists/{id}/", name="shopping:edit_lists", include_in_schema=False)
def patch_list(user=Depends(get_current_user), id: int = None, list_obj: ListEdit = None):
    """
    Edit lists
    """

    list_edited = edit_list(user_id=user.id, list_id=id, list_obj=list_obj)

    return list_edited


@router.delete("/lists/{id}", name="shopping:delete_list")
@router.delete("/lists/{id}/", name="shopping:delete_lists", include_in_schema=False)
def delete_http_list(user=Depends(get_current_user), id: int = None, list_obj: ListEdit = None):
    """
    Delete lists
    """

    list_edited = delete_list(user_id=user.id, list_id=id)

    return list_edited


@router.post("/lists/{id}/items", name="shopping:create_item")
@router.post("/lists/{id}/items/", name="shopping:create_item", include_in_schema=False)
def post_item(user=Depends(get_current_user), id: int = None, items: List[ListItemCreate] = None):
    """
    Create List items
    """

    items_id = [item.id for item in items if item.id is not None]

    remove_deleted_items(list_id=id, item_id=items_id)

    items = create_or_update_items(list_id=id, items=items)

    return {"results": items}


@router.get("/lists/{id}/items", name="shopping:get_item")
@router.get("/lists/{id}/items/", name="shopping:get_item", include_in_schema=False)
def get_item(user=Depends(get_current_user), id: int = None):
    """
    Get List items
    """

    items = list_items(list_id=id)
    return {"results": items}


def get_best_list(candidates):
    best_fit = candidates[0]
    for i in range(len(candidates) - 1):
        if candidates[i + 1].total_products() > best_fit.total_products() or (
            candidates[i + 1].total_products() >= best_fit.total_products()
            and best_fit.total() > candidates[i + 1].total()
        ):
            best_fit = candidates[i + 1]

    return best_fit


def get_best_establishment_by_combination(markets_combination):
    candidates = []
    for market_combination in markets_combination:
        list_establishment_product = ListEstablishmentProduct()
        for market in list(market_combination):
            estblishment_product = EstablishmentProduct(
                id=market.id,
                name=market.name,
                establishment_type=market.establishment_type,
                address=market.address,
                latitude=market.latitude,
                longitude=market.longitude,
            )
            list_establishment_product.establishments.append(estblishment_product)

        for i in range(len(market_combination) - 1):
            for product_key in market_combination[i].items:
                current_product_market = market_combination[i].items[product_key]

                for j in range(i + 1, len(market_combination)):
                    next_product_market = market_combination[j].items.get(product_key, None)
                    if next_product_market is not None:
                        if current_product_market["total"] <= next_product_market["total"]:
                            list_establishment_product.establishments[i].products.append(
                                current_product_market
                            )
                            market_combination[j].items.pop(product_key)
                            list_establishment_product.establishments[i].remove_duplicate()
                        else:

                            list_establishment_product.establishments[i].remove_duplicate()
                            list_establishment_product.establishments[i].remove_product(
                                product_key
                            )
                            break
                    else:
                        list_establishment_product.establishments[i].products.append(
                            current_product_market
                        )
                        list_establishment_product.establishments[i].remove_duplicate()

        for product_key in market_combination[-1].items:
            if product_key not in list_establishment_product.get_products_ids():
                product = market_combination[-1].items[product_key]
                list_establishment_product.establishments[-1].products.append(product)

        candidates.append(list_establishment_product)
    return candidates


def get_one_best_establishment(markets_with_items):
    candidates = []
    for market in markets_with_items:
        products = [market.items[key_product] for key_product in market.items]
        candidate = EstablishmentProduct(
            id=market.id,
            name=market.name,
            establishment_type=market.establishment_type,
            address=market.address,
            latitude=market.latitude,
            longitude=market.longitude,
            products=products,
        )
        candidates.append(ListEstablishmentProduct(establishments=[candidate]))

    return get_best_list(candidates)


def create_purchase_list_wrapper(location, candidate, setting, list_obj, user):
    origin = (location.latitude, location.longitude)
    distance, duration, overview_polyline = get_best_route_info(
        origin=origin, establishments=candidate.establishments, mode=setting.mode
    )

    purchase_list = PurchaseList(
        name=list_obj.name,
        color=list_obj.color,
        user_id=user.id,
        distance=distance,
        duration=duration,
        spent=0,
        list_id=list_obj.id,
        estimated_price=candidate.total(),
        overview_polyline=overview_polyline,
    )

    purchase_list = create_purchase_list(purchase_list_obj=purchase_list, extra_data=candidate)

    return purchase_list


@router.post("/lists/{list_id}/buy", name="shopping:buy")
@router.post("/lists/{list_id}/buy/ ", name="shopping:buy", include_in_schema=False)
def buy_list(user=Depends(get_current_user), list_id: int = None, setting: BuySetting = None):
    """
    Buy a list
    """
    location = get_enable_location(user_id=user.id)
    markets = get_available_markets_count(
        lat=location.latitude, lng=location.longitude, distance=setting.max_market_distance
    )

    if len(markets) == 0:
        raise HTTPException(status_code=400, detail="No markets near")

    items = list_items(list_id=list_id)
    item_ids = [item.product.id for item in items]

    markets_with_items = []
    for market in markets:
        item_prices = get_product_prices(establishment_id=market.id, product_ids=item_ids)
        if len(item_prices) == 0:
            continue

        items_dict = {item.product_id: item.dict() for item in item_prices}

        for item in items:
            key = item.product.id
            if key in items_dict:
                items_dict[key] = {**items_dict[key], **item.dict()}
                items_dict[key]["total"] = items_dict[key]["quantity"] * items_dict[key]["price"]

        market.items = items_dict
        markets_with_items.append(market)

    list_obj = detail_list(list_id=list_id)

    if len(markets) == 1 or setting.max_market_count == 1:
        candidate = get_one_best_establishment(markets_with_items)

        result = create_purchase_list_wrapper(
            location=location, candidate=candidate, setting=setting, list_obj=list_obj, user=user
        )
        return result

    candidates = []

    for num_combination in range(2, setting.max_market_count + 1):
        markets_combination = combinations(markets_with_items, num_combination)
        candidates.append(get_best_establishment_by_combination(markets_combination))

    candidates = list(itertools.chain(*candidates))
    candidates.append(get_one_best_establishment(markets_with_items))
    candidate = get_best_list(candidates)

    result = create_purchase_list_wrapper(
        location=location, candidate=candidate, setting=setting, list_obj=list_obj, user=user
    )
    return result


@router.get("/purchase_lists", name="shopping:list_purchase_lists")
@router.get("/purchase_lists/", name="shopping:list_purchase_lists", include_in_schema=False)
def get_purchase_list(user=Depends(get_current_user), in_progress: int = None):
    """
    List purchase lists
    """

    purchase_lists = list_purchase_lists(user_id=user.id, in_progress=in_progress)

    return {"results": purchase_lists}


@router.patch("/purchase_lists/{id}/complete", name="shopping:complete_purchase_lists")
@router.patch(
    "/purchase_lists/{id}/complete/",
    name="shopping:complete_purchase_lists",
    include_in_schema=False,
)
def complete_method_purchase_list(user=Depends(get_current_user), id=None):
    """
    List purchase lists
    """

    p = complete_purchase_list(user_id=user.id, purchase_id=id)

    return p
