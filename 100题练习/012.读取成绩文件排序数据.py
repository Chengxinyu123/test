def read_file():
    with open('./012.读取成绩文件排序数据.txt', 'r', encoding='UTF-8') as text:
        result = []
        for line in text:
            line = line[:-1]
            result.append(line.split(","))
    return  result

def sort_grade(datas):
    datas = sorted(datas, key=lambda x: int(x[2]), reverse=True)
    return datas
def write_output(data):
    with open('./012.out_put.txt', 'w', encoding='UTF-8') as output:
        for i in data:
            output.write(",".join(i) + "\n")
datas = read_file()
datas = sort_grade(datas)
write_output(datas)

# text = open('./012.读取成绩文件排序数据.txt', 'r', encoding='UTF-8')
# output = open('./012.out_put.txt', 'w', encoding='UTF-8')
# # append = text.readlines()
# # append = [item.strip() for item in append]
# # append = [item.split(",") for item in append]
# # result = sorted(append, key=lambda x: int(x[2]), reverse=True)
# for i in read_file():
#     str = ",".join(i) + '\n'
#     output.write(str)
#
#
#
# output.close()


