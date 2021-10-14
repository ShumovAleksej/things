strng = input()
x, y = '', ''
num = 1
for i in range(0, len(strng)):
    if strng[i] == x:
        num += 1
    else:
        x = strng[i]
        if i != 0:
            y += str(num)
            num = 1
        y += strng[i]
    if i == len(strng) - 1:
        y += str(num)
print(y)
