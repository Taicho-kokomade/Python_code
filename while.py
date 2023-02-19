i = 1
while i < 6:
    print(i, "番目のループです")
    i += 1

#x = 1 #無限ループ
#while x < 6:
    #print(x, "番目のループです")

#リストでなくとも、イテラブル型ならforに列挙可能
data1 = "こんにちは、赤ちゃん"
for value in data1:
    print(value)

data2 = 1 #開始から終了までの連続した数値を要素として持つrange型オブジェクトを作成する
for data2 in range(1,6): #疑似的なリストを生成 厳密にはrangeは関数ではなく型
    print(data2, "番目のグループです")

