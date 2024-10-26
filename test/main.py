import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def func(time_: int):
    time.sleep(time_)
    return f'slept for {time_}s'


if __name__ == '__main__':
    start = time.time()
    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        futures = []

        for i in [6, 3, 4, 1, 3, 5, 2]:
            futures.append(executor.submit(func, i))

        for future in as_completed(futures):
            print(future.result())

    print(f'Elapsed time: {time.time() - start}')
