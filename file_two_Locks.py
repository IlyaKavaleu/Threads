import threading
import time

a = 5
b = 5

a_lock = threading.Lock()
b_lock = threading.Lock()


def thread1calc():
    global a
    global b

    print('Thread1 acquired lock a')
    a_lock.acquire()
    a_lock.release()

    time.sleep(5)

    print('Thread1 acquired lock b')
    b_lock.acquire()
    b_lock.release()
    time.sleep(5)
    a += 5
    b += 5
    print('Thread1 releasing both locks')


def thread2calc():
    global a
    global b

    print('Thread2 acquired lock b')
    b_lock.acquire()
    b_lock.release()
    time.sleep(5)

    print('Thread2 acquired lock a')
    a_lock.acquire()
    a_lock.release()
    time.sleep(5)
    a += 10
    b += 10
    print('Thread2 releasing both locks')


if __name__ == '__main__':
    t1 = threading.Thread(target=thread1calc)
    t1.start()

    t2 = threading.Thread(target=thread2calc)
    t2.start()
