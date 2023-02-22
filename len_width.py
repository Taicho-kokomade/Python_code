import unicodedata

title = "WINGS プロジェクト"
print(len(title))  # lenは日本語も1文字としてカウント
# 全角を２文字としてカウントするなら、

# unicodedataモジュールのeast_asian_width関数を利用
data = "WINGS プロジェクト２０２０"
count = 0
for ch in data:
    if unicodedata.east_asian_width(ch) in "FWA":
        # FWAは戻り値の判定、ようは全角を２としてカウント
        count += 2
    else:
        count += 1
print(count)
