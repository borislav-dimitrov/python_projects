import json
from .product import Product


class ProductManager:
    def __init__(self):
        self._products: list[Product] = []
        self.create_product_objects()

    @staticmethod
    def load_products() -> dict:
        with open(r'food\nutrition_per_100.json', 'r') as file_handler:
            foods = json.load(file_handler)

        return foods

    def create_product_objects(self) -> None:
        '''Create products from the product nutrition json loaded data.'''
        products = self.load_products()

        for name in products:
            self._products.append(Product(name, *products[name].values()))

    def get_product_by_name(self, name) -> Product:
        '''Find product object by product name.'''
        for product in self._products:
            if name == product.name:
                return product

        raise RuntimeError(f'Food with name {name} was not found!')
