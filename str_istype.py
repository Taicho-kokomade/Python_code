# ・文字の種類の判定・
# isalnum()　英数字であるか
# isalpha()　英字であるか
# isascii()　ASCII文字であるか
# isdecimal()　１０進数値であるか
# isdigit()　数値であるか
# isnumeric()　数値文字であるか
# isidentifier()　有効な識別子であるか
# islower()　小文字であるか
# isupper()　大文字であるか
# istitle()　単語の先頭文字だけが大文字であるか
# isprintable()　印字可能な文字であるか
# isspace()　空白文字であるか
print("abc123".isalnum())
print("abc++".isalnum())
print("abcde".isalpha())
print("abc123".isalpha())
print("abc".isascii())
# isdigit isdecimal isnumericの違いは分かりにくい
# 大まかに、isdecimalはアラビア数字だけを認め
# isdigitはそれに加え「上付き数字」なども含める
# isnumericはさらに漢数字、ローマ数字なども含める
# 広く数字を認めるなら、isnumericが無難
