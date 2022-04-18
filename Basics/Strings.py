import re
import string


# Ex 1a
def first_string():
    str1 = 'James'
    print('Original string is:', str1)
    first_char = str1[0]
    print(first_char)
    middle_char = str1[2]
    print(middle_char)
    last_char = str1[4]
    print(last_char)
    result = first_char + middle_char + last_char
    print('The result is:', result)


first_string()
print(' ----------')


# sol 2
def solution2():
    str1 = 'James'
    res = str1[0]
    l = len(str1)
    mi = int(l / 2)
    res = res + str1[mi]
    res = res + str1[l - 1]
    print("New result:", res)


solution2()
print('----------')


# Ex 1b
def middle_chars():
    str1 = 'JhonDipPeta'
    str2 = "JaSonAy"
    midd_length = len(str1)
    midd_length2 = len(str2)
    midd_index = int(midd_length / 2)
    midd_index2 = int(midd_length2 / 2)
    print(midd_index)
    print(midd_index2)
    midd_chars = str1[4:7]
    midd_chars2 = str2[2:5]
    print(midd_chars)
    print(midd_chars2)


middle_chars()
print('----------')


# sol 2 - much simpler
def get_middle_three_chars(str1):
    print("Original String is", str1)
    mi = int(len(str1) / 2)
    res = str1[mi - 1:mi + 2]
    print("Middle three chars are:", res)


get_middle_three_chars("JhonDipPeta")
get_middle_three_chars("JaSonAy")
print('----------')


# Ex 2
def append_midd_string():
    s1 = "Ault"
    s2 = "Kelly"
    a = len(s1)
    midd = int(a / 2)
    print(a, '', midd)
    result = s1[0:2] + s2 + s1[2:]
    print(result)


append_midd_string()
print('----------')


# sol 2: much broad
def append_middle(s1, s2):
    print("Original strings are:", s1, '&', s2)
    mi = int(len(s1) / 2)
    x = s1[:mi:]  # middle index of s1
    print(x)
    x = x + s2
    print(x)
    x = x + s1[mi:]
    print(x)
    print("After appending new string in middle:", x)


append_middle("Ault", "Kelly")
print('----------')


# Ex 3
def first_midd_last(s1, s2):
    middle_s1 = int(len(s1) / 2)
    middle_s2 = int(len(s2) / 2)
    x = s1[middle_s1]
    y = s2[middle_s2]
    print(x, y)
    res = s1[0] + s2[0] + x + y + s1[-1] + s2[-1]
    print(res)


first_midd_last('America', 'Japan')
print('----------')


# sol 2: much complex
def mix_string(s1, s2):
    first_char = s1[0] + s2[0]
    print(first_char)
    middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]
    print(middle_char)
    last_char = s1[len(s1) - 1] + s2[len(s2) - 1]
    print(last_char)
    res = first_char + middle_char + last_char
    print('The mixed string is:', res)


s1 = "America"
s2 = "Japan"
mix_string(s1, s2)
print('----------')


# Ex 4
def lowers_first():
    str1 = 'PyNaTive'
    lower = []
    upper = []
    for char in str1:
        if char.islower():
            lower.append(char)
        else:
            upper.append(char)

    sorted_str = ''.join(lower + upper)
    print('The result is:', sorted_str)


lowers_first()
print('----------')


# Ex 5
def count_all():
    str1 = "P@#yn26at^&i5ve"
    print('Total counts of chars, digits, and symbols')
    alphabets = digits = special = 0
    for y in range(len(str1)):
        if str1[y].isalpha():
            alphabets = alphabets + 1
        elif str1[y].isdigit():
            digits = digits + 1
        else:
            special = special + 1
    print('Chars =', alphabets)
    print('Digits =', digits)
    print('Symbol =', special)


count_all()
print('----------')


# Ex 6
def mixed_string():
    s1 = "Abc"
    s2 = "Xyz"
    s1_len = len(s1)
    s2_len = len(s2)
    length = s1_len if s1_len > s2_len else s2_len
    result = ''
    s2 = s2[::-1]  # reversed
    for i in range(length):
        if i < s1_len:  # ascending
            result = result + s1[i]
        if 1 < s2_len:  # descending
            result = result + s2[i]
    print('Mixed result:', result)


mixed_string()
print('----------')


# Ex 7
def balance_test(s1, s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag


s1 = "Yn"
s2 = "PYnative"
flag = balance_test(s1, s2)
print("s1 and s2 are balanced:", flag)

s1 = "Ynf"
s2 = "PYnative"
flag = balance_test(s1, s2)
print("s1 and s2 are balanced:", flag)

balance_test(s1, s2)
print('----------')


# Ex 8
def occurrences_substring():
    str1 = "Welcome to USA. usa awesome, isn't it?"
    sub_string = 'USA'
    converted_str = str1.lower()
    print(converted_str)  # converted all words to lower
    count = converted_str.count(sub_string.lower())  # count 'usa' in converted_str
    print(sub_string.lower())
    print("The USA count is:", count)


occurrences_substring()
print('----------')


# Ex 9
def sum_average_str():
    str1 = 'PYnative29@#8496'
    s = 0
    count = 0
    for x in range(len(str1)):
        if str1[x].isdigit():
            z = int(str1[x])
            s = s + z
            count = count + 1  # counts the digits = 6
            avg = s / count

    print('Sum is:', s)
    print('Average number is:', avg)


sum_average_str()
print('----------')


# sol 2
def sum_average_sol2():
    input_str = "PYnative29@#8496"
    digit_list = [int(num) for num in re.findall(r'\d', input_str)]  # list of digits
    print('Digits:', digit_list)
    total = sum(digit_list)
    avg = total / len(digit_list)
    print("Sum is:", total, "Average is ", avg)


sum_average_sol2()  # imported re - 'regex/regular expressions'
print('----------')


# Ex 10
def count_all_occurrences():
    str1 = "Apple"
    char_dict = dict()  # used a dict format
    for x in str1:
        count = str1.count(x)
        char_dict[x] = count
    print(char_dict)


count_all_occurrences()
print('----------')


# Ex 11
def reverse_string():
    str1 = "PYnative"
    str2 = str1[::-1]
    print('The original string is:', str1)
    print('The reversed string is:', str2)


reverse_string()
print('----------')


# sol 2
def reverse_string2():
    str1 = "PYnative"
    x = ''.join(reversed(str1))
    print('The second solution - reversed str - is:', x)


reverse_string2()
print('----------')


# Ex 12
def last_position_substring():
    str1 = "Emma is a data scientist who knows Python. Emma works at google."
    sub_str = 'Emma'
    y = str1.rindex(sub_str)  # or rfind() - does the same
    print('Last occurrence of Emma starts at index:', y)


last_position_substring()
print('----------')


# Ex 13
def split_hyphens():
    str1 = 'Emma-is-a-data-scientist'
    sub_str = str1.rsplit('-')  # or split()
    print(sub_str)
    print('Displaying each substring')
    for i in sub_str:
        print(i)


split_hyphens()
print('----------')


# Ex 14
def remove_empty_strs():
    str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
    print("Original list is : " + str(str_list))
    str_list2 = []
    for x in str_list:
        if x:
            str_list2.append(x)
    print(str_list2)
    print('After removing empty strings: ', str_list2)


remove_empty_strs()
print('----------')


# sol 2
def remove_empty_sol2():
    str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
    print("Original list is : " + str(str_list))
    str_list2 = list(filter(None, str_list))  # filter() - built-in f
    print('After removing empty strings: ', str_list2)


remove_empty_sol2()
print('----------')


# Ex 15
def remove_specials():
    str1 = "/*Jon is @developer & musician"
    print("Original string is: ", str1)
    str2 = str1.translate(str.maketrans('', '', string.punctuation))
    print("New string is: ", str2)


remove_specials()
print('----------')


# sol 2
def remove_specials2():
    str1 = "/*Jon is @developer & musician"
    print("Original string is ", str1)
    res = re.sub(r'[^\w\s]', '', str1)  # replace special symbols with ''
    print("New string is ", res)


remove_specials2()
print('----------')


# Ex 16
def remove_except_int():
    str1 = 'I am 25 years and 10 months old'
    digit_str = []
    for x in str1:
        if x.isdigit():
            digit_str.append(x)
    print(digit_str)
    new_digit_str = ''.join(digit_str)
    print(new_digit_str)


remove_except_int()
print('----------')


# Ex 17
def alpha_num_strs():
    str1 = "Emma25 is Data scientist50 and AI Expert"
    final_list = []
    my_list = str1.split()
    print(my_list)
    for x in my_list:
        if any(char.isalpha() for char in x) and any(char.isdigit() for char in x):
            final_list.append(x)
            print('Result:', x)
    print('Displaying words with alphabets and numbers:')
    for y in final_list:
        print(y)


alpha_num_strs()
print('----------')


# Ex 18
def replace_specials():
    str1 = '/*Jon is @developer & musician!!'
    print("Original string is: ", str1)
    res = re.sub(r'[^\w\s]', '#', str1)  # replace specials with regex
    print("New string is: ", res)


replace_specials()
print('----------')


# sol 2
def replace_specials2():
    str1 = '/*Jon is @developer & musician!!'
    print("The original string is : ", str1)
    replace_char = '#'
    for char in string.punctuation:
        str1 = str1.replace(char, replace_char)
    print("The strings after replacement : ", str1)


replace_specials2()
print('----Till the end of the journey---- 😀')