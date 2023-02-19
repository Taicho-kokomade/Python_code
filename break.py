sum = 0
for i in range(1, 101):
    sum += i
    print(i, end = ",")
    if sum > 1000:
        break
print("\n合計が1000超えるのは、1~", i, "を加算した時です")