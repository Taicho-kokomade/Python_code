#リスト化すれば、その分メモリを使用するが
#次の値を生成するだけならば、rangeの大小に関わらず、メモリの使用量は変化しない
#この仕組みをイテレーターという
for i in range(1,6): #1以上5未満
    print(i, "番目")
print("\n")

for x  in range(10): #0から指定値　この場合０以上１０未満
    print(x, "番目")
print("\n")

for a in range(0, 10, 2): #第３引数に２指定で１つ飛ばし
    print(a, "番目")
print("\n")

for z in range(5, 0, -1): #負数を指定で逆順
    print(z, "番目")
print("\n")

for c in \
reversed(range(0,10,3)): #逆順の飛ばしはreversed関数のほうが見やすい
    print(c, "番目")
print("\n")

#range関数で生成されたrange値は、普通のprint文だと定義が出力されるだけ
#生成された値を確認するにはlist関数でリストに変換する
print(list(range(0, 7, 2)))


