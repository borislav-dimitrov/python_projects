import difflib
from utils import timeit
from diff_match_patch import diff_match_patch



def read_file_in_chunks(file_path, chunk_size):
    with open(file_path, 'r') as file:
        for line in file:
            yield line


def compare_files(file1, file2, output_file):
    chunk_size = 1000  # Adjust the chunk size as needed

    generator1 = read_file_in_chunks(file1, chunk_size)
    generator2 = read_file_in_chunks(file2, chunk_size)

    diff = difflib.ndiff(list(generator1), list(generator2))
    diff_lines = list(diff)

    # Save the output to a file
    with open(output_file, 'w') as f:
        for line in diff_lines:
            if line.startswith('- '):
                f.write(f"-{line[2:]}")
            elif line.startswith('+ '):
                f.write(f"+{line[2:]}")
            elif line.startswith('? '):
                f.write(f" {line[2:]}")
            elif line.startswith('  '):
                f.write(f" {line[2:]}")


def compare_files2(file1, file2, output_file):
    dmp = diff_match_patch()

    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        text1 = f1.read()
        text2 = f2.read()

    diffs = dmp.diff_main(text1, text2)
    diff_lines = [f"{sign}{line}" for sign, line in diffs]

    with open(output_file, 'w') as f:
        f.writelines(diff_lines)


@timeit
def main():
    file1 = 'file5.txt'
    file2 = 'file5 copy.txt'
    file3 = 'diff.txt'
    # with open(file1, 'r') as file1, open(file2, 'r') as file2:
    #         lines1 = file1.readlines()
    #         lines2 = file2.readlines()

    compare_files2(file1, file2, file3)

if __name__ == '__main__':
    main()
