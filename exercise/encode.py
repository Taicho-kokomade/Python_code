data = "こんにちは"
encode = data.encode("sjis")
print(encode)
encoded = encode
print(encoded.decode("sjis"))
print(encoded.decode("euc-jp", "replace"))
