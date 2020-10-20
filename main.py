COUNT_COMPARED = 0
COUNT_MOVED = 0


def find_smallest_index(numbers):
    global COUNT_COMPARED

    smallest_value = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < smallest_value:
            smallest_value = numbers[i]
        COUNT_COMPARED += 1

    index = numbers.index(smallest_value)

    return index


def selection_sort(numbers):
    sorted_numbers = []
    numbers_length = len(numbers)

    for i in range(numbers_length):
        global COUNT_MOVED

        index_s_number = find_smallest_index(numbers)
        sorted_numbers.append(numbers.pop(index_s_number))
        COUNT_MOVED += 1

    global COUNT_COMPARED
    print("Numbers compared: {}".format(COUNT_COMPARED))
    print("Numbers switched: {}".format(COUNT_MOVED))

    # Count variables are reset, to avoid counting multiple runs
    COUNT_COMPARED = 0
    COUNT_MOVED = 0

    return sorted_numbers
