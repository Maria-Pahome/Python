# Ex 1
def multiplied_sum(number1, number2):
    multiply = number1 * number2
    if multiply >= 1000:
        return multiply
    else:
        return number1 + number2


# 1st
if __name__ == '__main__':
    result = multiplied_sum(20, 30)
    print("The result is", result)
# 2nd
if __name__ == '__main__':
    result = multiplied_sum(40, 30)
    print("The result is", result)

# Ex 2
previous_number = 0
print("Printing current and previous sum in a range(10)")
for i in range(1, 11):
    x_sum = previous_number + i
    print(x_sum)
    print("Current Number is", i, "Previous Number is", previous_number, "Sum: ", x_sum)
    previous_number = i

for e in range(0, 10, 2):
    new_result = e ** e
    print(new_result)

# Ex 3
user_string = input("Enter word: ")
print("Original string is ", user_string)
length = len(user_string)
print("Printing only the even index chars:")
for i in range(0, length - 1, 2):
    print("index[", i, "]", user_string[i])

# solution no 2
x = list(user_string)
for i in x[0::2]:
    print(i)


# Ex 4
def remove_chars(words, n):
    print("Original sting:", words)
    removed = words[n:]
    return removed


print("Removing characters from a string")
print(remove_chars("George", 3))
print(remove_chars("George", 4))


# Ex 5

def first_last_same(nrList):
    print("Given list:", nrList)
    first_nr = nrList[0]
    last_nr = nrList[-1]
    if first_nr == last_nr:
        return True
    else:
        return False


nr_x = [10, 20, 30, 40, 10]
print("The result is", first_last_same(nr_x))
nr_y = [75, 65, 35, 75, 30]
print("The result is", first_last_same(nr_y))


# Ex 6
def divide_nr():
    newList = [10, 20, 33, 46, 55]
    print("Given list is:", newList)
    print("Divisible by 2:")
    for nr in newList:
        if nr % 2 == 0:
            print(nr)
        else:
            print("Incorrect!")


divide_nr()

# Ex 7
str_7 = "Emma is good developer. Emma is a writer."
sub_string = "Emma"
count = str_7.count(sub_string)
print(f"Emma appeared {count} times.")

# Ex 8
rows = 6
for i in range(rows):
    for x in range(i):
        print(i, end='')
    print('')


# Ex 9
def reversed_function(number):
    print('Original number: ', number)
    original_nr = number

    # reverse
    reversed_num = 0
    while number > 0:
        reminder = number % 10
        reversed_num = (reversed_num * 10) + reminder
        number = number // 10

    # check the nr
    if original_nr == reversed_num:
        print('Yes. The given number is palindrome.')
    else:
        print('No. The given number is not palindrome.')


reversed_function(132)
reversed_function(131)


# Ex 10

def merged_list(list1, list2):
    result_list = []

    for nr in list1:
        if nr % 2 != 0:
            result_list.append(nr)
    for nr in list2:
        if nr % 2 == 0:
            result_list.append(nr)

    return result_list


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print('result list: ', merged_list(list1, list2))


# Ex 11
def digit_reversed():
    number = int(input("Enter the number:"))
    print('Given number is ', number)
    while number > 0:
        digit = number % 10
        number = number // 10
        print(digit, end='')


digit_reversed()


# Ex 12
def income_tax():
    income = int(input('What is the taxable sum? '))
    tax_payable = 0
    print("Given income", income)

    if income <= 10000:
        tax_payable = 0
    elif income <= 20000:
        x = income - 10000
        tax_payable = x * 10 / 100
    else:
        tax_payable = 0
        tax_payable = 10000 * 10 / 100
        tax_payable += (income - 20000) * 20 / 100
    print("Total tax to pay is", tax_payable)


income_tax()


# Ex 13
def multiplication_table():
    for i in range(1, 11):
        for e in range(1, 11):
            print(i * e, '', end='')
        print()


multiplication_table()


# Ex 14 (print patterns)
# Pyramid pattern of stars in python
def star_half():
    rows9 = 7
    for j in range(1, rows9 + 1):
        for e in range(1, j + 1):
            print('*', '', end='')
        print()


def right_triangle():
    rows8 = 5
    k = 2 * rows - 2
    for y in range(0, rows8):
        for i in range(0, k):
            print(end='')
        k = k - 2
        for i in range(0, y + 1):
            print('* ', end='')
        print('')


def half_pyramid_star():
    rows7 = 9
    for i in range(rows7+ 1, 0, -1):
        for j in range(0, i - 1):
            print('* ', end=' ')
        print(" ")


def full_pyramid_star():
    rows6 = 5
    k = 2 * rows6 - 2
    for i in range(rows6, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("*", end=" ")
        print("")


def right_down_mirror():
    rows5 = 10
    i = rows5
    while i >= 1:
        j = rows5
        while j > i:
            print(' ', end=' ')
            j -= 1
        k = 1
        while k <= i:
            print('*', end=' ')
            k += 1
        print()
        i -= 1


def number_pattern():
    rows4 = int(input("Enter the number of rows: "))
    for x in range(rows4):
        for y in range(x):
            print(x, '', end='')
        print()


def number_half_pyramid():
    rows3 = int(input("Enter the number of rows: "))
    for t in range(rows3 + 1):
        for r in range(1, t + 1):
            print(r, '', end='')
        print()


def inverted_pyramid_nr():
    rows2 = int(input("Enter the number of rows: "))
    a = 0
    for u in range(rows2, 0, -1):
        a += 1
        for i in range(1, u + 1):
            print(a, '', end='')
        print()


def inverted_pyramid_same_digit():
    rows1 = 8
    digit = rows
    for a in range(rows1, 0, -1):
        for b in range(0, a):
            print(digit, '', end='')
        print('\r')


if __name__ == '__main__':
    star_half()
    right_triangle()
    half_pyramid_star()
    full_pyramid_star()
    right_down_mirror()
    number_pattern()
    number_half_pyramid()
    inverted_pyramid_nr()
    inverted_pyramid_same_digit()


# Ex 15
def exponent(base, exp):
    nr = exp
    result1 = 1
    while nr > 0:
        result1 = result1 * base
        nr = nr - 1
    print(base, "raises to the power of", exp, "is: ", result1)


exponent(5, 4)
exponent(2, 5)
