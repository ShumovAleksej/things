n = int(input())
ls = []
num = 0
play = True

while play:
    num = num + 1
    for i in range(1, num + 1):
        ls.append(num)
        if len(ls) == n:
            play = False
            break
for i in ls:
    print(i, end=' ')