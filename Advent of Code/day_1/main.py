from utils import DIGIT_MAP

INPUT_FILE_1 = r'.\day_1\inpt1.txt'
INPUT_FILE_2 = r'.\day_1\inpt2.txt'


class Solution:
    def __init__(self, inpt1, inpt2):
        self.inpt1 = inpt1
        self.inpt2 = inpt2
        self.resolve()

    def resolve(self):
        print()
        print('Day 1')
        print(f'    Part 1 - {self.part_1()}')
        print(f'    Part 2 - {self.part_2()}')
        print('=======================================================')

    def part_1(self):
        total = 0
        for line in self.inpt1:
            numerics = self.find_first_last_numerics(line)
            total += numerics
        return total

    @staticmethod
    def find_first_last_numerics(line):
        numbers = []
        for char in line:
            if char.isnumeric():
                numbers.append(char)
        return int(f'{numbers[0]}{numbers[-1]}')

    def part_2(self):
        total = 0
        for line in self.inpt2:
            numerics = self.find_numerics_from_chars(line)
            total += numerics

        return total

    @staticmethod
    def find_numerics_from_chars(line):
        numbers = []

        for idx, char in enumerate(line.lower()):
            if char.isnumeric():
                numbers.append(char)
                continue

            for digit in DIGIT_MAP:
                if digit.startswith(char) and line[idx:idx + len(digit)] == digit:
                    numbers.append(DIGIT_MAP[digit])
                    break

        return int(f'{numbers[0]}{numbers[-1]}')
