import json
from food import Food


class FoodManager:
    def __init__(self):
        self.foods = []
        self.create_food_objects()

    def load_foods(self):
        with open('nutritions_per_100.json', 'r') as file_handler:
            foods = json.load(file_handler)
        return foods

    def create_food_objects(self):
        '''Loaded foods data from json'''
        foods = self.load_foods()

        if not foods:
            raise Exception('Couldn\'t load foods from the json file!')

        for food_name in foods:
            self.foods.append(Food(food_name, foods[food_name]['calories'], foods[food_name]['fat'],
                                foods[food_name]['carbs'], foods[food_name]['protein'], foods[food_name]['salt']))

    def get_food_by_name(self, name) -> Food:
        '''Find food object by food name'''
        for food in self.foods:
            if name == food.name:
                return food

        raise Exception(f'Food with name {name} was not found in the database!')

    def calc_nutritions(self, food_eaten):
        '''
        Calculate the nutritions of the given food.

        :param food_eaten: list[dict, ...] - List with dictionaries containing food name and food amt
        [{'name': 'sample_food_name', 'amt': 100}]
        '''
        per_food = []
        total = {
            'ammount': 0,
            'calories': 0,
            'fat': 0,
            'carbs': 0,
            'protein': 0,
            'salt': 0,
        }

        for food_info in food_eaten:
            food = self.get_food_by_name(food_info['name'])
            nutritions = food.calc_nutritions(food_info['amt'])

            per_food.append(nutritions)

            total['ammount'] += nutritions['ammount']
            total['calories'] += nutritions['calories']
            total['fat'] += nutritions['fat']
            total['carbs'] += nutritions['carbs']
            total['protein'] += nutritions['protein']
            total['salt'] += nutritions['salt']

        return per_food, total
