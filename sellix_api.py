import json
import requests

from requests.structures import CaseInsensitiveDict

class sellix:
    # token = your Sellix bearer token (required)
    def __init__(self, token):
        self.token = token

    # Return all products
    def list_products(self):
        url = "https://dev.sellix.io/v1/products"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"

        resp = requests.get(url, headers=headers)
        parsed = json.loads(resp.content)

        return parsed

    # Get product by ID
    # cat_id = ID of the product you want to get (required)
    def get_product(self, prod_id):
        url = f"https://dev.sellix.io/v1/products/{prod_id}"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"

        resp = requests.get(url, headers=headers)
        parsed = json.loads(resp.content)

        return parsed

    # Create serial product
    # title = string, product title (required)
    # description = string, product description (required)
    # price = float, product price (required)
    # gateways = string, gateways. gateways: paypal, bitcoin, ethereum, litecoin, perfectmoney, bitcoincash, skrill, paydash, lexholdingsgroup, stripe, cashapp. (required)
    # discount_value = float, discount amount (required)
    # currency = product currency. e.g USD (required)
    # serial_list = list of serials
    # delivery_text = delivery text (required)
    def create_serial_product(self, title, description, price, gateways, currency, serial_list, delivery_text):
        url = f"https://dev.sellix.io/v1/products"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"

        data = f'''
        {{
  "title": "{title}",
  "price": {price},
  "currency": "{currency}",
  "description": "{description}",
  "gateways": {gateways},
  "type": "serials",
  "stock_delimiter": ",",
  "serials": {serial_list},
  "delivery_text": "{delivery_text}"
  }}
        '''.replace("'", '"')

        resp = requests.post(url, headers=headers, data=data)
        parsed = json.loads(resp.content)

        return parsed

    # Create service product
    # title = string, product title (required)
    # description = string, product description (required)
    # price = float, product price (required)
    # gateways = string, gateways. gateways: paypal, bitcoin, ethereum, litecoin, perfectmoney, bitcoincash, skrill, paydash, lexholdingsgroup, stripe, cashapp. (required)
    # discount_value = float, discount amount (required)
    # currency = product currency. e.g USD (required)
    # service_text = service text
    # delivery_text = delivery text (required)
    def create_service_product(self, title, description, price, gateways, currency, service_text, delivery_text):
        url = f"https://dev.sellix.io/v1/products"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"

        data = f'''
        {{
  "title": "{title}",
  "price": {price},
  "currency": "{currency}",
  "description": "{description}",
  "gateways": {gateways},
  "type": "service",
  "service_text": "{service_text}",
  "delivery_text": "{delivery_text}"
  }}
        '''.replace("'", '"')

        print(data)

        resp = requests.post(url, headers=headers, data=data)
        parsed = json.loads(resp.content)

        return parsed

    # Return all categories
    def list_categories(self):
        url = "https://dev.sellix.io/v1/categories"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"

        resp = requests.get(url, headers=headers)
        parsed = json.loads(resp.content)

        return parsed
    
    # Get category by ID
    # cat_id = ID of the category you want to get (required)
    def get_category(self, cat_id):
        url = f"https://dev.sellix.io/v1/categories/{cat_id}"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"

        resp = requests.get(url, headers=headers)
        parsed = json.loads(resp.content)

        return parsed
    
    # Create a category
    # title = category title (required)
    # unlisted = not required, true/false, defaults to false
    # sort_priority = int, sorted by ASC, defaults to 0
    # products_bound = list of products uniqids the category will contain
    def create_category(self, title, unlisted=False, sort_priority=0, products_bound:list=None):
        url = f"https://dev.sellix.io/v1/categories"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"
        headers["Content-Type"] = "application/json"

        if products_bound is None:
            data = f'{{"title": "{title}", "unlisted": "{unlisted}", "sort_priority": {sort_priority}}}'
        elif products_bound is not None:
            data = f'{{"title": "{title}", "unlisted": "{unlisted}", "sort_priority": {sort_priority}, "products_bound": "{products_bound}"}}'

        resp = requests.post(url, headers=headers, data=data)
        parsed = json.loads(resp.content)

        return parsed

    # Edit a category
    # cat_id = category ID (required)
    # title = new title (not required)
    # unlisted = true/false (not required)
    # sort_priority = new sort priority (not required)
    # products_bound = list of products uniqids the category will contain (not required)
    def edit_category(self, cat_id, title=None, unlisted=None, sort_priority=None, products_bound:list=None):
        url = f"https://dev.sellix.io/v1/categories/{cat_id}"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"
        headers["Content-Type"] = "application/json"

        if title is not None:
            data = f'{{"title": "{title}"}}'
            resp = requests.put(url, headers=headers, data=data)
            parsed1 = json.loads(resp.content)
            print(parsed1)
        if unlisted is not None:
            data = f'{{"unlisted": "{title}"}}'
            resp = requests.put(url, headers=headers, data=data)
            parsed2 = json.loads(resp.content)
            print(parsed2)
        if sort_priority is not None:  # TODO: This doesn't work
            data = f'{{"unlisted": "{title}"}}'
            resp = requests.put(url, headers=headers, data=data)
            parsed3 = json.loads(resp.content)
            print(parsed3)
        if products_bound is not None:
            data = f'{{"unlisted": "{products_bound}"}}'
            resp = requests.put(url, headers=headers, data=data)
            parsed4 = json.loads(resp.content)
            print(parsed4)

    # Delete a category
    # title = category ID (required)
    def delete_category(self, cat_id):
        url = f"https://dev.sellix.io/v1/categories/{cat_id}"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"
        headers["Content-Type"] = "application/json"

        resp = requests.delete(url, headers=headers)
        parsed = json.loads(resp.content)

        return parsed

sellix_api = sellix("rSlUGGDomzDM7Qzrojpooq7AyF968ipTrZxWA3zkYBYbfPzhHM48iFyA0kT5p8Fy")
p = sellix_api.create_service_product(title="Title", description="Description", price=20.0, gateways=["bitcoin"], currency="USD", service_text="Service Text", delivery_text="Delivery Text")
print(p)