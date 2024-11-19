from .product import Product
from .utils import DishNames


class Recipe:
    '''
    products - list[
        [product: Product, amount: int],
        ...
    ]
    '''

    def __init__(self, name: DishNames, products: list[list[Product | int]]) -> None:
        self.name = name
        self._products: list[list[Product | int]] = products

    def get_products(self) -> list[list[Product | int]]:
        '''Get the products and the amounts required for this recipe.'''
        return self._products
