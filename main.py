COUNT_COMPARED = 0
COUNT_MOVED = 0


def find_smallest_index(numbers):
    global COUNT_COMPARED

    smallest_value = numbers[0]
    index = 0
    for i in range(1, len(numbers) - 1):
        if numbers[i] < smallest_value:
            index = i
            break
        index = 0

        COUNT_COMPARED += 1

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


if __name__ == '__main__':
    ba = [1, 4, 7, 8, 11, 3, 15, 16, 17]
    bb = [22, 25, 45, 3, 1, 8, 15, 19, 22]
    bc = [99, 74, 55, 12, 65, 98, 8, 11, 23]
    bd = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    print(selection_sort(ba))