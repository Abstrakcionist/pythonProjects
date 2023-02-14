def sum_nums_div_3_or_5(x):
    count = 0
    for i in range(x):
        if i % 5 == 0 or i % 3 == 0:
            count += i

    return count


print(sum_nums_div_3_or_5(1000))
