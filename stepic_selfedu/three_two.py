def f(x):
    x += 1
    return x
lst = []
dictionary = dict()
for i in range(int(input())):
    num = int(input())
    if num not in dictionary:
        dictionary[num] = f(num)
    lst.append(dictionary[num])
for i in lst:
    print(i)
# best
# n=int(input())
# d={}
# for i in range(n):
#     x=int(input())
#     if x not in d:
#         d[x]=f(x)
#     print(d[x])