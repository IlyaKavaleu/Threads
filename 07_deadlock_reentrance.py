import threading
import time

lock_obj = threading.Lock()
#
# print('Acquaire 1st time')
# lock_obj.acquire()
#
# print('Acquaire 2st time')
# lock_obj.acquire()
#
# print('Releasing')
# lock_obj.release()


def reentrance():
    print('start')
    lock_obj.acquire(timeout=2)
    print('Thread start')
    reentrance()
    print('ended')
reentrance()