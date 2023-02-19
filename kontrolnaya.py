def variant(r, p, v):
    place_number = (r - 1) * 2 + p
    if place_number <= v:
        return place_number
    elif place_number % v == 0:
        return v
    else:
        return place_number % v


students, variants, row, place = map(int, open('input.txt').readlines())
petya = variant(row, place, variants)
desks = students // 2
arr = []
if (students // variants) >= 2:
    for desk in range(1, desks + 1):
        for lr in range(1, 3):
            if (desk != row) and (variant(desk, lr, variants) == petya):
                arr.append([desk, lr])
    print(arr[0][0], arr[0][1])
else:
    print(-1)
