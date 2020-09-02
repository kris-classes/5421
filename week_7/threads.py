import threading as th
import time


def hi(name):
    for i in range(100):
        print(f'hello {name} - from a thread')
        time.sleep(1)

def count():
    for i in range(100):
        print(i)
        time.sleep(0.2)


if __name__ == '__main__':
    t = th.Thread(target=hi, args=('wipun',)) 
    t.start()
    t2 = th.Thread(target=count)
    t2.start()

