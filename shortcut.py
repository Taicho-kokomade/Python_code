x = 1
if x != 2:
    print("実行されました") #Trueだから実行される

x == 2 or print("実行されました") #Falseだから右式が実行される

print(hoge() or "default")

result = hoge()
print("default" if result is None else result)
