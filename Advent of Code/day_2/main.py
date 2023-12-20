INPUT_FILE = r'.\day_2\inpt.txt'


class Solution:
    def __init__(self, inpt):
        self.inpt = inpt
        self.resolve()

    def resolve(self):
        print()
        print('Day 2')
        print(f'    Part 1 - {self.part_1()}')
        print(f'    Part 2 - {self.part_2()}')
        print('=======================================================')

    def part_1(self):
        sum_valid_games_id = 0

        for game in self.inpt:
            game_name, sets = self.define_sets(game)
            cubes_info = self.define_cubes_ct(game_name, sets)
            is_valid = self.game_is_possible(cubes_info, highest_r=12, highest_g=13, highest_b=14)
            if is_valid:
                sum_valid_games_id += int(game_name.split()[-1])

        return sum_valid_games_id

    def part_2(self):
        result = 0

        for game in self.inpt:
            game_name, sets = self.define_sets(game)
            cubes_info = self.define_cubes_ct(game_name, sets)
            result += cubes_info['red']['highest'] * cubes_info['green']['highest'] * cubes_info['blue']['highest']

        return result

    @staticmethod
    def define_sets(game):
        game, game_info = game.split(': ')
        sets = []
        for set_ in game_info.split(';'):
            sets.append(set_)

        return game, sets

    @staticmethod
    def define_cubes_ct(game_name, sets):
        result = {
            'name': game_name,
            'total': 0,
            'red': {'total': 0, 'highest': 0},
            'green': {'total': 0, 'highest': 0},
            'blue': {'total': 0, 'highest': 0},
        }

        for set_ in sets:
            new_set = set_.split(', ') if ',' in set_ else [set_]

            for s in new_set:
                cube_ct, color = s.split()
                if color in result:
                    result[color]['total'] += int(cube_ct)
                    if int(cube_ct) > result[color]['highest']:
                        result[color]['highest'] = int(cube_ct)
                else:
                    raise KeyError('Color not found!')
                result['total'] += int(cube_ct)
        return result

    @staticmethod
    def game_is_possible(game_info, highest_r, highest_g, highest_b):
        if (game_info['red']['highest'] <= highest_r
                and game_info['green']['highest'] <= highest_g
                and game_info['blue']['highest'] <= highest_b):
            return True
