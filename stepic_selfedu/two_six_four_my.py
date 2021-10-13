# ls = [ [int(i) for i in input().split()] for j in range(0, 3)]
ls = []
x = ''
while True:
    ls_x = []
    x = input()
    if x == 'end':
        break
    else:
        for i in x.split():
            ls_x.append(int(i))
    ls.append(ls_x)
# ls = [[9, 5, 3],
#       [0, 7, -1],
#       [-5, 2, 9],
#       ]

ls_n1 = []
for i in range(0, len(ls)):
    ls_n2 = []
    for j in range(0, len(ls[0])):
        sum = 0

        # i-1, j
        sum += ls[i - 1][j]

        # i+1, j
        if i == len(ls) - 1:
            kor = 0
        else:
            kor = i + 1
        sum += ls[kor][j]

        # i, j-1
        sum += ls[i][j - 1]

        # i, j+1
        if j == len(ls[0]) - 1:
            kor = 0
        else:
            kor = j + 1
        sum += ls[i][kor]

        ls_n2.append(sum)
    ls_n1.append(ls_n2)
# ls[i-1][j] + ls[i+1][j] + ls[i][j-1] + ls[i][j+1]
print(ls_n1)

for item in ls_n1:
    for i in item:
        print(i, end=' ')
    print()