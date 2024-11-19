from .product import Product
from .recipe import Recipe
from .utils import DishNames


class RecipeManager:
    def __init__(self) -> None:
        self._recipes: list[Recipe] = []

    def create_recipe(self, name: DishNames, products: list[list[Product | int]]) -> None:
        '''Create the recipes.'''
        self._recipes.append(Recipe(name=name, products=products))

    def get_recipe_by_name(self, name) -> Recipe:
        '''Find product object by product name.'''
        for recipe in self._recipes:
            if name == recipe.name:
                return recipe

        raise RuntimeError(f'Recipe with name {name} was not found!')
