#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''此文件为数据库操作
    在Main.py文件的当前路径下建数据库并存储用户名和密码
    '''
import sqlite3
import re
import sys
from prettytable import PrettyTable

DB_PATH = './passwd.db'


'''一个新创建的数据库当中是没有任何表的。
我们不能要求我们的用户自己去搞好一个表再来使用。
因此，当数据库不存在，在第一次链接的时候会自动创建这个数据库，
但是这个数据库中是没有任何表的，所以，我们需要检查数据库中有没有表，
如果有表，那么有没有我们使用的这个表，
如果不符合条件，我们则需要创建一个表，
并且这个表的结构要符合我们的设计。
'''
def checkDB(db):
    db.execute('''SELECT name FROM sqlite_master
                WHERE type IN ('table','view') AND name NOT LIKE 'sqlite_%'
                ORDER BY 1''')
    o = db.fetchall()
    if len(o) == 0 or not bool(re.search(r'(\'passwd\',)',str(o))):
        #print("创建了数据库")
        db.execute('''CREATE TABLE passwd (
            id integer primary key autoincrement,
            name varchar(255),
            password varchar(255),
            time timestamp default current_timestamp
        )''')
def insertDb(name,passwd):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    checkDB(c)
    prime = selectDb2(name)  # 判断用户名是否已经存在
    if prime == 1:  # 说明用户存在，不能注册此用户名
        return 0
    else:
        c.execute("INSERT INTO passwd (name,password) VALUES ('" + name + "', '" + passwd + "')");
        conn.commit()
        conn.close()
    return 1    #说明用户不存在，可以注册此用户名


def selectDb2(name):   # 注册是调用此函数，查看用户名是否已经存在
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    checkDB(c)

    select = "SELECT * from passwd "
    select += ('where name = ' + '\'' + name + '\'')

    res = list(c.execute(select))
    if len(res) == 0:
        return 0   # 用户不存在
    else:
        x = PrettyTable(['id','name','password','time'])
        x.align['name'] = 'l'
        x.padding_width = 1
        for row in res:
            x.add_row(list(row))
        #print(x)
    conn.close()
    return 1   # 用户存在
def selectDb(name,password):   # 登录调用此函数，查看用户名和密码是否正确
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    checkDB(c)

    select = "SELECT * from passwd "
    select += ('where name = ' + '\'' + name + '\'' + 'and password = ' + '\'' + password + '\'')

    res = list(c.execute(select))
    if len(res) == 0:
        #print('Info: record is empty')
        return 0    # 用户名和密码不正确
    else:
        x = PrettyTable(['id','name','password','time'])
        x.align['name'] = 'l'
        x.padding_width = 1
        for row in res:
            x.add_row(list(row))
        print(x)
    conn.close()
    return 1    # 用户名和密码正确

def deleteDb(name,password):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    checkDB(c)
    c.execute('DELETE from passwd where name =' + "'" + name + "'" + 'and password =' + "'" + password + "'" )
    conn.commit()
    o = conn.total_changes
    if o == 0:
        print('Failure: the password was not found')
    if o == 1:
        print('Success: name ' + "'" + name + "'" + ' password has been deleted')
    conn.close()

def display():
    select = "SELECT * from passwd "
    res = list(c.execute(select))   # 从数据库拿到结果，转换成列表
    x = PrettyTable(['id','name','password','time'])       # 给输出的表格设定表头，有几列就设定几个
    x.align['name'] = 'l'   # 可以给指定列设定文字对齐，默认是居中对齐，下面是改成了 left 左对齐
    x.padding_width = 1 # 设定表格内填充为 1 个空格，让表格可读性更高
    for row in res: # 循环数据
        x.add_row(list(row))        # 插入每一行的数据
    print(x)    # 打印表格

def updateDb(name, password, newpassword):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    checkDB(c)
    deleteDb(name,password)
    insertDb(name,newpassword)

    conn.close()

def isCorrectOrNot(username, password):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    checkDB(c)
    isUserExit = selectDb2(username)
    if isUserExit == 1:     #说明用户名存在，如果存在再判断密码是否正确
        isPassCorrect = selectDb(username, password)
        if isPassCorrect == 1:  # 说明用户名和密码匹配
            return 1, 1
        else:
            return 1, 0
    return 0, 0
#isCorrectOrNot("ding", "123")

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()
checkDB(c)
display()
'''
prime = insertDb("fan", "new3")
if prime == 1:
    print("插入成功！")
elif prime == 0:
    print("该用户已存在！")

#insertDb("ding", "new1")
#updateDb("ding","new","n123")
selectDb2("ding")
#deleteDb("ding","12328")
display()
time.sleep(10)
'''