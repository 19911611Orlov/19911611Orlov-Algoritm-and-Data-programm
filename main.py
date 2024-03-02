def remove_duplicates(arr):
    # Создание пустого списка для уникальных элементов
    unique_list = []

    # Итерация по каждому элементу в исходном массиве
    for i in arr:
        # Если элемент еще не встречался, добавляем его в unique_list
        if i not in unique_list:
            unique_list.append(i)

    return unique_list

# Пример использования функции
input_array = [1, 2, 2, 3, 4, 4, 5, 5, 5]
result = remove_duplicates(input_array)
print("Массив без дубликатов:", result)
