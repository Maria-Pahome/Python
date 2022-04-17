# Ex 1
def user(name, age):
    print(name, age)


user('George', '24')
print('----------')


# Ex 2
def var_length(*sequence):
    for num in sequence:
        print(num)


var_length('Printing values', 20, 40, 60)
var_length('Printing values', 80, 100)
print('----------')


# Ex 3
def return_values(x, y):
    addition = x + y
    subtraction = x - y
    return addition, subtraction


result = return_values(40, 10)
print(result)  # result in a tuple


# no 2
def return_values2(x, y):
    return x + y, x - y


addition2, subtraction2 = return_values2(40, 10)
print(addition2, subtraction2)  # simple result
print('----------')


# Ex 4
def default_args(name, salary=9000):
    print('Employee name is', name, 'and', 'the salary is', salary)


default_args('John', 12000)
default_args('Jessy')
print('----------')


# Ex 5
def outer_func(a, b):
    division = a / b
    print(division)

    def inner_func(a, b):
        addition3 = a + b
        return addition3

    added = inner_func(a, b)
    return added + 5


result = outer_func(12, 12)
print(result)
print('----------')


# Ex 6
def recursive_func(no):
    if no:
        return no + recursive_func(no - 1)
    else:
        return 0


result2 = recursive_func(10)
print('The recursive result:', result2)
print('----------')


# Ex 7
def display_student(name, age):
    print(name, age)


display_student("Emma", 26)
showStudent = display_student  # assign a new name to func
showStudent('Emma', 26)
print('----------')


# Ex 8
def even_list():
    even = []
    for x in range(4, 29, 2):
        even.append(x)
        print('The list is:', even)  # takes a list ~ 13 times
    print('The final list is:', list(range(4, 30, 2)))  # takes ones


even_list()
print('----------')


# Ex 9
def largest_no():
    x = [4, 6, 8, 24, 12, 2]
    largest_num = max(x)
    print(largest_num)


largest_no()

print('----Till the end of the journey---- 😀')