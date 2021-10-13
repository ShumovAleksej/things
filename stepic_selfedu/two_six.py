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

ls_n1=[]
for i in range(0, len(ls)):
    ls_n2 = []
    for j in range(0, len(ls[0])):
        x = ls[i-1][j]
        y = ls[i+1][j]
        ls_n2.append(x + y)
    ls_n1.append(ls_n2)
# ls[i-1][j] + ls[i+1][j] + ls[i][j-1] + ls[i][j+1]
print(ls_n1)