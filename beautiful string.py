sub_number, beautiful_string = open('input.txt').readlines()


def find_max(input_string):
    maximum = 1
    current_value = 1
    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            current_value += 1
            maximum = max(current_value, maximum)
        else:
            current_value = 1
    return maximum


print(find_max(beautiful_string))
