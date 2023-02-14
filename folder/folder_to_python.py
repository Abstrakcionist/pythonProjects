import os


def add_text(file_name: str):
    a = open(file_name)
    text = ''
    for i in a:
        text += str(i)
    return text


file_list = os.listdir()[1:]
files_text = []

for file in file_list:
    files_text.append(add_text(file))


print(files_text)
