from food_manager import FoodManager


def print_result(per_food, total):
    '''Print the result nicely'''
    print('==== PER FOOD ====')
    per_food_title = f'{"Food Name":<30} {"Amt [gr]":<15} {"Calories":<13} {"Fat":<8} {"Carbs":<10} {"Protein":<10} {"Salt":<5}'
    separator = '=' * len(per_food_title)

    print(separator)
    print(per_food_title)
    print(separator)
    for food in per_food:
        name = food['name']
        amt = food["ammount"]
        calories = round(food['calories'], 2)
        fat = round(food['fat'], 2)
        carbs = round(food['carbs'], 2)
        protein = round(food['protein'], 2)
        salt = round(food['salt'], 2)

        print(f'{name:<30} {amt:<15} {calories:<13} {fat:<8} {carbs:<10} {protein:<10} {salt:<5}')

    print(separator)

    print('\n\n==== TOTAL ====')
    amt = total["ammount"]
    calories = round(total['calories'], 2)
    fat = round(total['fat'], 2)
    carbs = round(total['carbs'], 2)
    protein = round(total['protein'], 2)
    salt = round(total['salt'], 2)
    total_title = f'{"Amt [gr]":<15} {"Calories":<13} {"Fat":<8} {"Carbs":<10} {"Protein":<10} {"Salt":<5}'
    separator = '=' * len(total_title)
    print(separator)
    print(total_title)
    print(separator)
    print(f'{amt:<15} {calories:<13} {fat:<8} {carbs:<10} {protein:<10} {salt:<5}')
    print(separator)


def main():
    food_mgr = FoodManager()
    food_eaten = [{'name': 'LIDL_FRESHONA_chickpeas_can', 'amt': 240},
                  {'name': 'LIDL_NIXE_tuna_fillets', 'amt': 50}]

    per_food, total = food_mgr.calc_nutritions(food_eaten)

    print_result(per_food, total)


if __name__ == '__main__':
    main()
