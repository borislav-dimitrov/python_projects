from copy import deepcopy

INPT_FILE = r'y2023\day3\puzzle.txt'


class ObjTypes:
    DOT = 'DOT'
    SYMBOL = 'SYMBOL'
    NUMBER = 'NUMBER'
    PART_NR = 'PART_NR'


class Obj:
    def __init__(self, symbol, row, column, obj_type) -> None:
        self.symbol = symbol
        self.row = row
        self.column = column
        self.obj_type = obj_type


class PartNumber:
    def __init__(self, numbers: list[Obj]) -> None:
        self.numbers = numbers
        self.value = int(''.join([n.symbol for n in self.numbers]))
        self.row = self.numbers[0].row
        self.column_start = min([n.column for n in self.numbers])
        self.column_end = max([n.column for n in self.numbers])
        self.is_valid = False


class Solution:
    def __init__(self, read_file_func) -> None:
        self._input = read_file_func(INPT_FILE)
        self._dots: list[Obj] = []
        self._symbols: list[Obj] = []
        self._numbers: list[Obj] = []
        self._part_nrs: list[PartNumber] = []
        self._gears = []

        self._resolve()

    def _resolve(self):
        # Part 1
        self._process_objects_from_input()
        self._find_part_numbers()
        self._validate_part_numbers()

        part_nrs_sum = sum(pn.value for pn in self._part_nrs if pn.is_valid)
        print(f'Valid part nrs sum: {part_nrs_sum}')

        # Part 2
        self._find_gears()
        gear_ratio_sum = sum(self._gears)
        print(f'Gear ratio sum: {gear_ratio_sum}')

    def _process_objects_from_input(self):
        for row, row_text in enumerate(self._input):
            for column, symbol in enumerate(row_text):
                if symbol == '.':
                    self._dots.append(Obj(
                        symbol=symbol, row=row, column=column, obj_type=ObjTypes.DOT
                    ))
                elif symbol.isnumeric():
                    self._numbers.append(Obj(
                        symbol=symbol, row=row, column=column, obj_type=ObjTypes.NUMBER
                    ))
                else:
                    self._symbols.append(Obj(
                        symbol=symbol, row=row, column=column, obj_type=ObjTypes.SYMBOL
                    ))

    def _find_part_numbers(self):
        consecutive = []

        for idx, number in enumerate(self._numbers):
            consecutive.append(number)
            if idx + 1 == len(self._numbers):
                self._part_nrs.append(PartNumber(deepcopy(consecutive)))
                consecutive.clear()
                continue

            if self._numbers[idx + 1].column != number.column + 1:
                self._part_nrs.append(PartNumber(deepcopy(consecutive)))
                consecutive.clear()

    def _validate_part_numbers(self):
        for pn in self._part_nrs:
            self._validate_pn(pn)

    def _validate_pn(self, pn: PartNumber):
        valid_rows = [i for i in range(pn.row - 1, pn.row + 2) if i >= 0]
        valid_cols = [i for i in range(pn.column_start - 1, pn.column_end + 2) if i >= 0]

        for symbol in self._symbols:
            if symbol.row in valid_rows and symbol.column in valid_cols:
                pn.is_valid = True
                return

    def _find_gears(self):
        for symbol in self._symbols:
            if symbol.symbol != '*':
                continue

            self._validate_gear(symbol)

    def _validate_gear(self, star: Obj):
        valid_rows = [i for i in range(star.row - 1, star.row + 2) if i >= 0]
        valid_cols = [i for i in range(star.column - 1, star.column + 2) if i >= 0]
        adjecent_pns = []

        for pn in self._part_nrs:
            pn_columns = [i for i in range(pn.column_start, pn.column_end + 1)]

            if pn.row not in valid_rows:
                continue

            if any(num in set(valid_cols) for num in pn_columns):
                adjecent_pns.append(pn)

        if len(adjecent_pns) == 2:
            self._gears.append(adjecent_pns[0].value * adjecent_pns[1].value)
