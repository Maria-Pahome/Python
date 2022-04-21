# Ex 1
print("Ex 1")
count = 1
while count <= 10:
    print(count)
    count = count + 1

print('---------------------------')

# Ex 2
print("Ex 2")


def pattern_nr():
    rows = 5
    for i in range(1, rows + 1, 1):
        for j in range(1, i + 1):
            print(j, '', end='')
        print('')


pattern_nr()

print('---------------------------')

# Ex 3
print("Ex 3")


def sum_numbers():
    n = int(input('Enter a number:'))
    s = 0
    for nr in range(1, n + 1, 1):
        s = s + nr
    print('Sum is ', s)


sum_numbers()
print('---------------------------')

# Ex 4
print("Ex 4")


def multiplication_table():
    for i in range(1, 11):
        num = i * 2
        print(num)


multiplication_table()

print('---------------------------')

# Ex 5
print("Ex 5")


def display_nr():
    numbers = [12, 75, 150, 180, 145, 525, 50]
    for i in numbers:
        if i > 500:
            break
        elif i > 150:
            continue
        elif i % 5 == 0:
            print(i)


display_nr()

print('---------------------------')

# Ex 6
print("Ex 6")


def total_numbers():
    number = int(input("Enter a number:"))
    counter = 0
    while number != 0:
        number = number // 10
        counter += 1
    print("Total digits are ", counter)


total_numbers()

print('---------------------------')

# Ex 7
print("Ex 7")


def reversed_nr_pattern():
    rows = 5
    k = 5
    for i in range(0, rows + 1):
        for j in range(k - i, 0, -1):
            print(j, '', end=' ')
        print('')


reversed_nr_pattern()
print('---------------------------')

# Ex 8
print("Ex 8")


def reversed_order(list1):
    new_list = list1[::-1]
    return new_list


list1 = [10, 20, 30, 40, 50]
print(reversed_order(list1))

print('---------------------------')

# Ex 9
print("Ex 9")


def negative_nrs():
    for i in range(-10, 0, +1):
        print(i)


negative_nrs()

print('---------------------------')

# Ex 10
print("Ex 10")


def else_block():
    for i in range(0, 5, 1):
        print(i)
    else:
        print('Done!')


else_block()

print('---------------------------')

# Ex 11
print("Ex 11")


def prime_numbers():
    start = 25
    end = 50
    print('Prime numbers between', start, 'and', end, 'are:')

    for i in range(start, end + 1):
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                print(i)


prime_numbers()

print('---------------------------')

# Ex 12
print("Ex 12")


def fibonacci_series():
    num1 = 0
    num2 = 1
    print('Fibonacci sequence:')
    for i in range(20):
        print(num1, '', end='')
        result = num1 + num2
        num1 = num2
        num2 = result


fibonacci_series()

print('---------------------------')

# Ex 13
print("Ex 13")

print('----Till the end of the journey---- 😀')

def factorial_number():
    num = 5
    factorial = 1
    if num < 0:
        print('Factorial does not exist for negative numbers.')
    elif num == 0:
        print('The factorial of 0 is 1')
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
    print('The factorial of', num, 'is', factorial, '.')


factorial_number()
print('---------------------------')

# Ex 14
print("Ex 14")


def reversed_integer():
    nr = int(input('Enter a number: '))
    reversed_nr = 0
    while nr > 0:
        reminder = nr % 10
        reversed_nr = (reversed_nr * 10) + reminder
        nr = nr // 10
    print("Reversed number is ", reversed_nr)


reversed_integer()

print('---------------------------')

# Ex 15
print("Ex 15")


def odd_index():
    my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for i in my_list[1::2]:
        print(i, end=" ")


#     resulted_list = []
#     for index in range(1, len(my_list), 2):
#         print(my_list[index])
#         resulted_list.append(my_list[index])
#     return resulted_list
#     print(odd_index([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])) # parameter: my_list
odd_index()
print('---------------------------')

# Ex 16
print("Ex 16")


def cube():
    input_number = 10
    for nr in range(1, input_number + 1):
        print("Current number is: ", nr, "and the cube is ", (nr * nr * nr))


cube()

print('---------------------------')

# Ex 17
print("Ex 17")


def sum_series():
    n = 8
    x = 6
    new_sum = 0
    for i in range(0, n):
        print(x, '', end='')
        new_sum = new_sum + x
        x = x * 10 + 6
    print('The sum of the series is ', new_sum)


sum_series()
print('---------------------------')

# Ex 18
print("Ex 18")


def triangle_star():
    rows = 5
    for x in range(1, rows + 1):
        for y in range(1, x + 1):
            print('* ', end='')
        print('')
    for e in range(rows - 1, 0, -1):
        for i in range(1, e + 1):
            print('* ', end='')
        print('')


triangle_star()
