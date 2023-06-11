import difflib
from utils import timeit


def compare_files(file1_path, file2_path, file3_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2, open(file3_path, 'w') as output:
        lines1 = file1.readlines()
        lines2 = file2.readlines()

        diff = difflib.unified_diff(lines1, lines2, fromfile=file1_path, tofile=file2_path, lineterm='')
        diff = iter(diff)
        for line in diff:
            if (line.startswith('---')
                or line.startswith('+++')
                or line.startswith('@@') and line.endswith('@@')):
                # Skip difflib headers
                continue
            else:
                output.write(line)


@timeit
def main_func():
    file1_path = 'file1.txt'
    file2_path = 'file2.txt'
    output = 'diff.txt'

    compare_files(file1_path, file2_path, output)


if __name__ == '__main__':
    main_func()
