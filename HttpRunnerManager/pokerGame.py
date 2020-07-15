# -*- coding:utf-8 -*-

# 题目：从扑克牌中随机抽 5 张牌，判断是不是顺子，
# 即这 5 张牌是不是连续的。2-10 为数字本身，A 为 1，J 为 11，Q 为 12，K 为 13，
# 而大小王可以看成任意的 数字。

# 先抽取5张，
# 然后判断抽取的是否有大小王，如果有王，先去掉王
# 然后剩下的牌分数字牌和字母牌，数字牌和字母牌组合成一条数据
# 先判断数字牌和字母牌是不是顺子，如果是，那抽取的就是顺子，如果不是，加入王后组合判断是否可以组成顺子

import random

def poker():
    num = ["A","2","3","4","5","6","7","8","9","10",'J','Q','K']
    poker = num * 4 + ["大王","小王"]
    return poker

def pokerRandom(poker2):
    # 随机抽取5张
    while poker2:
        pokerIn = random.sample(poker2, 5)
        print("随机抽取：", pokerIn)
        if len(pokerIn) != len(set(pokerIn)):
            continue
        else:
            return pokerIn


def pokerK(pokerIn):
    # 王牌筛选
    pokerK = []
    for pokerKstr in pokerIn:
        if pokerKstr == "大王" or pokerKstr == "小王":
            pokerK.append(pokerKstr)
            print("王牌数据：", pokerK)
    return pokerK

def pokerResult(pokerIn):
    # 数字牌&字母牌组合
    num = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
    letter = ['A', 'J', 'Q', 'K']
    pokerResult = []
    pokerN = []
    pokerL = []
    for pokerStr in pokerIn:
        if pokerStr in num:
            pokerN.append(pokerStr)
        if pokerStr in letter:
            pokerL.append(pokerStr)

    print("数字牌：", pokerN)
    print("字母牌：", pokerL)

    for i in range(len(pokerL)):
        if pokerL[i] == "A":
            pokerL[i] = 1
        elif pokerL[i] == "J":
            pokerL[i] = 11
        elif pokerL[i] == "Q":
            pokerL[i] = 12
        elif pokerL[i] == "K":
            pokerL[i] = 13
        # print("遍历的字母牌：", pokerL[i])
    print("字母牌转换成数字牌后：", pokerL)

    pokerResult = pokerN + pokerL
    return pokerResult

def poker_Result(pokerK,pokerResult):
    judge = 0
    judgeN = 0
    for i in range(1, len(pokerResult2)):
        if pokerResult2[i - 1] == pokerResult2[i] - 1:
            judge = judge + 1
        else:
            judgeN = judgeN + 1

    print("连续数量",judge)
    print("不连续数量",judgeN)

    if judge == len(pokerResult)-1:
        print("排序后的抽取牌：是连续的，随机抽取的牌也是连续的")
    elif judge == len(pokerResult)-2 and pokerResult[1]-pokerResult[0]==9:
        print("排序后的抽取牌：10,J,Q,K,A 可以组成顺子")

    elif judge != len(pokerResult)-1 :
        # print("排序后的抽取牌：不是连续的继续判断王牌组合后是否可以组成顺子")
        if len(pokerK) != 0 :

            if len(pokerK) == 1 :
                if judgeN == 1 :
                    for i in range(1, len(pokerResult)):
                        if pokerResult[i] - pokerResult[i - 1] > 2:
                            print("王牌&排序后的抽取牌组合：不连续数字大于1 组合单张王牌后不可以组成顺子")
                        elif pokerResult[i] - pokerResult[i - 1] == 2:
                            print("王牌&排序后的抽取牌组合：组合单张王牌后可以组成顺子")
                elif judgeN > 1:
                    print("王牌&排序后的抽取牌组合：组合单张王牌后不可以组成顺子")


            elif len(pokerK) == 2 :
                if judgeN == 2:
                    for i in range(2, len(pokerResult)):
                        if pokerResult[i-1] - pokerResult[i-2] == 2 and pokerResult[i] - pokerResult[i-1] == 2:
                            print("王牌&排序后的抽取牌组合：组合2张王牌后可以组成顺子")
                        else:
                            print("王牌&排序后的抽取牌组合：两个不连续数字差有一个或两个大于2，组合2张王牌后不可以组成顺子")

                elif judgeN == 1:
                    # 3,4,6 3,4,7 3,4,8
                    if pokerResult[1] - pokerResult[0] == 1 and 4 > pokerResult[2] - pokerResult[1] > 1:
                        print("王牌&排序后的抽取牌组合：组合2张王牌后可以组成顺子")
                    elif 4 > pokerResult[1] - pokerResult[0] >1 and pokerResult[2] - pokerResult[1] == 1:
                        print("王牌&排序后的抽取牌组合：组合2张王牌后可以组成顺子")
                    else:
                        print("王牌&排序后的抽取牌组合：其中一个不连续数字差有一个大于3，组合2张王牌后不可以组成顺子")

                    # for i in range(1, len(pokerResult)):
                    #     if pokerResult[i] - pokerResult[i-1] == 4 or pokerResult[i] - pokerResult[i-1] == 1:
                    #         print("王牌&排序后的抽取牌组合：组合2张王牌后可以组成顺子")

                elif judgeN > 2 :
                    print("王牌&排序后的抽取牌组合：组合2张王牌后不可以组成顺子")
        else:
            print("王牌&排序后的抽取牌组合：没有王牌，本次抽取的牌无法组成顺子")





# 所有的扑克牌面
poker2 = poker()
print("所有扑克牌：",poker2)
# 随机抽取五张
pokerIn = pokerRandom(poker2)
# 王牌筛选
pokerK2 = pokerK(pokerIn)
# # 数字牌&字母牌组合
pokerResult2 = pokerResult(pokerIn)
for i,j in enumerate(pokerResult2): pokerResult2[i] = int(j)
pokerResult2.sort()
print("组合排序后的抽取牌",pokerResult2)

# pokerK2 = ["大王"]
# pokerResult2 = [9,10,11,12]
# 计算组合后的数据连续数量用于逻辑判断
poker_Result(pokerK2,pokerResult2)








# print("所有扑克牌：",poker())
#
# num = ["2","3","4","5","6","7","8","9","10"]
# letter = ['A','J','Q','K']


# 随机抽取5张
# while poker():
#     pokerIn = random.sample(poker(), 5)
#     print("随机抽取：",pokerIn)
#     if len(pokerIn) != len(set(pokerIn)):
#         continue
#     else:
#         break

# 王牌筛选
# pokerK = []
# for pokerKstr in pokerIn :
#     if pokerKstr == "大王" or pokerKstr == "小王":
#         pokerK.append(pokerKstr)
#         print("王牌数据：",pokerK)

# 数字牌&字母牌组合
# pokerResult = []
# pokerN = []
# pokerL = []
# for pokerStr in pokerIn:
#     if pokerStr in num:
#         pokerN.append(pokerStr)
#     if pokerStr in letter:
#         pokerL.append(pokerStr)
#
# print("数字牌：",pokerN)
# print("字母牌：",pokerL)
#
# for i in range(len(pokerL)):
#     if pokerL[i] == "A":
#         pokerL[i] = 1
#     elif pokerL[i] == "J":
#         pokerL[i] = 11
#     elif pokerL[i] == "Q":
#         pokerL[i] = 12
#     elif pokerL[i] == "K":
#         pokerL[i] = 13
#     print("遍历的字母牌：",pokerL[i])
# print("字母牌转换成数字牌后：",pokerL)
#
# pokerResult = pokerN + pokerL

# for i,j in enumerate(pokerResult): pokerResult[i] = int(j)
# pokerResult.sort()
# print("排序后的抽取牌",pokerResult)
#
# # pokerK = ["大王"]
# # pokerResult = [5,6,9,10]

# judge = 0
# judgeN = 0
# for i in range(1,len(pokerResult)):
#     if pokerResult[i-1] == pokerResult[i]-1 :
#         judge = judge + 1
#     else:
#         judgeN = judgeN +1
#
# # print("连续数量",judge)
# # print("不连续数量",judgeN)
#
#
# if judge == len(pokerResult)-1:
#     print("排序后的抽取牌：是连续的，随机抽取的牌也是连续的")
# elif judge != len(pokerResult)-1 :
#     # print("排序后的抽取牌：不是连续的继续判断王牌组合后是否可以组成顺子")
#     if len(pokerK) != 0 :
#
#         if len(pokerK) == 1 :
#             if judgeN == 1 :
#                 for i in range(1, len(pokerResult)):
#                     if pokerResult[i] - pokerResult[i - 1] > 2:
#                         print("王牌&排序后的抽取牌组合：不连续数字大于1 组合单张王牌后不可以组成顺子")
#                     elif pokerResult[i] - pokerResult[i - 1] == 2:
#                         print("王牌&排序后的抽取牌组合：组合单张王牌后可以组成顺子")
#             elif judgeN > 1:
#                 print("王牌&排序后的抽取牌组合：组合王牌后不可以组成顺子")
#
#
#         elif len(pokerK) == 2 :
#             if judgeN == 2:
#                 for i in range(2, len(pokerResult)):
#                     if pokerResult[i-1] - pokerResult[i-2] == 2 and pokerResult[i] - pokerResult[i-1] == 2:
#                         print("王牌&排序后的抽取牌组合：组合2张王牌后可以组成顺子")
#                     else:
#                         print("王牌&排序后的抽取牌组合：两个不连续数字差有一个或两个大于2，组合2张王牌后不可以组成顺子")
#
#             elif judgeN == 1:
#                 # 3,4,6 3,4,7 3,4,8
#                 if pokerResult[1] - pokerResult[0] == 1 and 4 > pokerResult[2] - pokerResult[1] > 1:
#                     print("王牌&排序后的抽取牌组合：组合2张王牌后可以组成顺子")
#                 elif 4 > pokerResult[1] - pokerResult[0] >1 and pokerResult[2] - pokerResult[1] == 1:
#                     print("王牌&排序后的抽取牌组合：组合2张王牌后可以组成顺子")
#                 else:
#                     print("王牌&排序后的抽取牌组合：其中一个不连续数字差有一个大于3，组合2张王牌后不可以组成顺子")
#
#                 # for i in range(1, len(pokerResult)):
#                 #     if pokerResult[i] - pokerResult[i-1] == 4 or pokerResult[i] - pokerResult[i-1] == 1:
#                 #         print("王牌&排序后的抽取牌组合：组合2张王牌后可以组成顺子")
#
#             elif judgeN > 2 :
#                 print("王牌&排序后的抽取牌组合：组合2张王牌后不可以组成顺子")
#     else:
#         print("王牌&排序后的抽取牌组合：没有王牌，本次抽取的牌无法组成顺子")







# import random
# list1 = ['佛山', '南宁', '北海', '杭州', '南昌', '厦门', '温州']
# # 随机返回只有一个值的list
# a = random.sample(list1, 1)
#
# # 随机返回只有一个值的list
# b = random.sample(list1, 3)
# print(a)
# print(b)

# print("\n\n\n")
#
# from itertools import groupby
#
# lst = [1, 2, 3, 5, 6, 7, 8, 11, 12, 13, 19]    # 连续数字
#
# fun = lambda x: x[1]-x[0]
# for k, g in groupby(enumerate(lst), fun):
#     print("k:",k)
#     print("g",g)
#     l1 = [j for i, j in g]    # 连续数字的列表
#     print("l1:",l1)
#     if len(l1) > 1:
#         scop = str(min(l1)) + '-' + str(max(l1))    # 将连续数字范围用"-"连接
#     else:
#         scop = l1[0]
#     print("连续数字范围：{}".format(scop))
