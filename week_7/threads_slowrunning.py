"""
ISCG5421 - threading module

Kris Pritchard / @krisrp
Sep 2020

"""
import threading
import time

def slow_thing(secs):
    print(f'B: Doing something that takes {secs}s.')
    time.sleep(secs)
    print('C: Finished doing that thing')

if __name__ == '__main__':
    print('A: This program does a thing')
    t1 = threading.Thread(target=slow_thing, args=(20,))
    t1.start()
    t2 = threading.Thread(target=slow_thing, args=(10,))
    t2.start()
    t1.join()  # Comment these out and see what they do
    t2.join()  # A better name than join would be 'pause and wait for thread to finish'
    print('D: Ending program')

