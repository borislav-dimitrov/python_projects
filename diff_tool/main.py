import os
from utils import load_files, timeit, EOF


def mark_x_lines_for_diff(first, last, dict, diff_type):
    lines = []
    for i in range(first, last):
        key = get_n_key(dict, i)
        content, _ = get_content_line(key)
        lines.append(f'{diff_type}{content}')

    return lines


def scan_ahead_for_match(d1_line, d2_line, dict1, dict2):
    '''
    First scan ahead in dict2 since it is more logical
    for the change to be introduced in the new/changed file.
    Then scan ahead in dict1.

    :param d1_line: int - Current line in dict1 where change is spotted
    :param d2_line: int - Current line in dict2 where change is spotted
    :param dict1: dict - ...
    :param dict2: dict - ...
    :return: tuple | None - next matched rows or None
    '''
    n1 = len(dict1)
    n2 = len(dict2)
    d1_match = None
    d2_match = None
    # treshold = 0 if n1 <= 50000 else 1000
    counter = d2_line

    while counter < n2:
        # if treshold != 0 and counter >= treshold:
        #     break

        d2_key = get_n_key(dict2, counter)
        d2_content, _ = get_content_line(d2_key)
        d1_key = get_n_key(dict1, d1_line)
        d1_content, _ = get_content_line(d1_key)

        if d2_content == d1_content:
            d1_match = d1_line
            d2_match = counter
            break
        counter += 1

    if not d1_match and not d2_match:
        counter = d1_line

        while counter < n1:
            # if treshold != 0 and counter >= treshold:
            #     break

            d1_key = get_n_key(dict1, counter)
            d1_content, _ = get_content_line(d1_key)
            d2_key = get_n_key(dict2, d2_line)
            d2_content, _ = get_content_line(d2_key)

            if d2_content == d1_content:
                d1_match = counter
                d2_match = d2_line
                break
            counter += 1

    return d1_match, d2_match


def get_n_key(dict_, n):
    return list(dict_)[n]


def clean_diff(diff):
    while EOF in diff:
        diff.remove(EOF)

    return diff


def save_diff(diff):
    diff = clean_diff(diff)
    with open('diff.txt', 'w') as handler:
        for line in diff:
            handler.write(line + '\n')


def get_content_line(key):
    temp = key.split('_')
    line = int(temp[-1])
    content = '_'.join(temp[:-1])
    return content, line


def get_diff(dict1, dict2):
    diff = []
    tracker = []

    dict1_curr_line = 0
    dict2_curr_line = 0

    while dict2_curr_line < len(dict2) and dict1_curr_line < len(dict1):
        dict2_line = get_n_key(dict2, dict2_curr_line)
        dict2_content, dict2_line_nr = get_content_line(dict2_line)

        dict1_line = get_n_key(dict1, dict1_curr_line)
        dict1_content, dict1_line_nr = get_content_line(dict1_line)

        if dict1_content == dict2_content:
            # IGNORE
            diff.append(f'{dict2_content}')

            dict1_curr_line += 1
            dict2_curr_line += 1
        elif dict1_content != dict2_content:
            # DIFF
            d1_line, d2_line = scan_ahead_for_match(dict1_line_nr, dict2_line_nr, dict1, dict2)
            if d1_line is not None and d2_line is not None:
                # Offset lines and mark the diff
                if d1_line != dict1_curr_line:
                    diff.extend(mark_x_lines_for_diff(dict1_curr_line, d1_line, dict1, '- '))
                elif d2_line != dict2_curr_line:
                    diff.extend(mark_x_lines_for_diff(dict2_curr_line, d2_line, dict2, '+ '))

                dict1_curr_line = d1_line
                dict2_curr_line = d2_line
            else:
                # Should never come here
                raise Exception('Oops!')
        else:
            # Should never come here
            raise Exception('Oops!')

        if dict2_curr_line // 500 not in tracker:
            tracker.append(dict2_curr_line // 500)
            print(f'current lines d1, d2 = {dict1_curr_line, dict2_curr_line}')
    return diff


def lines_to_dict(lines):
    line_counter = 0
    new_obj = {}

    for line in lines:
        new_line = f'{line}_{line_counter}'
        new_obj[new_line] = line_counter

        line_counter += 1

    return new_obj


@timeit
def main_func():
    lines1, lines2 = load_files('file5.txt', 'file5 copy.txt')
    print('Loading... 20%')
    lines1 = lines_to_dict(lines1)
    print('Loading... 40%')
    lines2 = lines_to_dict(lines2)
    print('Loading... 60%')
    diff = get_diff(lines1, lines2)
    print('Loading... 80%')
    save_diff(diff)
    print('Loading... 100%')


if __name__ == '__main__':
    main_func()
