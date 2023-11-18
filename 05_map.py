# import concurrent.futures
# from search import read_ints, search_three_numbers
#
# if __name__ == '__main__':
#     print('started main')
#     data = read_ints('file.txt')
#     with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#         results = executor.map(search_three_numbers, (data, data, data, data), ('t1', 't2', 't3', 't4'))  #map
#         for result in results:
#             print(result)
#
#     print('Ended main')
#
import threading

# Общая переменная
counter = 0

# Функция для инкрементации
def increment():
    global counter
    for _ in range(1000000):
        counter += 1

# Создаем два потока, которые инкрементируют счетчик
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

# Запускаем потоки
thread1.start()
thread2.start()

# Ждем завершения потоков
thread1.join()
thread2.join()

# Выводим результат
print("Counter:", counter)
