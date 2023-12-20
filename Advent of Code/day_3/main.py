INPUT_FILE = r'.\day_3\inpt.txt'


class Solution:
    def __init__(self, inpt):
        self.inpt = inpt
        self.resolve()

    def resolve(self):
        print()
        print('Day 3')
        print(f'    Part 1 - {self.part_1()}')
        print(f'    Part 2 - {self.part_2()}')
        print('=======================================================')

    def part_1(self):
        position_map = {}
        digits_to_sum = []

        for row_idx, line in enumerate(self.inpt):
            position_map[row_idx] = {}
            for char_idx in range(len(line)):
                position_map[row_idx][char_idx] = {'symbol': line[char_idx]}
                position_map[row_idx][char_idx]['is_digit'] = False
                position_map[row_idx][char_idx]['is_symbol'] = False

                if line[char_idx].isdigit():
                    position_map[row_idx][char_idx]['is_digit'] = True
                elif not line[char_idx].isdigit() and line[char_idx] != '.':
                    position_map[row_idx][char_idx]['is_symbol'] = True

        for row in position_map:
            prev_row = row - 1 if row != 0 else None
            next_row = row + 1 if row + 1 in position_map else None

            digit = ''
            digit_start = None

            for col in position_map[row]:
                if position_map[row][col]['symbol'].isdigit():
                    if digit == '':
                        digit_start = col

                    digit += position_map[row][col]['symbol']
                elif not position_map[row][col]['symbol'].isdigit() and digit != '':
                    valid_digit = self.check_digit_neighbours(digit, digit_start, col - 1, position_map, row, prev_row,
                                                              next_row)
                    if valid_digit:
                        digits_to_sum.append(valid_digit)
                    digit = ''

        inpt_text = ''.join(self.inpt)
        for digit in digits_to_sum:
            if inpt_text.count(f'.{digit}.') != digits_to_sum.count(digit):
                import pdb; pdb.set_trace()

        return sum(digits_to_sum)

    @staticmethod
    def check_digit_neighbours(digit, digit_start, digit_end, position_map, row, prev_row, next_row):
        neighbours = []
        valid = False

        # top / bottom
        for i in range(digit_start - 1, digit_end + 2):
            neighbours.append((prev_row, i))
            neighbours.append((next_row, i))

        # left
        neighbours.append((row, digit_start - 1))

        # right
        neighbours.append((row, digit_end + 1))

        for row, col in neighbours:
            if row in position_map and col in position_map[row]:
                if position_map[row][col]['is_symbol']:
                    valid = True
                    break

        if valid:
            return int(digit)

    def part_2(self):
        pass
