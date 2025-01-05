import random as r

def get_random_account_number(size):
    account_num = [r.randint(1, 9)]

    for _ in range(1, size):
        account_num.append(r.randint(0, 9))

    result = ''
    for num in account_num:
        result += str(num)

    return int(result)