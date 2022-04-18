# Ex 1
def reversed_list():
    list1 = [100, 200, 300, 400, 500]
    list1.reverse()  # or negative slicing [::-1]
    print(list1)


reversed_list()
print('-------------')


# Ex 2
def concatenated_lists():
    list1 = ["M", "na", "i", "Ke"]
    list2 = ["y", "me", "s", "lly"]
    y = list(zip(list1, list2))
    print(y)
    new_list = [x + w for x, w in y]
    print(new_list)


concatenated_lists()
print('-------------')


# Ex 3
def squares_list():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    new_list = [x ** 2 for x in numbers]
    print('Squares:', new_list)


squares_list()
print('-------------')


# Ex 4
def concatenate_list():
    list1 = ["Hello ", "take "]
    list2 = ["Dear", "Sir"]
    concatenated_lst = list(list1 + list2)
    print('Elements are added:', concatenated_lst)
    new_lst = [x + y for x in list1 for y in list2]
    print('Solution 2:', new_lst)


concatenate_list()
print('-------------')


# Ex 5
def iterate_list():
    list1 = [10, 20, 30, 40]
    list2 = [100, 200, 300, 400]
    list2.reverse()
    print('Reversed list: ', list2)
    print('The final results:')
    for (a, b) in zip(list1, list2):
        print(a, b)


iterate_list()
print('-------------')


# Ex 6
def remove_empty_strs():
    list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
    list2 = list(filter(None, list1))
    print('The new list:', list2)


remove_empty_strs()
print('-------------')


# Ex 7
def add_new_item():
    list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    list2 = list1[2][2]
    print('The list of list2[2][2]:', list2)
    list1[2][2].append(7000)
    print('Result:', list1)


add_new_item()
print('-------------')


# Ex 8
def added_nested_lst():
    list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
    # sub list to add
    sub_list = ["h", "i", "j"]
    list2 = list1[2][1][2]
    print('The list of list1[2][1][2]:', list2)
    list1[2][1][2].extend(sub_list)
    print('Expected result:', list1)
    print("\N{winking face}")
    list1[2][1][2].append(sub_list)  # attach the entire lst to position
    print('Appended list:', list1)
    list1[2][1][2].extend(sub_list)  # extends just the el at the end, not the list
    print('Extended list:', list1)


added_nested_lst()
print('-------------')


# Ex 9
def new_value():
    list1 = [5, 10, 15, 20, 25, 50, 20]
    print('The index of 20:', list1.index(20))
    list1[3] = 200
    print('New replaced list:', list1)


new_value()
print('-------------')


# Ex 10
def remove_occurrences():
    list1 = [5, 20, 15, 20, 25, 50, 20]
    count = list1.count(20)
    print('Number 20 appears:', count, 'times.')

    new_list = [x for x in list1 if x != 20]
    print('Happy new list:', new_list)

    print("\N{winking face}", '#1')
    while 20 in list1:
        list1.remove(20)
    print('Solution #1:', list1)

    print("\N{winking face}", '#2')

    def remove_value(sample_lst, value):
        return [x for x in sample_lst if x != value]

    expected_res = remove_value(list1, 20)
    print('Solution #2:', expected_res)


remove_occurrences()

print('----Till the end of the journey---- 😀')
