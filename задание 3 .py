def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return primes

# Задаем диапазон
start_range = 10
end_range = 50

# Находим простые числа в заданном диапазоне
prime_numbers = find_primes(start_range, end_range)

# Выводим список простых чисел
print(f"Простые числа в диапазоне от {start_range} до {end_range}:")
print(prime_numbers)
