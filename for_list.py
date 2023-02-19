data1 = [15,43,7,59,98]
data2 = [i * 2 for i in data1] #内包表記
print(data2)
print("\n")

data3 = [15,43,7,59,98]
data4 = [] #通常のfor文で記述するなら
for u in data3:
    data4.append(u * 2) #appendはリストに要素を追加する命令
print("\n")

#内包表記は文でなく式である、そのまま結果を変数に渡せる！！
#forと同様で、リストに限らずイテラブル型なら内包表記可能
#リスト内包、セット内包、辞書内包

data5 = [15,43,7,59,98]
data6 = [str(v) for v in data5] #リストの数値を文字列に変換
print(data6)


