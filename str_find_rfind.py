# 文字列を検索する
msg = "にわにはにわにわとりがいる"

print(msg.find("にわ"))
print(msg.find("にも"))
print(msg.rfind("にわ"))
print(msg.find("にわ", 3))
print(msg.find("にわ", 3, 5))
print(msg.find("にわ", -7, -1))
#        s.find(sub[, start[, end]])

# 部分文字列が元の文字列に含まれているかどうかだけを
# 確認したい(=文字位置の取得が不要)ときは
# findメソッドではなく、in演算子を使う
