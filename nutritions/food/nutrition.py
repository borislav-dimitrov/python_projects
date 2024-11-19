from food.utils import DishNames


class Nutrition:
    def __init__(self, name: str | DishNames, calories: int = 0, protein: int = 0, fat: int = 0, carbs: int = 0) -> None:
        self.name = name
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbs = carbs
