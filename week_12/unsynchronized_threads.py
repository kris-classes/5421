"""
ISCG5421 S2 2020

A simple in-class example to show how unsynchronized threads can lead to incorrect results.
"""
import threading
import time


# Using a global variable to demonstrate issues with multiple threads operating on data without synchronization.
counter = 0

def adder(amount):
    global counter
    for i in range(amount):
        counter += 1
        name = threading.current_thread().name
        # NOTE: If you uncomment this print you'll likely get correct behaviour.
        #print(f'{name} counter: {counter}')

    print(f'{name} final value: {counter}')
    return counter


threads = []
NUM_THREADS = 10
COUNT_MAX = 100000

for i in range(NUM_THREADS):
    t = threading.Thread(target=adder, args=(COUNT_MAX,))
    #threads.append(t)
    print(f'Starting thread: {t.name}')
    t.start()

#for thread in threads:
#    thread.start()

# NOTE: The correct 
print(f'Final counter value expected: {NUM_THREADS*COUNT_MAX}: Got {counter}')
