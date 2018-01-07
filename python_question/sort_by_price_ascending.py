# Implement the function sort_by_price_ascending, which:
# 1. Accepts a string in JSON format, as in the example below.
# 2. Order items by price in ascending order.
# 3. if two products have same price, it orders them by their name in
# alphabetical order.
# 4. Returns a string in JSON format that is equivalent to the one in
# the input format.
# For example, the call
# Products.sort_by_price_ascending('[{"name":"eggs","price:"1"},
# {"name":"coffee","price:"9.99"}, {"name":"rice","price:"4.04"}]')
# should return
# '[{"name":"eggs","price:"1"}, {"name":"rice","price:"4.04"},
# {"name":"coffee","price:"9.99"}]'
import json


class Products:
    @staticmethod
    def sort_by_price_ascending(json_string):
        json_loaded = json.loads(json_string)
        sorted_json = sorted(json_loaded, key=lambda tag: (tag['price'], tag['name']))
        json_dumped = json.dumps(sorted_json)
        return json_dumped


print(Products.sort_by_price_ascending(
    '[{"name":"eggs","price":"1"},{"name":"coffee","price":"9.99"}, {"name":"vodka", "price":"9.99"}, {"name":"rice","price":"4.04"}]'))
