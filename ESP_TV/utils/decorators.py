import time


def time_it(function_to_be_timed):
    '''Timer Decorator'''
    def wrapper(*args, **kwargs):
        start = time.time()

        function_to_be_timed(*args, **kwargs)

        end = time.time()
        print(f'Function {function_to_be_timed.__name__} ran in {end - start} seconds!')

    return wrapper
