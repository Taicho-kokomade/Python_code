def check_3_5multi(num):
    if num % 3 == 0 or num % 5 == 0:
        return True
    else:
        return False


def check_5_3_multi(num):
    if num % 3 != 0 and num % 5 != 0:
        return True
    else:
        return False
