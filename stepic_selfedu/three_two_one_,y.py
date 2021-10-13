lst = [i for i in input().lower().split()]
st = set()
for item in lst:
    st.add(item)
for x in st:
    print(x, lst.count(x))
