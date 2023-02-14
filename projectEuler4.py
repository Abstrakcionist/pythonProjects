def is_palindrome(number):
    digit = str(number)
    digit_re = ''
    for i in range(len(digit)-1, 0, -1):
        digit_re += digit[i]
    if digit == digit_re:
        return True
    else:
        return False

print(is_palindrome(90009))
numbers = []
maximum = 0
for x in range(100, 1000):
    for y in range(100, 1000):
        result = x * y
        numbers.append(result)
        maximum = max(result, maximum)

print(maximum)

