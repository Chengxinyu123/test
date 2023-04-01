import re
def list_sum(list1):
    list_long = len(list1)
    result = 0
    for i in range(0, list_long):
        result += int(list1[i])
    return result


if __name__ == '__main__':
    test = input('请按列表输入数字：')
    list_test = re.findall('[0-9]+', test)
    print(list_sum(list_test))
