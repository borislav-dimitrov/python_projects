import time


EOF = '\n==== eof tag ===='


def timeit(f):
    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        separator = '\n======================\n'
        print(f'{separator}Function: {f.__name__}\nArgs: [{args}, {kw}]\nTook: {te-ts:2.4f} sec{separator}')
        return result
    return timed


def load_files(a_file='file1.txt', b_file='file2.txt', list=True):
    if list:
        with open(a_file) as a_handle:
            a_lines = [line.rstrip() for line in a_handle]

        with open(b_file) as b_handle:
            b_lines = [line.rstrip() for line in b_handle]
    else:
        with open(a_file) as a_handle:
            a_lines = ''.join(a_handle.readlines())

        with open(b_file) as b_handle:
            b_lines = ''.join(b_handle.readlines())

    a_lines.append(EOF)
    b_lines.append(EOF)
    if len(a_lines) < len(b_lines):
        while len(a_lines) != len(b_lines):
            a_lines.append(EOF)
    if len(a_lines) > len(b_lines):
        while len(a_lines) != len(b_lines):
            b_lines.append(EOF)

    return a_lines, b_lines
