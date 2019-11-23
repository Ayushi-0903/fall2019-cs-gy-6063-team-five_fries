from typing import Optional
from ..models import Address, CachedSearch
from .fetch import fetch_geocode


def parse_lat_lng(geo_result_obj):
    """
    Parses out a latitude/longitude tuple from the Google Geocoder response object
    """
    if geo_result_obj:
        if "geometry" in geo_result_obj.keys():
            geo = geo_result_obj["geometry"]
            if "location" in geo.keys():
                location = geo_result_obj["geometry"]["location"]
                return (location["lat"], location["lng"])

    # default case if there was no result returned
    return (None, None)


def normalize_us_address(address) -> Optional[Address]:
    if not address:
        return None

    # want to get rid of extraneous spaces and uppercase letters
    # as those don't matter to the Geocode API and will reduce the number
    # of extra Cache objects
    address = (" ".join(address.split())).lower()
    cache, created = CachedSearch.objects.get_or_create(search_string=address)

    if not created:
        return Address(
            street=cache.street,
            city=cache.city,
            state=cache.state,
            zipcode=cache.zipcode,
            latitude=cache.latitude,
            longitude=cache.longitude,
        )

    response_list = fetch_geocode(address, region="us")

    if not response_list:
        return None

    response = response_list[0]

    state = None
    city = None
    route = ""
    street_num = ""

    for comp in response.get("address_components"):
        types = comp.get("types")

        if not types:
            continue

        if "administrative_area_level_1" in types:
            state = comp.get("short_name")

        if "street_number" in types:
            street_num = comp.get("long_name")

        if "route" in types:
            route = comp.get("long_name")

        # https://stackoverflow.com/a/49640066/1556838
        if "locality" in types or "sublocality_level_1" in types:
            city = comp.get("long_name")

    zip_code = response.get("postal")
    loc = response.get("geometry").get("location")
    lat, lon = loc["lat"], loc["lng"]

    # save the search and it's return value from the Geocode API so next time
    # it is searched we do not need to requery
    cache.street = " ".join(filter(lambda x: x, [street_num, route]))
    cache.city = city
    cache.state = state
    cache.zipcode = zip_code
    cache.latitude = lat
    cache.longitude = lon
    cache.save()

    return Address(
        street=" ".join(filter(lambda x: x, [street_num, route])),
        city=city,
        state=state,
        zipcode=zip_code,
        latitude=lat,
        longitude=lon,
    )