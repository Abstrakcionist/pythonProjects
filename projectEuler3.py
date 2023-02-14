def simple_number(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def find_all_divisors(number):
    divisors = []
    for i in range(2, int(number ** 0.5)+1):
        divisor = number // i
        if number % i == 0:
            if divisor != number / divisor:
                divisors.append(divisor)
                divisors.append(number // divisor)
            else:
                divisors.append(divisor)
    divisors.sort()
    divisors.reverse()
    return divisors


def main(number):
    divisors = find_all_divisors(number)
    for i in range(len(divisors)):
        if simple_number(divisors[i]):
            return divisors[i]
    return f'ERROR'


print(main(600851475143))
