# sortメソッド　list型の内容を逆順にソート
data = [25, 3, 49, 67, 14]
# dataをオブジェクトとして渡す
data.sort(reverse=True)  # 引数reverseをTrueで逆順の意味
print(data)
print()

# sorted関数
data2 = [25, 3, 49, 67, 14]
# data2を引数として渡す
print(sorted(data2, reverse=True))
print()
