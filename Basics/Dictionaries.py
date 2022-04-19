from pprint import pprint


# Ex 1
def converted_lists():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    zipped = dict(zip(keys, values))
    print('Expected result #1:', zipped)


converted_lists()
print('-------------')


# sol 2
def converted_lists2():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    resulted_dict = dict()
    for x in range(len(keys)):
        resulted_dict.update({keys[x]: values[x]})  # update() - updates specific key:value
    print('Expected result #2:', resulted_dict)


converted_lists2()
print('-------------')


# Ex 2
def merged_dicts():
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    dict1.update(dict2)
    print('Merged dictionary:', dict1)


merged_dicts()
print('-------------')


# Ex 3
def specific_value():
    sampleDict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }
    print('Key times:', len(sampleDict))
    print('Expected value:', sampleDict["class"]["student"]["marks"]["history"])


specific_value()
print('-------------')


# Ex 4
def default_values():
    employees = ['Kelly', 'Emma']
    defaults = {"designation": 'Developer', "salary": 8000}
    new_dict = dict.fromkeys(employees, defaults)
    print('Expected result:', new_dict)
    print('The data for Kelly:', new_dict["Kelly"])
    print('The data for Emma:', new_dict["Emma"])


default_values()
print('-------------')


# Ex 5
def extracted_keys():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"}
    keys = ["name", "salary"]
    new_dict = {k: sample_dict[k] for k in keys}  # dict comprehension
    print('Resulted dict #1:', new_dict)


extracted_keys()
print('-------------')


# sol 2
def extracted_keys2():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"}
    keys = ["name", "salary"]
    result = dict()
    for k in keys:
        result.update({k: sample_dict[k]})
    print('Resulted dict #2:', result)


extracted_keys2()
print('-------------')


# Ex 6
def delete_keys():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }
    # Keys to remove
    keys = ["name", "salary"]

    del sample_dict["name"]
    del sample_dict["salary"]
    print("Solution #1:", sample_dict)

    # for k in keys:
    #     sample_dict.pop(k)
    # print('Solution #2:', sample_dict)

    # sample_dict = {k: sample_dict[k] for k in sample_dict.keys() - keys}
    # print('Solution #3:', sample_dict)


delete_keys()
print('-------------')


# Ex 7
def check_value():
    sample_dict = {'a': 100, 'b': 200, 'c': 300}
    x = sample_dict.get('b')
    print(x, 'present in a dict')


check_value()
print('-------------')


# sol 2
def check_value2():
    sample_dict = {'a': 100, 'b': 200, 'c': 300}
    x = sample_dict.values()
    print('Dict is a list:', x)
    if 200 in x:
        print(200, 'present in a dict')


check_value2()
print('-------------')


# Ex 8
def rename_key():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New York"
    }
    sample_dict['location'] = sample_dict['city']
    print('Added key:', sample_dict)
    del sample_dict['city']
    print('Updated dictionary:', sample_dict)


rename_key()
print('-------------')


# Ex 9
def key_min_value():
    sample_dict = {
        'Physics': 82,
        'Math': 65,
        'history': 75
    }
    lower_value = min(sample_dict, key=sample_dict.get)  # min() & max() - built-in fs
    print('Lowest value in dict:', lower_value)


key_min_value()
print('-------------')


# Ex 10
def change_nested_dict():
    sample_dict = {
        'emp1': {'name': 'John', 'salary': 7500},
        'emp2': {'name': 'Emma', 'salary': 8000},
        'emp3': {'name': 'Brad', 'salary': 500}  # 8500
    }
    sample_dict['emp3']['salary'] = 8500
    print('The changed key:', sample_dict['emp3'])
    print('New dictionary value:')
    pprint(sample_dict)


change_nested_dict()
print('----Till the end of the journey---- 😀')
