# 引数 広義にparameter 仮引数parameter 実引数argument
# 仮引数 関数などが値を要求する表明 formal parameter?
# 実引数 表明に対して実際に渡された値 actual parameter?


def say_hello(target=" Python"):
    print("Hello" + target)


say_hello()


def say_yes(target, target2=" Python"):
    print("Hello" + target)
    print("Hello" + target2)


say_yes(" world")


def say_good(target2, target1=" World"):
    print(" hello " + target1)
    print(" hello " + target2)


say_good(" Python")


def say_bye(*targets):
    # "*"で可変長引数、リストが使える
    for target in targets:
        print("Hey " + target)


say_bye("World", "Python", "Programming")


def say_come(**targets):
    # "**"で辞書に、辞書の中身は引数として
    # 与えた順番になるとは限らない
    for person, mens in targets.items():
        print(person + "人" + mens)


say_come(America="hello", France="Bonjour", Kenya="Jambo")
