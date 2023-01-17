import time, threading


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop)
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)


# Lock
balance = 0


def change_it(n):
    global balance
    balance += n
    balance -= n


# def run_thread(n):
#     for i in range(2000000):
#         change_it(n)

lock = threading.Lock()


def run_thread(n):

    for i in range(2000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()


t1 = threading.Thread(target=run_thread(5))
t2 = threading.Thread(target=run_thread, args=(10,))
# t1.start()
t2.start()
# t1.join()
t2.join()
print(balance)

