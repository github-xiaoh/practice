# -*- coding:utf-8 -*-


import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "root123456", "practice2", charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM test1 WHERE id < 100"
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   print("执行1")
   print(results)
   for row in results:
      age = row[1]
      name = row[0]
      # 打印结果
      print ("age=%s,name=%s"%(age, name ))
except:
   print ("Error: unable to fecth data")

# 关闭数据库连接
db.close()







#!/usr/bin/python

import MySQLdb

# 打开数据库连接

user_name = 'vsvyfcxnqq60t$iaGYxk'
pass_word = 'vsvyfcxnqq60t$iaGYxk'

db = MySQLdb.connect("localhost", "root", "root123456", "practice2", charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = "INSERT INTO test1(id,name,age) VALUES" + "(26,'mmmm',22)" + ',' + '(25,"kkk",+23)'
print(sql)
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
   print("插入成功")
except:
   # 发生错误时回滚
   db.rollback()
   print("插入数据失败，回滚完成！！！")

# 关闭数据库连接
db.close()