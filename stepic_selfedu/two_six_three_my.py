ls, x = input().split(), int(input())
ls_index = []
sch = 0
if ls.count(str(x)) == 0:
    print('Отсутствует')
else:
    for i in ls:
        if int(i) == x:
            print(ls.index(i, sch), end=' ')
        sch += 1
