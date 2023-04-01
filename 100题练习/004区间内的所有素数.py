
def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for a in range(2, int(num / 2) + 1):
            if num % a == 0:
                return False
    return True

def sushu(bg, ed):
    result = []
    for i in range(bg, ed+1):
        if is_prime(i):
            result.append(i)
    return result


bg = int(input('请输入起始值：'))
ed = int(input('请输入结束值：'))
print(sushu(bg, ed))