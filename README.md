# Python Sellix.io API Wrapper

# Usage

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
