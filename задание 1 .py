def remove_duplicates(arr):
    return list(set(arr))

# Пример использования функции
original_array = [1, 2, 2, 3, 4, 4, 5, 5, 6]
print("Исходный массив:", original_array)

unique_array = remove_duplicates(original_array)
print("Массив без дубликатов:", unique_array)
