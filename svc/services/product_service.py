from svc.repositories.product_database import get_product_by_location


def is_product_available(selection):
    products = get_product_by_location(selection)
    return len(products) > 0

