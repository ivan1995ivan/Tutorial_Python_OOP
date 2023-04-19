import pprint
class Products:
    title = 'chocolate'
    price = 1


Products.amount = 12
pprint.pprint(Products.__dict__)