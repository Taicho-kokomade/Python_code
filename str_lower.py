# 文字変換のメソッド
data1 = "Wings Project"
data2 = "self learn python"
data3 = "Fußball"

print(data1.lower())  # 大文字→小文字に変換
print(data1.upper())  # 小文字→大文字に変換
print(data1.swapcase())  # 大文字と小文字を反転
print(data2.capitalize())  # 先頭文字を大文字に、以降を小文字に変換
print(data2.title())  # 単語の先頭文字を大文字に、それ以外を小文字に変換
print(data3.lower())
print(data3.casefold())  # 大文字小文字の区別を除去
# casefoldは大文字小文字の区別を完全になくす、
# 大文字小文字の区別せずに比較する時は最初にcasefoldで区別の除去をする