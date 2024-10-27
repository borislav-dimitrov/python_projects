from y2023.day3.main import Solution as Solution3


def read_input(file):
    lines = []

    with open(file, 'r') as handler:
        lines = [line.strip() for line in handler.readlines()]

    return lines


def main():
    day3 = Solution3(read_input)


if __name__ == '__main__':
    main()
