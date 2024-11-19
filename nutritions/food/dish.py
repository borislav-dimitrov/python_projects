from .nutrition import Nutrition
from .recipe import Recipe
from .utils import DishTypes


class Dish:
    def __init__(self, recipe: Recipe, dish_type: DishTypes) -> None:
        self.name = recipe.name
        self.dish_type = dish_type
        self._recipe = recipe

    def _nutrition_per_serving(self) -> Nutrition:
        '''Calculate the nutrition that the current recipe provides for the specified amount of servings.'''
        dish_nutrition_per_serving = Nutrition(self.name)

        for (product, amount) in self._recipe.get_products():
            product_nutrition: Nutrition = product.calc_nutrition(amount)

            dish_nutrition_per_serving.calories += product_nutrition.calories
            dish_nutrition_per_serving.protein += product_nutrition.protein
            dish_nutrition_per_serving.fat += product_nutrition.fat
            dish_nutrition_per_serving.carbs += product_nutrition.carbs

        return dish_nutrition_per_serving

    def nutrition(self, servings: float = 1) -> Nutrition:
        '''Calculate the nutrition that the current recipe provides for the specified amount of servings.'''
        per_serving = self._nutrition_per_serving()

        per_serving.servings = servings
        per_serving.calories *= servings
        per_serving.protein *= servings
        per_serving.fat *= servings
        per_serving.carbs *= servings

        return per_serving
