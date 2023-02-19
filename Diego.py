'''count_diego_marks, diego_marks, guests, guests_marks = open('input.txt').readlines()'''
a = open('input.txt')
all = []
for i in a:
    all.append(readline(i))
count_diego_marks = all[0][:-2]
diego_marks = []
guests = 0
guests_marks = []


print(count_diego_marks)