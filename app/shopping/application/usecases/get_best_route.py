import googlemaps

from common.settings import GOOGLE_MAPS_KEY

gmaps = googlemaps.Client(key=GOOGLE_MAPS_KEY)


def get_best_route_info(origin, establishments, mode: str = "driving"):
    points = [(e.latitude, e.longitude) for e in establishments]
    if len(points) > 1:
        direction_result = gmaps.directions(
            origin=origin,
            destination=points[-1],
            waypoints=points[0 : len(points) - 1],
            optimize_waypoints=True,
        )
    else:
        direction_result = gmaps.directions(origin=origin, destination=points[0])

    overview_polyline = direction_result[0]["overview_polyline"]["points"]
    distance = sum([leg["distance"]["value"] for leg in direction_result[0]["legs"]])
    duration = sum([leg["duration"]["value"] for leg in direction_result[0]["legs"]])
    return distance, duration, overview_polyline
