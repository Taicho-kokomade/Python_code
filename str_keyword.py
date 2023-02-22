# 予約済の識別子(キーワード)を確認する
import keyword
id1 = "tiff"
id2 = "if"

# keywordモジュールで『文字列が予約済の
# 識別子であるか』をiskeyword関数を使って判定
print(keyword.iskeyword(id1))
print(keyword.iskeyword(id2))

# isidentifierメソッドは「与えられた文字列がキーワード
# として認められている文字のみで構成せれているか」を判定するだけ
print(id1.isidentifier())
print(id2.isidentifier())
