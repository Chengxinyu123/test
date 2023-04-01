# 学生成绩是复杂列表，元素是字典或者元组
'''
[
    {'sno': 101, 'sname': "小张", 'sgrade': 88},
    {'sno': 102, 'sname': "小王", 'sgrade': 77},
    {'sno': 103, 'sname': "小李", 'sgrade': 99},
    {'sno': 104, 'sname': "小赵", 'sgrade': 66}
]
'''

origin_list = [
    {'sno': 101, 'sname': "小张", 'sgrade': 88},
    {'sno': 102, 'sname': "小王", 'sgrade': 77},
    {'sno': 103, 'sname': "小李", 'sgrade': 99},
    {'sno': 104, 'sname': "小赵", 'sgrade': 66}
]

result = sorted(origin_list, key= lambda x: x['sgrade'])
print(result)

def pai_xu(origin_list, flag):
    result = []
    result.append(origin_list[0])
    for count in range(1, len(origin_list)):
        i = 0
        while i < len(result):
            if origin_list[count]['sgrade'] > result[i]['sgrade']:
                if i == len(result) - 1:
                    result.append(origin_list[count])
                    break
                i = i + 1
                continue
            else:
                result.insert(i, origin_list[count])
                break
    if flag == 0:
        return result
    else:
        result.reverse()
        return result
print(pai_xu(origin_list, 0))