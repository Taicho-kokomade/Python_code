# インデックス・スライス構文
# txt()[index(インデックス番号)]
# txt()[start(開始位置):end(終了位置):step(増減)]

title = "あいうえおかきくけこ"

print(title[2])
print(title[2:5])  # "うえお"になる０１２番目の"う"５文字目の"お"まで
print(title[2:])
print(title[:5])
print(title[:])  # endだけ指定位置までということで全部？
print(title[-7:])  # えおかきくけこ
print(title[-7:-5])  # 後ろから７文字目、後ろから５文字目で"えお"
print(title[::2])  # step １文字おきの取出し"あうおきけ"
print(title[1::2])  # "いえかくこ" 
print(title[::-1])  # 末尾から１文字ずつ、こけくきかおえういあ
