# Ex 1
def reverse_tuple():
    tuple1 = (10, 20, 30, 40, 50)
    reverse = tuple1[::-1]
    print(reverse)


reverse_tuple()
print('----------------')


# Ex 2
def access_value():
    tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
    num = tuple1[1][1]
    print(num)


access_value()
print('----------------')


# Ex 3
def create_tuple():
    tuple1 = (50,)
    print(tuple1)


create_tuple()
print('----------------')


# Ex 4
def unpack_tuple():
    tuple1 = (10, 20, 30, 40)
    a, b, c, d = tuple1  # unpacking in var
    print(a)
    print(b)
    print(c)
    print(d)


unpack_tuple()
print('----------------')


# Ex 5
def swap_tuple():
    tuple1 = (11, 22)
    tuple2 = (99, 88)
    tuple1, tuple2 = tuple2, tuple1
    print('Tuple1:', tuple1)
    print('Tuple2:', tuple2)


swap_tuple()
print('----------------')


# Ex 6
def copy_els():
    tuple1 = (11, 22, 33, 44, 55, 66)
    tuple2 = tuple1[3:-1]
    print('New tuple:', tuple2)


copy_els()
print('----------------')


# Ex 7
def modify_tuple():
    tuple1 = (11, [22, 33], 44, 55)  # 22 to 222
    tuple1[1][0] = 222
    print('New item in tuple:', tuple1)


modify_tuple()
print('----------------')


# Ex 8
def sort_tuple():
    tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))  # by 2nd item
    tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))  # lambda - takes any numbers of args
    print(tuple1)


sort_tuple()
print('----------------')


# Ex 9
def count_els_tuple():
    tuple1 = (50, 10, 60, 70, 50)
    print('This is a normal tuple count of 50: ', tuple1.count(50))
    print('This is a tuple into a list and counted 50: ', list(tuple1).count(50))


count_els_tuple()
print('----------------')


# Ex 10
def check_tuple():
    tuple1 = (45, 45, 45, 45)
    for x in tuple1:
        if x == x:
            print(True)


check_tuple()
print('----Till the end of the journey---- 😀')
