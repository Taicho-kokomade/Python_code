data = ["さくら","うめ","ききょう","x","くちなし","ぼたん"]
for name in data:
    #要素がｘの場合にループ終了
    if name == "x":
        break
    print(name)
else:
    print("正常終了しました")#breakするとこのprintは出ない