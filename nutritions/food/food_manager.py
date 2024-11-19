from .dish import Dish
from .nutrition import Nutrition
from .product_manager import ProductManager
from .recipe_manager import RecipeManager
from .dish_manager import DishManger
from .utils import DishNames, DishTypes


class FoodManager:
    def __init__(self):
        self._product_mgr = ProductManager()
        self._recipe_mgr = RecipeManager()
        self._dish_mgr = DishManger()

        self._initialize_recipes()
        self._initialize_dishes()

    def _initialize_recipes(self) -> None:
        self._recipe_mgr.create_recipe(
            name=DishNames.OAT_MEAL, products=[
                [self._product_mgr.get_product_by_name('LIDL_CROWNFIELD_oat_flakes'), 100],
                [self._product_mgr.get_product_by_name('LIDL_VEMONDO_oat_milk'), 200],
            ]
        )

    def _initialize_dishes(self) -> None:
        self._dish_mgr.add_dish(self._recipe_mgr.get_recipe_by_name(DishNames.OAT_MEAL), dish_type=DishTypes.BREAKFAST)

    def get_dish(self, name: str) -> Dish:
        return self._dish_mgr.get_dish_by_name(name)

    def get_dish_nutrition(self, name: str, servings: float = 1) -> Nutrition:
        dish = self._dish_mgr.get_dish_by_name(name)

        if not dish:
            raise RuntimeError(f'Could not find a dish with name - {name}!')

        return dish.nutrition(servings)