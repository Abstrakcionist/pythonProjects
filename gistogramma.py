def split_string(input_string):
    symbols = []
    for i in input_string:
        if (i != ' ') and (i not in symbols):
            symbols.append(i)
    symbols.sort()
    return symbols


def symbols_counter(input_string, arr):
    dict = {}
    maximum = 0
    for i in arr:
        a = input_string.count(i)
        maximum = max(a, maximum)
        dict[i] = a
    return dict.values(), maximum


def do_horizontal(dict, maximum):
    arr =[]
    for i in dict:
        arr.append((['#'] * i) + ([' '] * (maximum - i)))
    return arr


def do_vertical(mlist, symbols):
    mlist = list(zip(*mlist))
    symbols_str = ''
    for i in reversed(mlist):
        print(''.join(i))
    for i in symbols:
        symbols_str += i
    return symbols_str


fin = open('input.txt', 'r')
a = [line.strip() for line in fin.readlines()]
input_string = ''
for i in a:
    input_string += i
symbols = split_string(input_string)
dict, maximum = symbols_counter(input_string, symbols)
arr = do_horizontal(dict, maximum)
gistogramma = do_vertical(arr, symbols)
print(gistogramma)

