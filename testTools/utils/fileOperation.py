# -*- coding:utf-8 -*-


import os


def newFile(reportPath):
    #列举reportPath目录下的所有文件，结果以列表形式返回。
    lists=os.listdir(reportPath)
    #sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    #最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn:os.path.getmtime(reportPath+'/'+fn))
    #获取最新文件的绝对路径
    file_path=os.path.join(reportPath,lists[-1])
#    L=file_path.split('\\')
#    file_path='\\\\'.join(L)
    return file_path



def openFile(newPath):
    ret = True
    try:
        with open(newPath,'r',encoding='utf-8') as f :
            reportText = f.readlines()
            return reportText
    except:
        ret = False
        return ret






# file = newFile("/Users/chenhang/Desktop/pythonFile/python/untitled/practice/Django-program/HttpRunnerManager/logs/script.log")
# print(file)
#
# fileText = openFile(file)
#
# if fileText:
#     print(fileText)
# else:
#     print("文件读取错误")
#
# str1 = 'b\'2018-06-29 11:14:13,438 [django.request:93] [base:get_response] [WARNING]- Not Found: /\\n2018-06-29 11:14:13,440 [django.server:124] [basehttp:log_message] [WARNING]- "GET / HTTP/1.1" 404 74\\n2018-06-29 11:14:29,552 [django.server:124] [basehttp:log_message] '
#
# fileText2 = str(fileText).split('\\n')
# log_list = []
# for i in fileText2:
#     print(i)
#     log_list.append(i)
# print(log_list)


# path = "/Users/chenhang/Desktop/pythonFile/python/untitled/practice/Django-program/HttpRunnerManager/logs/script.log"
#
#
# with open(path,'r',encoding='utf-8') as f :
#     reportText = f.readlines()
# print(reportText)
#
# log_list = []
# for line in reportText:
#     line = line.splitlines()
#     # print(line)
#     log_list.append(line)
#
# print(log_list)
