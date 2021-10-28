import json
import requests

from requests.structures import CaseInsensitiveDict

class sellix:
    # token = your Sellix bearer token (required)
    def __init__(self, token):
        self.token = token

    #          #
    # PRODUCTS #
    #          #

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

        resp = requests.post(url, headers=headers, data=data)
        parsed = json.loads(resp.content)

        return parsed

    # Edit a product
    # prod_id = product ID (required)
    # title = string, new title (not required)
    # description = string, new description (not required)
    # price = float, new new price (not required)
    # gateways = list, list of gateways to accept ex: ["paypal", "bitcoin"] (not required)
    def edit_product(self, prod_id, title=None, description=None, price=None, gateways=None):
        url = f"https://dev.sellix.io/v1/products/{prod_id}"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"
        headers["Content-Type"] = "application/json"

        if title is not None:
            data = f'{{"title": "{title}"}}'
            resp = requests.put(url, headers=headers, data=data)
            parsed1 = json.loads(resp.content)
            print(parsed1)
        if description is not None:
            data = f'{{"description": "{description}"}}'
            resp = requests.put(url, headers=headers, data=data)
            parsed2 = json.loads(resp.content)
            print(parsed2)
        if price is not None:  # TODO: This doesn't work
            data = f'{{"price": {price}}}'
            resp = requests.put(url, headers=headers, data=data)
            parsed3 = json.loads(resp.content)
            print(parsed3)
        if gateways is not None:
            data = f'{{"unlisted": {gateways}}}'
            resp = requests.put(url, headers=headers, data=data)
            parsed4 = json.loads(resp.content)
            print(parsed4)

    # Delete a product
    # prod_id = product ID (required)
    def delete_product(self, prod_id):
        url = f"https://dev.sellix.io/v1/products/{prod_id}"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"
        headers["Content-Type"] = "application/json"

        resp = requests.delete(url, headers=headers)
        parsed = json.loads(resp.content)

        return parsed

    #            #
    # CATEGORIES #
    #            #


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
    # cat_id = category ID (required)
    def delete_category(self, cat_id):
        url = f"https://dev.sellix.io/v1/categories/{cat_id}"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"
        headers["Content-Type"] = "application/json"

        resp = requests.delete(url, headers=headers)
        parsed = json.loads(resp.content)

        return parsed

    #        #
    # ORDERS #
    #        #


    # Get orders
    def get_orders(self):
        url = f"https://dev.sellix.io/v1/orders"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"

        resp = requests.get(url, headers=headers)
        parsed = json.loads(resp.content)

        return parsed

    # Get orders by ID
    # order_id = ID of the order you want to get (required)
    def get_order(self, order_id):
        url = f"https://dev.sellix.io/v1/orders/{order_id}"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"

        resp = requests.get(url, headers=headers)
        parsed = json.loads(resp.content)

        return parsed

    #          #
    # FEEDBACK #
    #          #


    # Get feedback
    def get_feedback(self):
        url = f"https://dev.sellix.io/v1/feedback"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"

        resp = requests.get(url, headers=headers)
        parsed = json.loads(resp.content)

        return parsed

    # Get feedback by ID
    # feedback_id = ID of the feedback you want to get (required)
    def feedback_reply(self, feedback_id):
        url = f"https://dev.sellix.io/v1/feedback/{feedback_id}"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"

        resp = requests.get(url, headers=headers)
        parsed = json.loads(resp.content)

        return parsed

    # Reply to feedback
    # feedback_id = ID of the feedback you want to reply to (required)
    # feedback_responce = string, feedback responce
    def reply(self, feedback_id, feedback_responce):
        url = f"https://dev.sellix.io/v1/feedback/reply/{feedback_id}"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"

        data = f'{{"reply": "{feedback_responce}"}}'

        resp = requests.get(url, headers=headers, data=data)
        parsed = json.loads(resp.content)

        return parsed

    #         #
    # COUPONS #
    #         #

    # Create a Coupon
    # Code = coupon code
    # Discount Value = float, percentage amount of the discount
    # Max Uses = int, max coupon code uses. defaults to -d (-1 = infinte)
    # Products Bound = list, list of product IDs the code can be used on
    def create_coupon(self, code=None, discount_value=None, max_uses=-1, products_bound=None):
        url = f"https://dev.sellix.io/v1/coupons"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"
        headers["Content-Type"] = "application/json"

        if products_bound is None:
            data = f'{{"code": "{code}", "discount_value": "{discount_value}", "max_uses": {max_uses}}}'
        elif products_bound is not None:
            data = f'{{"code": "{code}", "discount_value": "{discount_value}", "max_uses": {max_uses}, "products_bound": "{products_bound}"}}'

        resp = requests.post(url, headers=headers, data=data)
        parsed = json.loads(resp.content)

        return parsed

    # Edit a Coupon
    # Coupon ID = coupon ID
    # Code = coupon code
    # Discount Value = float, percentage amount of the discount
    # Max Uses = int, max coupon code uses (-1 = infinte)
    # Products Bound = list, list of product IDs the code can be used on
    def edit_coupon(self, coupon_id=None, code=None, discount_value=None, max_uses=None, products_bound=None):
        url = f"https://dev.sellix.io/v1/coupons/{coupon_id}"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"
        headers["Content-Type"] = "application/json"

        if code is not None:
            data = f'{{"code": "{code}"}}'
            resp = requests.post(url, headers=headers, data=data)
            parsed = json.loads(resp.content)
        if discount_value is not None:
            data = f'{{"discount_value": "{discount_value}"}}'
            resp = requests.post(url, headers=headers, data=data)
            parsed = json.loads(resp.content)
        if max_uses is not None:
            data = f'{{"max_uses": "{max_uses}"}}'
            resp = requests.post(url, headers=headers, data=data)
            parsed = json.loads(resp.content)
        if products_bound is not None:
            data = f'{{"products_bound": "{products_bound}"}}'
            resp = requests.post(url, headers=headers, data=data)
            parsed = json.loads(resp.content)

        return parsed

    # Delete a Coupon
    # coupon_id = coupon ID (required)
    def delete_coupon(self, coupon_id):
        url = f"https://dev.sellix.io/v1/coupons/{coupon_id}"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"
        headers["Content-Type"] = "application/json"

        resp = requests.delete(url, headers=headers)
        parsed = json.loads(resp.content)

        return parsed

    # Get all coupons
    def list_coupons(self):
        url = f"https://dev.sellix.io/v1/coupons"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"

        resp = requests.get(url, headers=headers)
        parsed = json.loads(resp.content)

        return parsed
    
    # Get coupons by ID
    # Coupon ID = ID of the coupon
    def get_coupon(self, coupon_id):
        url = f"https://dev.sellix.io/v1/coupons/{coupon_id}"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"

        resp = requests.get(url, headers=headers)
        parsed = json.loads(resp.content)

        return parsed

    #         #
    # QUERIES #
    #         #

    # Reply to query
    # query_id = ID of the query you want to reply to (required)
    # query_responce = string, query responce
    def query_reply(self, query_id, query_responce):
        url = f"https://dev.sellix.io/v1/queries/reply/{query_id}"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"

        data = f'{{"reply": "{query_responce}"}}'

        resp = requests.post(url, headers=headers, data=data)
        parsed = json.loads(resp.content)

        return parsed

    # Close queries
    # Query ID = int, query ID (required)
    def close_query(self, query_id):
        url = f"https://dev.sellix.io/v1/queries/{query_id}"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"

        resp = requests.post(url, headers=headers)
        parsed = json.loads(resp.content)

        return parsed

    # Reopen queries
    # Query ID = int, query ID (required)
    def reopen_query(self, query_id):
        url = f"https://dev.sellix.io/v1/queries/reopen/{query_id}"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"

        resp = requests.post(url, headers=headers)
        parsed = json.loads(resp.content)

        return parsed

    # List all queries
    def list_queries(self):
        url = f"https://dev.sellix.io/v1/queries"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"

        resp = requests.get(url, headers=headers)
        parsed = json.loads(resp.content)

        return parsed

    # Get query by ID
    def get_query(self, query_id):
        url = f"https://dev.sellix.io/v1/queries/{query_id}"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"

        resp = requests.get(url, headers=headers)
        parsed = json.loads(resp.content)

        return parsed

    #            #
    # BLACKLISTS #
    #            #

    # Create blacklist
    # Blacklist type = string, blacklist type. ex: email, ip, or country (required)
    # Data = string, blocked data. ex: country code, email, or an IP address (required)
    # Note = string, internal note for blacklist reasons (required)
    def create_blacklist(self, blacklist_type, blacklist_data, note):
        url = f"https://dev.sellix.io/v1/blacklists"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"

        data = f'{{"type": "{blacklist_type}", "data": "{blacklist_data}", "note": "{note}"}}'

        print(data)

        resp = requests.post(url, headers=headers, data=data)
        parsed = json.loads(resp.content)

        return parsed

    # Edit a blacklist
    # Blacklist ID = int, blacklist ID (required)
    # Blacklist type = string, blacklist type. ex: email, ip, country (required)
    # Note = string, interal note for blacklist reasons (required)
    def edit_blacklist(self, blacklist_id, blacklist_type=None, blacklist_data=None, note=None):
        url = f"https://dev.sellix.io/v1/blacklists/{blacklist_id}"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"
        headers["Content-Type"] = "application/json"

        if blacklist_type is not None:
            data = f'{{"type": "{blacklist_data}"}}'
            resp = requests.put(url, headers=headers, data=data)
            parsed1 = json.loads(resp.content)
            print(parsed1)
        if blacklist_data is not None:
            data = f'{{"data": "{data}"}}'
            resp = requests.put(url, headers=headers, data=data)
            parsed1 = json.loads(resp.content)
            print(parsed1)
        if note is not None:
            data = f'{{"note": "{note}"}}'
            resp = requests.put(url, headers=headers, data=data)
            parsed1 = json.loads(resp.content)
            print(parsed1)

    # Delete a blacklist
    # blacklist_id = blacklist ID (required)
    def delete_blacklist(self, blacklist_id):
        url = f"https://dev.sellix.io/v1/blacklists/{blacklist_id}"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"
        headers["Content-Type"] = "application/json"

        resp = requests.delete(url, headers=headers)
        parsed = json.loads(resp.content)

        return parsed

    # List blacklists
    def list_blacklists(self):
        url = "https://dev.sellix.io/v1/blacklists"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"

        resp = requests.get(url, headers=headers)
        parsed = json.loads(resp.content)

        return parsed

    # Get blacklist by ID
    # Blacklist ID = int, blacklist ID (required)
    def get_blacklist(self, blacklist_id):
        url = f"https://dev.sellix.io/v1/blacklists/{blacklist_id}"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"

        resp = requests.get(url, headers=headers)
        parsed = json.loads(resp.content)

        return parsed

    #          #
    # PAYMENTS #
    #          #

    # Create payment
    # Gateway = string, paypal, bitcoin, ethereum, litecoin, perfectmoney, bitcoincash, skrill, paydash, lexholdingsgroup, stripe, cashapp. (required) 
    # Email = string, customers email. where products will be sent (required)
    # Return URL = string, return URL (required)
    # Currency = string, currency type, ex: USD (required)
    # Value = float, amount the customer would pay (required if product ID is not supplied)
    # Product ID = string, ID of product customer is buying (required is value is not given)
    # Quantity = float, quantity customer if buying (required if product ID is supplied)
    def create_intergrated_payment(self, gateway, email, return_url, currency, value=None, title=None, product_id=None, quantity=None):
        url = "https://dev.sellix.io/v1/payments"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"

        if value is None:
            data = f'''
    {{
    "product_id": "{product_id}",
    "gateway": "{gateway}",
    "currency": "{currency}",
    "quantity": {quantity},
    "email": "{email}",
    "white_label": false,
    "return_url": "{return_url}"
    }}
            '''
        else:
            data = f'''
    {{
    "title": "{title}",
    "gateway": "{gateway}",
    "currency": "{currency}",
    "value": {value},
    "email": "{email}",
    "white_label": false,
    "return_url": "{return_url}"
    }}
            '''

        resp = requests.post(url, headers=headers, data=data)
        parsed = json.loads(resp.content)

        return parsed

    # Delete a payment
    # Payment ID = payment ID (required)
    def delete_payment(self, payment_id):
        url = f"https://dev.sellix.io/v1/payments/{payment_id}"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.token}"
        headers["Content-Type"] = "application/json"

        resp = requests.delete(url, headers=headers)
        parsed = json.loads(resp.content)

        return parsed
