# 変数のscope global変数 local変数

a = 10
b = 20


def multiply(x, y):
    print(a)
    return x * y


print(multiply(a, b))


c = 10
d = 20
# グローバル変数cは関数内部では参照のみが
# 許されていて、代入や変更はglobal宣言をすることで
# 関数内部での代入、変更ができるようになる


def multi(x, y):
    global c
    c = c + 30
    return x * y


print(multi(c, d))
print(c)
