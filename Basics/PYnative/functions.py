# 1: Write a program to create a function that takes two arguments, name and age, and print their value.
def my_func(name, age):
    print(f"My name is {name}")
    print(f"My age is {age}")


my_func("Maria", "24")


# 2: Write a program to create function func1() to accept a variable length of arguments and print their value.
# Create a function in such a way that we can pass any number of arguments
# to this function and the function should process them and display each argument’s value.
def func1(*numbers):
    total = 0
    for no in numbers:
        print(no)


# 0 arguments
func1(3)

# 5 arguments
func1(10, 5, 2, 5, 4)

# 3 arguments
func1(78, 7, 2.5)


# 3: Write a program to create function calculation() such that
# it can accept two variables and calculate addition and subtraction.
# Also, it must return both addition and subtraction in a single return call.
# a
def calculation(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction


# get result in tuple format
res = calculation(70, 10)
print(res)


# b
def calculation(a, b):
    return a + b, a - b


# get result in tuple format
# unpack tuple
add, sub = calculation(40, 10)
print(add, sub)


# 4:Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary
def show_employee(name, salary="9000"):
    print(f"Name: {name} salary: {salary} ")


show_employee("Ben", 12000)
show_employee("Jessa")


# 5:Create an inner function to calculate the addition in the following way:
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it
# outer function
def outer_func(a, b):
    square = a ** 2

    # inner function
    def addition(a, b):
        return a + b

    # call inner function from outer function
    add1 = addition(a, b)
    # add 5 to the result
    return add1 + 5


result = outer_func(90, 10)
print(result)

# 6:Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
# A recursive function is a function that calls itself, again and again.




# 1:
# 1:
# 1:
# 1:
