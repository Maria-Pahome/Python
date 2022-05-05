# Ex 1
import collections


def lists():
    l1 = [3, 6, 9, 12, 15, 18, 21]
    l2 = [4, 8, 12, 16, 20, 24, 28]
    odd_index = l1[1::2]
    print('Element at odd-index positions from list one:')
    print(odd_index)
    even_index = l2[0::2]
    print('Element at even-index positions from list two:')
    print(even_index)
    final_list = odd_index + even_index
    print('Printing Final third list:')
    print(final_list)


lists()
print('----------------')


# Ex 2
def remove_add_lists():
    list1 = [34, 54, 67, 89, 11, 43, 94]
    list1.remove(list1[4])
    print('List After removing element at index 4:', list1)
    list1.insert(2, 11)
    print('List after Adding element at index 2:', list1)
    list1.append(11)
    print('List after Adding element at last:', list1)


remove_add_lists()
print('----------------')


# Ex 3
def slice_chunks():
    sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
    chunk1 = slice(3)
    chunk2 = slice(3, 6, 1)
    chunk3 = slice(6, 9, 1)
    print('Chunk  1:', sample_list[chunk1])
    reversed1 = list(reversed(sample_list[chunk1]))
    print('After reversing it:', reversed1)

    print('Chunk  2:', sample_list[chunk2])
    reversed2 = list(reversed(sample_list[chunk2]))
    print('After reversing it:', reversed2)

    print('Chunk  3:', sample_list[chunk3])
    reversed3 = list(reversed(sample_list[chunk3]))
    print('After reversing it:', reversed3)


slice_chunks()
print('----------------')


# sol 2
def slice_chunks2():  # more used
    sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
    print("Original list ", sample_list)

    length = len(sample_list)
    chunk_size = int(length / 3)
    start = 0
    end = chunk_size

    # run loop 3 times
    for i in range(3):
        # get indexes
        indexes = slice(start, end)

        # get chunk
        list_chunk = sample_list[indexes]
        print("Chunk ", i, list_chunk)

        # reverse chunk
        print("After reversing it ", list(reversed(list_chunk)))

        start = end
        end += chunk_size


slice_chunks2()
print('----------------')


# Ex 4
def count_occurrences():
    sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
    occurrences = collections.Counter(sample_list)  # collections

    print('Printing count of each item:', occurrences)


count_occurrences()
print('----------------')


# sol 2
def count_occurrences2():
    sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
    count_num = dict()
    for x in sample_list:
        if x in count_num:
            count_num[x] = count_num[x] + 1  # count_num[x] += 1 - increments
        else:
            count_num[x] = 1
    print("Printing count of each item: ", count_num)


count_occurrences2()
print('----------------')


# Ex 5
def list_pairs():
    first_list = [2, 3, 4, 5, 6, 7, 8]
    second_list = [4, 9, 16, 25, 36, 49, 64]
    my_set = [(x, y) for x in first_list for y in second_list if x ** 2 == y]
    print('Result is:', set(my_set))


list_pairs()
print('----------------')


# sol 2
def list_pairs2():
    first_list = [2, 3, 4, 5, 6, 7, 8]
    second_list = [4, 9, 16, 25, 36, 49, 64]
    my_dict = set(zip(first_list, second_list))
    print(my_dict)


list_pairs2()
print('----------------')
