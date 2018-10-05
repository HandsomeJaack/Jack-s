c = {1: "one",
     0: "zero",
     True: "true",
     False: "false"}
# -> {1: 'true', 0: 'false'}, таким будет вывод этого словвря
# т.к. 1 == True
print(c)
print(2*False + True)
# -> 1
print({"one": 1, "two": 2, "three": 3} == dict(one=1, two=2, three=3))
a = {1, 2, 3}      # множества
b = {0, 2, 4}
print(a & b)     # -> {2}
print(a | b)     # -> {0, 1, 2, 3, 4}
print(a ^ b)     # -> {0, 1, 3, 4}
print(a - b)     # -> {1, 3}, однако один арифметический
                 # оператор всё же оставили