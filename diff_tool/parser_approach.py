def find_pair(idx, pairs):
    for pair in pairs[::-1]:
        if pair['end'] is None:
            return pairs.index(pair)

    return pairs

def replace_in_string(pos, stringg, new_char=-1):
    stringg = [*stringg]
    if new_char == -1:
        stringg.pop(pos)
    else:
        stringg[pos] = new_char
    return ''.join([str(i) for i in stringg])

def get_pairs():
    start_idx = []
    pairs = []
    end_idx = []
    ctr = 0

    while ctr < len(content):
        if content[ctr] == '{' and ctr not in start_idx:
            pairs.append({'start': ctr, 'end': None})
            start_idx.append(ctr)
        elif content[ctr] == '}' and ctr not in end_idx:
            pair_nr = find_pair(ctr, pairs)
            if pair_nr is not None:
                pairs[pair_nr]['end'] = ctr
                pairs[pair_nr]['content'] = content[pairs[pair_nr]['start']:pairs[pair_nr]['end']]
            end_idx.insert(0, ctr)

        ctr += 1

    return start_idx, end_idx, pairs

def get_idx(content):
    new = {}
    keys = []

    start_idx, end_idx, pairs = get_pairs()

    for pair in pairs:
        print(pair['content'])


    return start_idx, end_idx

def main_func(content):
    start, end = get_idx(content)

    for idx in start:
        content = content[:idx-1] + ': ' + content[idx:]

if __name__ == '__main__':
    with open('file5.txt', 'r') as handler:
        content = ''.join(handler.readlines()).strip()

    main_func(content)
