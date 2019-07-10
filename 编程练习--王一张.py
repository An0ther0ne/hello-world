""""
(一)设计
设计一个关于户型的数据结构
"""
house_type = {
    "buildingType":"别墅",
    "name":"A-Z3-Y060",
    "area":3547,
    "length":23.4,
    "width":34.5,
    "heigth":67.9,
    "floor":23,
    "countHouse":345,
    "num":23,
    "double":21,
    "triple":1,
    "leftWall":1,
    "rightWall":0
}

"""
(二)编程
"""
# 第1题
import json

# 导入数据
with open('input.json',encoding='utf-8') as f:
    apartmentRadio = json.load(f)

# 整理出户型配比
housing_rate = {}# 创建空字典用于存储户型配比

for item in apartmentRadio:
    housing_rate[item["area"]] = item["countRate"]

print(housing_rate)


# 第2题
var1 = var2 = var3 = 0#var1,var2,var3已知，不妨设为0
num = 5
buildingArea = {}
dict_1 = {}; dict_1["name"] = "计容总建筑面积"; dict_1["planValue"] = var2
dict_2 = {}; dict_2["name"] = "不计容总建筑面积"; dict_2["planValue"] = var3
detail = [dict_1,dict_2]

buildingArea["sumplanValue"] = var1
buildingArea["detail"] = detail

print(buildingArea)


# 第3题
# 已知上述json，求“计容总建筑面积”的值（忽略第2题的构建过程）
detail = buildingArea["detail"]

for item in detail:
    if item["name"] == "计容总建筑面积":
        print(item["planValue"])


"""
(三)算法
"""
# 第一步
dict_1 = {115: 25, 140: 21, 180: 23}
dict_2 = {115: 7, 140: 5, 180: 3}
dict_3 = {115: 2, 140: 2, 180: 2}


def totalArea_differ():
    min = 93615
    for i in range(int(dict_1[115]*0.9),int(dict_1[115]*1.1)+2):
        for j in range(int(dict_1[140]*0.9),int(dict_1[140]*1.1)+2):
            for k in range(int(dict_1[180]*0.9),int(dict_1[180]*1.1)+2):
                totalArea = 115 * i * dict_2[115] * dict_3[115] + 140 * j * dict_2[140] * dict_3[140] + 180 * k * dict_2[180] * dict_3[180]
                if abs(totalArea-93615) < min:
                    min = abs(totalArea-93615)
                    s = (i,j,k)
    print(min,s)
totalArea_differ()

# 第二步（也可直接使用第三步中的代码）
# def totalArea_differ_2():
#     min = 93615
#     key_list = []# 创建一个空集合用于存储key的值
#     for i in dict_1.keys():
#         key_list.append(i)
#
#     # key_list中有多少个值，就使用多少个for循环（本题key_list的长度已知）
#     for i in range(int(dict_1[key_list[0]]*0.9),int(dict_1[key_list[0]]*1.1)+2):
#         for j in range(int(dict_1[key_list[1]]*0.9),int(dict_1[key_list[1]]*1.1)+2):
#             for k in range(int(dict_1[key_list[2]]*0.9),int(dict_1[key_list[2]]*1.1)+2):
#                  .
#                  .
#                  .
#                 totalArea = key_list[0] * i * dict_2[key_list[0]] * dict_3[key_list[0]] + key_list[1] * j * dict_2[key_list[1]] * dict_3[key_list[1]] + ...
#                 if abs(totalArea-93615) < min:
#                     min = abs(totalArea-93615)
#                     s = (i,j,k,...)
#     print(min,s)

# 第三步
import numpy as np

def totalArea_differ_3():
    min = 93615
    count = 0# 计数

    key_list = []# 创建一个空集合用于存储key的值
    value_1 = []; value_2 = []; value_3 = []
    for i in dict_1.keys():
        key_list.append(i)

    for i in range(len(key_list)):
        value_1.append(dict_1[key_list[i]])
        value_2.append(dict_2[key_list[i]])
        value_3.append(dict_3[key_list[i]])

    while min > 10:
        # 生成len(key_list)维(-0.1,0.1)之间的随机数
        index_array = (np.random.rand(len(key_list)) - 0.5) / 5

        floors = np.floor(value_1 * (index_array + np.ones(3)))# 层数
        totalArea = np.sum(key_list * floors * value_2 * value_3)
        min = abs(totalArea-93615)
        count += 1
    print(min,count)

totalArea_differ_3()