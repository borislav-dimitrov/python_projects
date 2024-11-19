from food import FoodManager
from food.utils import DishNames


def main() -> None:
    food_mgr = FoodManager()

    print(food_mgr.get_dish(DishNames.OAT_MEAL).dish_type)
    print(food_mgr.get_dish_nutrition(DishNames.OAT_MEAL, servings=1).__dict__)



if __name__ == '__main__':
    main()
