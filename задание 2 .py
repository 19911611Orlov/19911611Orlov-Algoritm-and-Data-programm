def remove_element(arr, element_to_remove):
    return [x for x in arr if x != element_to_remove]

# Пример использования функции
nums = [1, 3, 5, 2, 3, 4, 5, 3, 6]
element = 3  # Элемент для удаления

print("Исходный список:", nums)
nums = remove_element(nums, element)
print(f"Список после удаления элемента {element}:", nums)
