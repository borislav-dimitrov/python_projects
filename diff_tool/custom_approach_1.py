import os
from utils import timeit


def load_files(f_path_1, f_path_2):
    with open(f_path_1, 'r') as a_handle:
        a_lines = [line.rstrip() for line in a_handle]

    with open(f_path_2, 'r') as b_handle:
        b_lines = [line.rstrip() for line in b_handle]

    return a_lines, b_lines

class DiffTool:
    def __init__(self, holy_content, other_content):
        self.holy_content = holy_content
        self.holy_len = len(holy_content)
        self.other_content = other_content
        self.other_len = len(other_content)
        self.nr_of_rows = max(self.holy_len, self.other_len)
        self.diff = []


    def get_diff(self):
        for row in range(self.nr_of_rows):
            holy_line = self.holy_content[row] if row < self.holy_len else self.holy_content[-1]
            other_line = self.other_content[row] if row < self.other_len else self.other_content[-1]

            if other_line != holy_line:
                self._diff_spotted(other_line, holy_line, row)
            if other_line == holy_line:
                self.diff.append(('*   ', other_line, str(row)))

    def _diff_spotted(self, other, holy, row):
        if self.other_content[row] != holy:
            self.diff.append(('DIFF', other, holy, str(row)))

    def dump_diff(self, file_path):
        with open(os.path.normpath(file_path), 'w') as handle:
            for rec in self.diff:
                handle.write(f'{rec[0]} {rec[1]}\n')

@timeit
def main_func():
    holy_content, other_content = load_files('file3.txt', 'file4.txt')
    diff_tool = DiffTool(holy_content=holy_content, other_content=other_content)
    diff_tool.get_diff()
    diff_tool.dump_diff('diff.txt')

if __name__ == '__main__':
    main_func()
