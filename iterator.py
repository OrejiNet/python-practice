def iterator(numbers: list[int]):

    if not numbers:
        return []

    # Initialize max and min with the first element of the list
    max_num = min_num = numbers[0]

    for value in numbers:
        if value > max_num:
            max_num = value
        if value < min_num:
            min_num = value

    return [max_num, min_num]

print(iterator([-1, 1, 2, 3, 4, 5]))