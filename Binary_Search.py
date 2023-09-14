def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # Начальные границы интервала поиска

    while left <= right:
        mid = (left + right) // 2  # Средний индекс

        if arr[mid] == target:  # Если средний элемент равен цели, возвращаем индекс
            return mid
        elif arr[mid] < target:  # Если средний элемент меньше цели, сужаем интервал справа
            left = mid + 1
        else:  # Иначе сужаем интервал слева
            right = mid - 1

    return -1  # Если элемент не найден


# Пример использования:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_element = 5
result = binary_search(my_list, target_element)

if result != -1:
    print(f"Элемент {target_element} найден по индексу {result}.")
else:
    print(f"Элемент {target_element} не найден.")