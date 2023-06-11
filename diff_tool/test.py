import gc
from utils import timeit, load_files


ACTIONS = {
    'IGNORE': 'I',
    'ADD': '+',
    'REMOVE': '-'
}


def get_diff(lines1, lines2, max_chunk_len=1000):
    m1 = len(lines1)
    m2 = len(lines2)
    chunks = m1 // max_chunk_len

    distances = []
    actions = []

    for i in range(chunks):
        chunk = max_chunk_len if i != chunks - 1 else max_chunk_len + (m1 - (max_chunk_len * chunks))

        for _ in range(chunk):
            distances.append([0] * (m2 + 1))
        import pdb; pdb.set_trace()

    import pdb; pdb.set_trace()

    # for _ in range(m1 + 1):
    #     distances.append([0] * (m2 + 1))
    #     actions.append([0] * (m2 + 1))

    distances[0][0] = 0
    actions[0][0] = ACTIONS['IGNORE']

    for n2 in range(1, m2 + 1):
        n1 = 0
        distances[n1][n2] = n2
        actions[n1][n2] = ACTIONS['ADD']

    for n1 in range(1, m1 + 1):
        n2 = 0
        distances[n1][n2] = n1
        actions[n1][n2] = ACTIONS['REMOVE']

    for n1 in range(1, m1 + 1):
        for n2 in range(1, m2 + 1):
            if lines1[n1 - 1] == lines2[n2 - 1]:
                distances[n1][n2] = distances[n1 - 1][n2 - 1]
                actions[n1][n2] = ACTIONS['IGNORE']
                continue

            remove = distances[n1 - 1][n2]
            add = distances[n1][n2 - 1]

            distances[n1][n2] = remove
            actions[n1][n2] = ACTIONS['REMOVE']

            if distances[n1][n2] > add:
                distances[n1][n2] = add
                actions[n1][n2] = ACTIONS['ADD']

            distances[n1][n2] += 1

    patch = []
    n1 = m1
    n2 = m2

    while n1 > 0 or n2 > 0:
        action = actions[n1][n2]
        if action == ACTIONS['ADD']:
            n2 -= 1
            patch.append((ACTIONS['ADD'], n2, lines2[n2]))
        elif action == ACTIONS['REMOVE']:
            n1 -= 1
            patch.append((ACTIONS['REMOVE'], n1, lines1[n1]))
        elif action == ACTIONS['IGNORE']:
            n1 -= 1
            n2 -= 1
        else:
            assert False, 'unreachable'

    patch.reverse()
    return patch


def save_diff(diff):
    with open('diff.txt', 'w') as handle:
        for line in diff:
            handle.write(f'{line[0]}{line[2]}')


def main_func():
    a_lines, b_lines = load_files(a_file='file1.txt', b_file='file2.txt')
    diff = get_diff(a_lines, b_lines)
    save_diff(diff)


if __name__ == '__main__':
    main_func()
