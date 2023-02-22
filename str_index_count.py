# 例外を返すindex/rindexメソッド
# msg = "にわにはにわにわとりがいる"
# print(msg.index(" に も "))
# エラー ValueError: substring not foundとでる

# 部分文字列の登場回数をカウントするcountメッソド
msg2 = "にわにはにわにわとりがいる"
print(msg2.count("にわ"))
print(msg2.count("にわ", 3))
print(msg2.count("にわ", 3, 6))

msg3 = "いちいちいちばにいち"
print(msg3.count("いちいち"))
# ２回カウントしそうだけど重複のない出現数を
# カウントするので１回のカウントになる
