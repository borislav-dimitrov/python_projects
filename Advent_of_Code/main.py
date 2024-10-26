def load_input():
    with open('input.txt', 'r') as handler:
        lines = [i.strip() for i in handler.readlines()]

    return lines


def process(inpt):
    digit_line_pos, symbol_line_pos = collect_digit_symbol_info(inpt)
    print(digit_line_pos, symbol_line_pos, sep='\n\n')

    for symbol, symbol_line_nr, symbol_pos_nr in symbol_line_pos:
        for digit, digit_line_nr, digit_pos_nr in digit_line_pos:
            pass


def collect_digit_symbol_info(inpt):
    digit_line_pos = []
    symbol_line_pos = []

    for line_nr, line in enumerate(inpt):
        for idx, char in enumerate(line):
            if is_digit(char):
                digit_line_pos.append((char, line_nr, idx))
            else:
                if char != '.':
                    symbol_line_pos.append((char, line_nr, idx))

    return digit_line_pos, symbol_line_pos


def is_digit(char: str) -> bool:
    if char.isdigit():
        return True
    return False


def main():
    inpt = load_input()
    process(inpt)


if __name__ == '__main__':
    main()
