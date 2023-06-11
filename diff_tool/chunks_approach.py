from difflib import SequenceMatcher, Differ
from utils import timeit

DIFFER = Differ()


def compare_files_with_row_numbers(lines1, lines2):
    import pdb; pdb.set_trace()
    delta = DIFFER.compare(lines1, lines2)
    return delta

def chunks(content, chunk_size=1000):
    for i in range(0, len(content), chunk_size):
        yield content[i:i + chunk_size]


@timeit
def main_func():
    # file1 = 'file5.txt'
    # file2 = 'file5 copy.txt'
    file1 = 'file6.txt'
    file2 = 'file7.txt'
    output = 'diff.txt'
    result = ''


    with open(file1, 'r') as handler1, open(file2, 'r') as handler2:
        lines1 = handler1.readlines()
        lines2 = handler2.readlines()
    print('Files loaded.')

    if len(lines1) > len(lines2):
        for _ in range(len(lines1) - len(lines2)):
            lines2.append('\n')
    if len(lines1) < len(lines2):
        for _ in range(len(lines2) - len(lines1)):
            lines1.append('\n')

    assert len(lines1) == len(lines2)
    print('File lengths verified.')

    if len(lines1) >= 10000 and len(lines2) >= 10000:
        lines1 = chunks(lines1)
        print(f'    Done splitting lines 1 in chunks.')
        lines2 = chunks(lines2)
        print(f'    Done splitting lines 2 in chunks.')

        print('    Starting comparison.')
        counter = 1
        result_chunks = []
        for chunk1, chunk2 in zip(lines1, lines2):
            result_chunks.append(compare_files_with_row_numbers(chunk1, chunk2))
            print(f'    comparing chunk {counter} done.')
            counter += 1

        print('    Saving file.')
        with open(output, 'w') as handler3:
            for chunk in result_chunks:
                for line in chunk:
                    import pdb; pdb.set_trace()
                    handler3.write(result)
    else:
        result = compare_files_with_row_numbers(lines1, lines2)

    print('Saving file.')
    with open(output, 'w') as handler3:
        handler3.write(result)

if __name__ == '__main__':
    main_func()
