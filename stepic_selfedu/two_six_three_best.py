l = [int(i) for i in input().split()]
x = int(input())
if not x in l:
    print('Отсутствует')
else:
    for i in range(len(l)):
        if l[i] == x: print(i, end=' ')
