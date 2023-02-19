data1 = [1,2,3,4,5]
r, *s, t = data1
print(r)
print(s)
print(t)
print("\n")

data2 = [1,2]
a, b, *c = data2
print(a)
print(b)
print(c)
print("\n")

data3 = [1,2,3,4,5]
a, _, b, _, c = data3
print(a)
print(b)
print(c)
print(_)
print("\n")

x, *__, y = data3
print(x)
print(y)
print(__)
print("\n")