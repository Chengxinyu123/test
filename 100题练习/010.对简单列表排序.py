# 简单列表：元素类型不是复合类型（列表中没有嵌套列表/元组/字典）
# 怎样原地排序？怎样不改变原列表排序
# list.sort()可以做到原地排序
# listb = sorted(lista) 可以保持列表a的顺序不变
# 怎样指定升序或降序
# list.sort(reverse=True) 和listb = sorted(lista, reverse=True)


def pai_xu(origin_list, flag):
    result = []
    result.append(origin_list[0])
    for count in range(1, len(origin_list)):
        i = 0
        while i < len(result):
            if origin_list[count] > result[i]:
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



print(pai_xu([1,1,1,1,2,3,5,6,7,8,9,5,6,7,2,3,4,5], 1))