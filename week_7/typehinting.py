"""
Example of type hinting for ISCG5421

Kris Pritchard / Sep 2020

Run with:
    mypy typehinting.py

You should see errors like this:

    typehinting.py:16: error: Argument 1 to "hello" has incompatible type "int"; expected "str"
    typehinting.py:16: error: Argument 2 to "hello" has incompatible type "str"; expected "int"
    Found 2 errors in 1 file (checked 1 source file)
"""

def hello(name: str, age: int = 25) -> int:
    print(f'Hello {name}. You are {age} years old.')
    return age + 1


hello('bob', 20)
hello(42, 'anne')
