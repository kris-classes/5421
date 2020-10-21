"""
ISCG5421 S2 2020

In-class example of using asyncio for concurrency.
"""

import asyncio
import time

async def do_thing(start_msg, end_msg, time_taken):
    print(start_msg)
    await asyncio.sleep(time_taken)
    print(end_msg)

async def make_fries():
    await do_thing('Making fries', 'Finished making fries', 5)

async def serve_customer():
    await do_thing('Serving customer', 'Finished serving customer', 4)

async def make_burger():
    await do_thing('Making burger', 'Finished making burger', 3)


async def main():
    
    print('Starting synchronous example')
    # Tasks created from coroutines here can be run concurrently
    make_fries_task = asyncio.create_task(make_fries())
    make_burger_task = asyncio.create_task(make_burger())
    serve_customer_task = asyncio.create_task(serve_customer())
    await make_fries_task
    await make_burger_task
    await serve_customer_task
    # How to make coroutines behave synchronously
    print('Finished')
    print('==========')
    print('Starting synchronous example')
    await make_fries()
    await make_burger()
    await serve_customer()
    print('Finished')

asyncio.run(main())
