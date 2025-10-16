import json
from pathlib import Path

PRODUCTS_FILE = Path("app/data/products.json")

async def get_all_products():
    with PRODUCTS_FILE.open() as f:
        data = json.load(f)
        return data.get("products", [])

async def get_products_by_names(names: list[str]):
    products = await get_all_products()
    lower_names = [name.lower() for name in names]

    matched_products = [
        product for product in products 
        if any(name in product["title"].lower() for name in lower_names)
    ]

    print(lower_names)
    return matched_products


