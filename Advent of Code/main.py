from day_1.main import Solution as Solution1, INPUT_FILE_1 as IF_1_1, INPUT_FILE_2 as IF_1_2
from day_2.main import Solution as Solution2, INPUT_FILE as IF_2_1
from day_3.main import Solution as Solution3, INPUT_FILE as IF_3_1


def read_input(file):
    lines = []

    with open(file, 'r') as handler:
        lines = [line.strip() for line in handler.readlines()]

    return lines


def main():
    day_1 = Solution1(read_input(IF_1_1), read_input(IF_1_2))
    day_2 = Solution2(read_input(IF_2_1))
    day_3 = Solution3(read_input(IF_3_1))


if __name__ == '__main__':
    main()
