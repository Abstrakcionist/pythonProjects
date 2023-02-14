def fibonacci_numbers(length):
    fibonacci_line = [1, 2]
    pointer = 1
    while fibonacci_line[-1] < length:
        fibonacci_line.append(fibonacci_line[pointer] + fibonacci_line[pointer - 1])
        pointer += 1
    return fibonacci_line[:-1]


def even_fibonacci_numbers(length):
    summ = 0
    fibonacci_line = fibonacci_numbers(length)
    for num in fibonacci_line:
        if num % 2 == 0:
            summ += num
    return summ


print((even_fibonacci_numbers(4000000)))
