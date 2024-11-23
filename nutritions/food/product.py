from .nutrition import Nutrition


class Product:
    def __init__(self, name: str, hint: str, calories: int, protein: int, fat: int, carbs: int) -> None:
        self.name = name
        self.hint = hint
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbs = carbs

    def calc_nutrition(self, amount_grams: int) -> Nutrition:
        '''
        Calculate the nutrition for the given amount eaten.
        '''
        amount = amount_grams / 100
        nutrition = Nutrition(self.name)
        nutrition.calories += self.calories * amount
        nutrition.protein += self.protein * amount
        nutrition.fat += self.fat * amount
        nutrition.carbs += self.carbs * amount

        return nutrition
