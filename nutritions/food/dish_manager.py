from .dish import Dish
from .recipe import Recipe
from .utils import DishTypes


class DishManger:
    def __init__(self) -> None:
        self._dishes: list[Dish] = []

    def add_dish(self, recipe: Recipe, dish_type: DishTypes) -> None:
        '''Add a new dish.'''
        self._dishes.append(Dish(recipe, dish_type))

    def get_dish_by_name(self, name) -> Dish | None:
        '''Find dish object by dish name.'''
        for dish in self._dishes:
            if name == dish.name:
                return dish