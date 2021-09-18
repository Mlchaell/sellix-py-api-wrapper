# Python Sellix.io API Wrapper

## Overview
- [Install](README.md#Install)
- [Init](README.md#Init)
- [Products](README.md#Products)
- [Categories](README.md#Categories)
- [Orders](README.md#Orders)
- [Feedback](README.md#Feedback)
- [Coupons](README.md#Coupons)
- [Queries](README.md#Queries)
- [Blacklists](README.md#Blacklists)
- [Blacklists](README.md#Blacklists)
- [Payments](README.md#Payments)
- [Todo](README.md#Todo)

## Install:

```
pip3 install sellix-py-api-wrapper
```

## Init:
```
sellix_api = sellix("SELLIX TOKEN")
```

## Products

### Create Products

- Title = string, product title (required)
- Description = string, product description (required)
- Price = float, product price (required)
- Gateways = string, gateways. gateways: paypal, bitcoin, ethereum, litecoin, perfectmoney, bitcoincash, skrill, paydash, lexholdingsgroup, stripe, cashapp. ex: ["paypal", "bitcoin"] (required)
- Discount Value = float, discount amount (required)
- Currency = product currency. e.g USD (required)
- Serial List = list of serials (required for serial product)
- Delivery Text = delivery text (required)

```
Serial Product: sellix_api.create_serial_product()
Service Product: sellix_api.create_service_product()
```

### Edit Products
- Product ID = product ID (required)
- Title = string, new title (not required)
- Description = string, new description (not required)
- Price = float, new new price (not required)
- Gateways = list, list of gateways to accept ex: ["paypal", "bitcoin"] (not required)

```
sellix_api.edit_product()
```

### Delete a Product
- Product ID = product ID (required)

```
Delete a product: sellix_api.delete_product(product_id)
```

### Get Products
```
Get all products: sellix_api.list_products()
Get products by ID: sellix_api.get_product(product_id)
```

## Categories

### Create Category
- Title = category title (required)
- Unlisted = not required, true/false, defaults to false
- Sort Priority = int, sorted by ASC, defaults to 0
- Products Bound = list of products uniqids the category will contain

```
sellix_api.create_category()
```

### Edit Categories
- Cat ID = category ID (required)
- Title = new title (not required)
- Unlisted = true/false (not required)
- Sort Priority = new sort priority (not required)
- Products Bound = list of products uniqids the category will contain (not required)

```
sellix_api.edit_category()
```

### Delete Category
```
sellix_api.delete_category(category_id)
```

### Get Categories
```
Get all categories: sellix_api.list_categories()
Get categories by ID: sellix_api.get_category(category_id)
```

## Orders

### Reply to Feedback
- Feedback ID = int, ID of the feedback you want to reply to (required)
- Feedback Responce = string, feedback repsonce
```
sellix_api.feedback_reply()
```

### Get Orders
```
Get all orders: sellix_api.get_orders()
Get orders by ID: sellix_api.get_order(order_id)
```

## Feedback

### Get Feedback
```
Get all feedback: sellix_api.get_feedback()
Get feedback by ID: sellix_api.get_feedback_by_id(feedback_id)
```

## Coupons

### Create a Coupon
- Code = string, coupon code (required)
- Discount Value = float, percentage amount of the discount (required)
- Max Uses = int, max coupon code uses. defaults to -d (-1 = infinte) (required)
- Products Bound = list, list of product IDs the code can be used on (not required)

```
sellix_api.create_coupon()
```

### Edit a Coupon
- Coupon ID = coupon ID
- Code = string, coupon code
- Discount Value = float, percentage amount of the discount
- Max Uses = int, max coupon code uses (-1 = infinte)
- Products Bound = list, list of product IDs the code can be used on

```
sellix_api.edit_coupon()
```

### Delete a Coupon
- Coupon ID - ID of the coupon

```
sellix_api.delete_coupon()
```

### Get coupons
```
Get all coupons: sellix_api.list_coupons()
Get coupons by ID: sellix_api.get_coupons(coupon_id)
```
## Queries

### Reply to Query
- Query ID = ID of the query you want to reply to (required)
- Query Responce = string, query responce

```
sellix_api.query_reply()
```

### Close Query
- Query ID = ID of the query you want to reply to (required)

```
sellix_api.close_query()
```

### Reopen Query
- Query ID = ID of the query you want to reply to (required)

```
sellix_api.reopen_query()
```

### Get Queries
```
Get all queries: sellix_api.list_queries()
Get query by ID: sellix_api.get_query(query_id)
```

## Blacklists

### Create a Blacklist 
- Blacklist type = string, blacklist type. ex: email, ip, or country
- Data = string, blocked data. ex: country code, email, or an IP address
- Note = string, internal note for blacklist reasons

```
sellix_api.create_blacklist()
```

### Edit a Blacklist
- Blacklist ID = int, blacklist ID (required)
- Blacklist type = string, blacklist type. ex: email, ip, country (required)
- Note = string, interal note for blacklist reasons (required)

```
sellix_api.edit_blacklist()
```

### Delete Blacklist
- Blacklist ID = blacklist ID (required)

```
sellix_api.delete_blacklist()
```

### Get blacklists
```
Get all blacklists: sellix_api.list_blacklists()
Get blacklist by ID: sellix_api.get_blacklist(blacklist_id)
```

## Payments

### Payment Types
```
**Integrated**
With the integrated checkout option, Sellix handles the checkout aspect for you by only returning a unique payment URL. This unique URL contains our realtime checkout page.

**White-label**
The white-label checkout flow provides the raw order created rather than a payment URL. With the raw order information, you are able to develop and integrate your own checkout experience completely separate from Sellix.
This has the added downside of not having the realtime status updates that the integrated checkout flow offers, but this can of course be implemented on your side using the webhooks.
```

### Create Intergrated Payment
- Gateway = string, paypal, bitcoin, ethereum, litecoin, perfectmoney, bitcoincash, skrill, paydash, lexholdingsgroup, stripe, cashapp. (required) 
- Email = string, customers email. where products will be sent (required)
- Return URL = string, return URL (required)
- Currency = string, currency type, ex: USD (required)
- Value = float, amount the customer would pay (required if product ID is not supplied)
- Product ID = string, ID of product customer is buying (required is value is not given)
- Quantity = float, quantity customer if buying (required if product ID is supplied)

```
sellix_api.create_intergrated_payment()
```

## Todo
- Whitelabel Payments
