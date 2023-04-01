# 给定一个正整数n 返回n*(n-1)*(n-2)...*1
def jiecheng(number):
    result = 1
    sum = number
    while number > 0:
        result *= number
        number -= 1
    return f'{sum}的阶乘是{result}'
print(jiecheng(6))