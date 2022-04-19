# Ex 1
def add_els_set():
    sample_set = {"Yellow", "Orange", "Black"}
    sample_list = ["Blue", "Green", "Red"]
    sample_set.update(sample_list)
    print(sample_set)


add_els_set()
print('---------------------')


# Ex 2
def identical_items():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    set3 = set1.intersection(set2)
    print('Intersection between sets:', set3)


identical_items()
print('---------------------')


# ex 3
def unique_items():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    set3 = set1.difference(set2)
    print('Different from set2:', set3)
    set4 = set2.difference(set1)
    print('Different from set1:', set4)
    set5 = set1.union(set2)
    print('United set:', set5)


unique_items()
print('---------------------')


# ex 4
def update_set():
    set1 = {10, 20, 30}
    set2 = {20, 40, 50}
    set1 = set1.difference(set2)
    print('New set1:', set1)


update_set()
print('---------------------')


# ex 5
def remove_items():
    set1 = {10, 20, 30, 40, 50}
    to_delete = {10, 20, 30}
    set1.difference_update(to_delete)
    print('New set:', set1)


remove_items()
print('---------------------')


# ex 6
def returns():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    new_set = set(set2.symmetric_difference(set1))  # diff in a or b, but not both
    print('New set:', new_set)


returns()
print('---------------------')


# ex 7
def common_els():
    set1 = {10, 20, 30, 40, 50}
    set2 = {60, 70, 80, 90, 10}
    if set1.isdisjoint(set2):
        print("Two sets have no items in common")
    else:
        print("Two sets have items in common:")
        print(set1.intersection(set2))


common_els()
print('---------------------')


# ex 8
def update_set1():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    set1.symmetric_difference_update(set2)
    print(set1)


update_set1()
print('---------------------')


# ex 9
def remove_items_sets():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    set3 = set(set1.intersection(set2))
    print('Intersection:', set3)
    to_delete = {10, 20}
    set1.difference_update(to_delete)
    print('New set1:', set1)


remove_items_sets()
print('---------------------')


# sol 2
def remove_items_sets2():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    set1.intersection_update(set2)
    print('New set1:', set1)


remove_items_sets2()
print('----Till the end of the journey---- 😀')
