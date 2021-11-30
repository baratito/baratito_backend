from datetime import datetime, timedelta

from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer
from shopping.application.repositories.purchase_list_repository import PurchaseListRepository
from shopping.application.usecases.get_purchase_list_items import get_purchase_list_items


@inject
def purchase_list_summary(
    purchase_list_repository: PurchaseListRepository = Provide[
        ApplicationContainer.purchase_list_repository_container.purchase_list_respository
    ],
    user_id: int = None,
):
    months = {
        "1": {"name": "enero", "abbreviation": "en", "total": 0, "purchases": []},
        "2": {"name": "febrero", "abbreviation": "feb", "total": 0, "purchases": []},
        "3": {
            "name": "marzo",
            "abbreviation": "mar",
            "total": 0,
        },
        "4": {"name": "abril", "abbreviation": "abr", "total": 0, "purchases": []},
        "5": {"name": "mayo", "abbreviation": "may", "total": 0, "purchases": []},
        "6": {"name": "junio", "abbreviation": "jun", "total": 0, "purchases": []},
        "7": {"name": "julio", "abbreviation": "jul", "total": 0, "purchases": []},
        "8": {"name": "agosto", "abbreviation": "ago", "total": 0, "purchases": []},
        "9": {"name": "septiembre", "abbreviation": "sept", "total": 0, "purchases": []},
        "10": {"name": "octubre", "abbreviation": "oct", "total": 0, "purchases": []},
        "11": {"name": "noviembre", "abbreviation": "nov", "total": 0, "purchases": []},
        "12": {"name": "diciembre", "abbreviation": "dic", "total": 0, "purchases": []},
    }

    from_date = datetime.utcnow() - timedelta(days=365)
    from_date = from_date.strftime("%Y-%m-%d")
    purchases = purchase_list_repository.list(user_id=user_id, from_date=from_date)

    for purchase in purchases:
        created_date = datetime.strptime(purchase.created_date, "%Y-%m-%d %H:%M:%S.%f")
        # TODO: this is not quite true
        key = str(created_date.month)
        months[key]["total"] += purchase.spent
        items = get_purchase_list_items(purchase_id=purchase.id)
        purchase.establishments = items
        purchases_list = months[key].get("purchases", [])
        purchases_list.append(purchase)
        months[key]["purchases"] = purchases_list

    return [months[key] for key in months]
