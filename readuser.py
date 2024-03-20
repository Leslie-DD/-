'''功能函数
    为登录页面判断用户名和密码是否与user.txt.中的内容相符
    传进来的参数为登陆界面输入的用户名和密码
    返回值为判断用户名是否存在和密码是否正确，取值为0或1
    '''

import sys


def init_user():
    username_gather = []
    password_gather = []
    grade_gather = []
    user=[]
    with open('User.txt', encoding='gb2312') as file_obj: # 使用国际码编码，且单斜杠改为双斜杠
        user = file_obj.readlines()
    for i in range(0, len(user), 2):
        username_gather.append(user[i][4:-1])
        password_gather.append(user[i+1][3:-1])
    return username_gather, password_gather


def isCorrectOrNot(username,password):
    Username, Password = init_user()
    isUserExist = 0
    isPassCorrect = 0
    for i in range(0, len(Username)):
        if username == Username[i]:
            isUserExist = 1
            if password == Password[i]:
                isPassCorrect = 1
    return isUserExist, isPassCorrect

