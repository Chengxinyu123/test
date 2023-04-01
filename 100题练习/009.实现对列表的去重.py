# 输入,包含重复元素的列表
# [10,10,20,20,30,30]
# 返回
# [10,20,30]


def distinct_list(origin_list):
    item = 0
    result = []
    for i in range(0, len(origin_list)):
        item = origin_list.pop()
        if item not in result:
            result.append(item)
    return result


print(distinct_list([1, 2, 3, 3, 2]))


# 还可以用set()
result = list(set(origin_list))s