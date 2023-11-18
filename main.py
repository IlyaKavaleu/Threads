import concurrent.futures
import threading
import time

from decoratore import measure_time
from search import read_ints, search_three_numbers

def parallel(ints):
    thread_name = threading.current_thread().name
    print(f'Current thread --- {thread_name}')
    futures = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        futures.append(executor.submit(search_three_numbers, ints, thread_name+'1'))
        futures.append(executor.submit(search_three_numbers, ints, thread_name+'2'))
        futures.append(executor.submit(search_three_numbers, ints, thread_name+'3'))
        futures.append(executor.submit(search_three_numbers, ints, thread_name+'4'))
        futures.append(executor.submit(search_three_numbers, ints, thread_name+'5'))
        futures.append(executor.submit(search_three_numbers, ints, thread_name+'6'))

        for future in concurrent.futures.as_completed(futures):
            while not future.done():
                print('#', end='')
                time.sleep(0.3)

            print(f'{future.result()}')

        print('Something')
    print('Ended main')


if __name__ == '__main__':
    print('Start main')
    ints = read_ints('file.txt')
    parallel(ints)
    print('Finished main')
