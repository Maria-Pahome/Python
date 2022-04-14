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


# Ex5


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
