def find_max(input_string, n):
    maximum = 1
    current_value = 1
    for i in range(0, len(input_string) - 1):
        if input_string[i] == input_string[i + 1]:
            current_value += 1
            maximum = max(current_value, maximum)
        elif n !=0:
            for dop in range(n):
                
    return maximum


sub_number, beautiful_string = open('input.txt').readlines()
print(find_max(beautiful_string))