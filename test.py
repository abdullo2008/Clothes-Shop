import requests

products = []
products_url = requests.get('http://127.0.0.1:8000/api/v1/')

# for product in products_url.json():
#     products.append(product)
for product_cat in products_url.json():
    products.append(product_cat)
# print(products_url.json(  )['category'])
print(products)
categories = []
category_names = []
response = requests.get('http://127.0.0.1:8000/api/v1/category/')
for i in response.json():
    categories.append(i['id'])
    category_names.append(i)
print(category_names)
