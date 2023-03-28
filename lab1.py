from typing import List


print('\n\n-------------part 1-------------')
def six_is_first_or_last(list):
    if list[0] == 6 or list[-1] == 6:
        return True
    else: 
        return False


print(six_is_first_or_last([6, 1, 10, 5]))
print(six_is_first_or_last([2, 1, 10, 6]))
print(six_is_first_or_last([2, 1, 10, 1]))

print('\n\n-------------part 2-------------')
def merge_dicts(dict1, dict2):
    result = dict1.copy()  # створюємо копію першого словника
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result


dict1 = {'a': 200, 'b': 50}
dict2 = {'a': 100, 'c': 500}
merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)

print('\n\n-------------part 3-------------')
def generate_list(num):
    return [i for i in range(num+1)]


my_list = generate_list(5)
print(my_list)

print('\n\n-------------part 4-------------')
def count_matching_pairs(s1, s2):
    matching_pairs = set()
    for i in range(len(s1)-1):
        pair = s1[i:i+2]
        if pair in s2:
            matching_pairs.add(pair)
    return len(matching_pairs)

s1 = "xadasw"
s2 = "xad"
matching_pairs = count_matching_pairs(s1, s2)
print(matching_pairs)  # 2

print('\n\n-------------part 5-------------')
def get_events_by_date(events_dict, date):
    if date not in events_dict:
        return []
    else:
        return events_dict[date]


events_dict = {
    '2023-03-28': ['Meeting with clients', 'Lunch with coworkers'],
    '2023-03-29': ['Product demo', 'Team meeting'],
    '2023-03-30': ['Design review', 'Code review'],
}

events_on_2023_03_28 = get_events_by_date(events_dict, '2023-03-28')
print(events_on_2023_03_28)  # ['Meeting with clients', 'Lunch with coworkers']
