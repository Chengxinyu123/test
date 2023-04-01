# 输入
# 原始列表：[3,5,7,9,11,13]
# 移除元素：[7,11]
# 返回
# [3,5,9,13]

import re


def remove_content(origin_list, remove_list):
    for i in remove_list:
        while i in origin_list:
            origin_list.remove(i)
    return origin_list


origin_list_str = input('请输入初始列表：')
remove_list_str = input('请输入要移除的元素：')
item_origin = re.findall("[0-9]+", origin_list_str)
item_remove = re.findall("[0-9]+", remove_list_str)
origin_list = [int(item) for item in item_origin]
remove_list = [int(item) for item in item_remove]

result = [item for item in origin_list if item not in remove_list]


if __name__ == "__main__":
    result = [item for item in origin_list if item not in remove_list]
    print(result)
    print(remove_content(origin_list, remove_list))
