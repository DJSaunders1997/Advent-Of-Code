# https://adventofcode.com/2022/day/1
from input import elves_list

# Define Helper Functions
def spliter(value, array):
    # Splitter function taken and (barely) modified from https://stackoverflow.com/a/45190116

    res = []
    while value in array:
        index = array.index(value)
        # removed +1 as we don't want None in our list
        res.append(array[:index])
        array = array[index + 1:]
    if array:
        # Append last elements
        res.append(array)
    return res


def max_val_and_index(nested_list):
    # Given a list of lists of ints, calculate the sum of all values in each element.
    # Return the maximum total, and its index.

    res = []
    for list_of_nums in nested_list:
        res.append(sum(list_of_nums))

    max_val = max(res)
    max_val_index = res.index(max_val)

    return(max_val, max_val_index)


split_elves_list = spliter(None, elves_list)

max_val, max_val_index = max_val_and_index(split_elves_list)

print(
    f"""
The elf carrying the most calories is elf number {max_val_index+1}.
They're carrying {max_val} calories worth of food.
"""
)

# Part 2

# modify max_val_and_index


def sort_nested_list(nested_list):
    # Given a list of lists of ints, calculate the sum of all values in each element.
    # Return the maximum total, and its index.

    res = []
    for list_of_nums in nested_list:
        res.append(sum(list_of_nums))

    max_val = max(res)
    max_val_index = res.index(max_val)

    return(sorted(res, reverse=True))


list_sum = sort_nested_list(split_elves_list)
list_sum_indexes = range(len(list_sum))

sum_top_3 = sum(sorted(list_sum[:3]))

print(
    f"""
The sum of the top 3 elves calories is {sum_top_3}.
"""
)
