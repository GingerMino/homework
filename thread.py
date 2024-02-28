import threading
import time

def countdown(threadName, delay):
    while True:
        if threadName == 'Thread-1':
            for i in range(10, 0, -1):
                print(f'{threadName} : {i}')
                time.sleep(1)
            print(f'{threadName} : STOP')
            break
        elif threadName == 'Thread-2':
            for i in range(10, 0, -1):
                print(f'{threadName} : {i}')
                time.sleep(1)
            print(f'{threadName} : STOP')
            break

thread1 = threading.Thread(target=countdown, args=('Thread-1', 1))
thread2 = threading.Thread(target=countdown, args=('Thread-2', 1))

thread1.start()
thread2.start()