def get_diamond(diagonal1, diagonal2):
    return diagonal1 * diagonal2 / 2


print(get_diamond(6, 9))

area = get_diamond(8, 11)
print(f"ひし形の面積は{area}です。")
