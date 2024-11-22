import json
from .product import Product
from .nutrition_data import NUTRITION_PER_100_GRAMS

class ProductManager:
    def __init__(self):
        self._products: list[Product] = []
        self.create_product_objects()

    def create_product_objects(self) -> None:
        '''Create products from the product nutrition json loaded data.'''
        for name in NUTRITION_PER_100_GRAMS:
            self._products.append(Product(name, *NUTRITION_PER_100_GRAMS[name].values()))

    def get_product_by_name(self, name) -> Product:
        '''Find product object by product name.'''
        for product in self._products:
            if name == product.name:
                return product

        raise RuntimeError(f'Food with name {name} was not found!')
