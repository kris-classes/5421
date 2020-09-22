"""Tuples"""

my_tuple = (123, 567)
type(my_tuple)
print(type(my_tuple))
print(type(123))
print(my_tuple[0])
my_tuple.count(567)
my_tuple.index(123, 0)

# my_tuple[0] = 42  #this will raise a type error

"""Primitive Types"""

print(type("Hello"))

str(123)

int("123")

print(type(123.045))

x = float("inf")

print(x)
print(x + 1)
print(x + 1000000)

print(bool("Hello"))

print(bool("False"))
print(bool("false"))
print(bool(""))

print(bool([5, 8, 200, "fred"]))
print(bool([]))
my_list = [676, 777, 456]
while len(my_list) > 0:
    val = my_list.pop()
    print(val)
my_list2 = [676, 777, 456]
while my_list2:
    val = my_list2.pop()
    print(val)

help(my_tuple)

"""Sets"""

my_set = set([12, 12, 42, 42, 77, 55])
print(my_set)

set_a = {1, 2, 3, 10, 15, 77}
set_b = {3, 4, 5}
print(set_a & set_b)
print(set_a | set_b)
print(set_a.intersection(set_b))
print(set_a.union(set_b))
print(set_a.difference(set_b))
print(set_a - set_b)
print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)
for item in set_a:
    print(f"item: {item}")

for item in range(0, len(set_a), 2):
    print(f'range:, {item}')
print("blah blah blah")
# help(set)

for i in range(10, 0, -3):
    print(i)

for i, item in enumerate(["Hi", "Bye", "Kia Ora"]):
    print(f"{i}, {item}")

"""Dictionaries"""

my_dict = {"k": 42, "l": 55}
print(my_dict["k"])
#print(my_dict["o"])  #raises key error
print(my_dict.get("k"))
print(my_dict.get("o"))
print(my_dict.get("z", 70))
print("Hello")
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
for k,v in my_dict.items():
    print(k,v)