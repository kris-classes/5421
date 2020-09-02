import multiprocessing as mp
import time


def hi():
    for i in range(10):
        print('hello')
        time.sleep(1)


if __name__ == '__main__':
    p = mp.Process(target=hi)
    p.start()

