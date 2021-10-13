def modify_list(l):
    x = []
    for item in l:
        if item % 2 == 0:
            x.append(item // 2)
    l.clear()
    l.extend(x)

z = [1, 2, 3, 4, 5, 6]
modify_list(z)
print(z)