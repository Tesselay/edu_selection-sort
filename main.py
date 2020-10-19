COUNT_SEARCHED = 0
COUNT_MOVED = 0


def find_smallest_index(numbers):
    smallest_value = numbers[0]
    index = -1          # '-1' to target var left when the last value has to be selected
    for i in range(1, len(numbers) - 1):
        print(i)
        if numbers[i] < smallest_value:
            smallest_value = numbers[i]
            index = i

    return index


def selection_sort(numbers):
    sorted_numbers = []
    numbers_length = len(numbers)

    for i in range(numbers_length):
        global COUNT_SEARCHED
        global COUNT_MOVED
        COUNT_SEARCHED += 1
        COUNT_MOVED += 1
        index_s_number = find_smallest_index(numbers)
        sorted_numbers.append(numbers.pop(index_s_number))

    return sorted_numbers


if __name__ == '__main__':
    ba = [1, 4, 7, 8, 11, 3, 15, 16, 17]
    bb = [22, 25, 45, 3, 1, 8, 15, 19, 22]
    bc = [99, 74, 55, 12, 65, 98, 8, 11, 23]
    bd = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    print(selection_sort(bd))