begin = int(input('请输入起始值：'))
end = int(input('请输入结束值：'))


def is_ou(begin, end):
    result = []
    if begin % 2 == 0:
        for i in range(begin, end, 2):
            result.append(i)
    else:
        for i in range(begin+1, end, 2):
            result.append(i)
    return  result
data = [item for item in range(begin, end) if item % 2 == 0]
print(data)
out = is_ou(begin, end)
print(out)
