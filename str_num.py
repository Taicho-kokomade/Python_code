# 文字列を数値に変換
import unicodedata
# unicodedataモジュールのdigit/numeric関数を利用
print(unicodedata.digit("5"))
print(unicodedata.numeric("参"))
print(unicodedata.numeric("Ⅷ"))
# digitはint値　numericはfloat値を返す
# 漢数字、ローマ数字を変換するにはnumeric関数だけ

# これらを使うことで漢数字を入力されても半角数値に
# 整えて、後続の処理に渡すことができる
