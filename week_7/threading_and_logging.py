"""
ISCG5421 - threading module

Kris Pritchard / @krisrp
Sep 2020

"""
import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(funcName)s %(message)s',
)

class MyCustomThread(threading.Thread):
    def run(self):
        logging.debug('Running custom thread')

def worker():
    logging.debug('Doing some work')
    time.sleep(3)
    logging.debug('Finished doing work')

if __name__ == '__main__':
    logging.info('Program is running')
    t1 = threading.Thread(target=worker)
    t1.start()
    logging.warning('Warning message')
    customthread = MyCustomThread()
    customthread.start()
