data1 = [1,2,3]
data2 = [1,2,3]
print(data1 == data2) #同値性　値が等しいか True
print(data1 is data2) #同一性　オブジェクト　格納先が等しいか False

data3 = "あいう"
data4 = "あいう"
print(data3 == data4) #True
print(data3 is data4) #イミュータブル型だからTrueになる
