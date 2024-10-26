class Food:
    def __init__(self, name, calories, fat, carbs, protein, salt):
        self.name = name
        self.calories = calories
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
        self.salt = salt

    def calc_nutritions(self, ammount):
        '''
        Calculate the nutritions for the given ammount eaten.

        :param ammount: int - ammount of food eaten in grams!
        '''
        amt = ammount / 100

        return {
            'name': self.name,
            'ammount': ammount,
            'calories': self.calories * amt,
            'fat': self.fat * amt,
            'carbs': self.carbs * amt,
            'protein': self.protein * amt,
            'salt': self.salt * amt
        }
