'''文件说明：
    出题并将题目存到相应文件夹下'''

import random
import re
import os
import time

'''功能：创建文件夹
    若文件夹已存在……
    若不存在则创建
'''
def mkdir(path):
    path = path.strip()         # 去除首位空格
    path = path.rstrip("\\")    # 去除尾部 \ 符号
    isExists = os.path.exists(path) # 判断路径是否存在 存在True 不存在False
    if not isExists:   # 如果不存在则创建目录
        os.makedirs(path)
        return True
    else:               # 如果目录存在则不创建
        return False
'''功能：读取当前文件夹下所有已生成题目到列表中
    返回值为文件中的所有题目集合
'''
def read_questions(path1):
    files = os.listdir(path1)
    text = []
    for file in files: # 遍历文件夹
        if not os.path.isdir(file): # 判断是否是文件夹，不是文件夹才打开
            f = os.path.basename(file)
            paths=path1+'\\'+f  # 确定文件路径
            with open(paths, encoding='utf-8')as f:
                text.extend(f.readlines())  # 注意extend 和 append的区别
    '''格式化题目'''
    for tex in text:
        text.remove('\n')
    for i in range(0, len(text)):
        text[i] = text[i][text[i].index('.') + 2: text[i].index('\n')]
    return text
'''功能：随机化生成题目存到列表gather中，存到文件中
    参数：  题目数量count，
            年级（整型）level，
            用户姓名（用来确定文件夹名称）user_name，
            年级（字符串，用来确定文件夹名称）grade_level
    返回值：题目集合
'''
def set_questions(numberOfQuestion, level, user_name, grade_level):
    current_time = str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))  # 格式化当前时间
    path = user_name + '\\' + grade_level   # 举例： 张三\\初中
    mkdir(path)                             # 创建或打开文件夹
    gather = []
    path = path + '\\' + current_time + ".txt"  # 设置路径
    data = open(path, "w", encoding='utf-8')    # 打开文件

    qid = 0   #题号
    while qid < numberOfQuestion:
        '''
            生成小学题目
        '''
        basic_symble = ['+', '-', '*', '/']  # 基本操作符
        operate_symble_count = random.randint(1, 5)  # 操作符的个数
        operate_number_count = operate_symble_count + 1  # 题目中数的个数
        question_symble = []  # 用来存储这道题中的操作符
        question_number = []  # 用来存储这道题中的数
        for i in range(0, operate_symble_count):  # 生成题目中的所有操作符
            question_symble.extend(basic_symble[random.randint(0, 3)])
        question_symble.extend('=')
        for i in range(0, operate_number_count):  # 生成题目中的所有数
            question_number.append(random.randint(1, 100))
        '''添加括号
        '''
        left = [0] * operate_number_count
        right = [0] * operate_number_count
        exit = [0] * operate_number_count
        count = 0
        for i in range(0, operate_number_count):
            if (random.randint(1, 100) % 3 == 2 and exit[i] > 0 and left[i] == 0 and count > 0):  # 一个数右边加括号的条件
                right[i] += 1
                exit[i] -= 1
                count -= 1
            if (random.randint(1, 100) % 3 == 1 and i != operate_number_count - 1 and right[i] == 0):  # 一个数左边加括号的条件
                left[i] += 1
                count += 1
                for j in range(i, operate_number_count):
                    exit[j] += 1
        flag = 0
        for j in range(operate_number_count - 1, -1, -1):  # 此循环找 可以添加右括号 的开始位置
            if left[j] == 1:
                flag = j
                break
        while (count != 0):  # 左右括号不一样多就需要再次遍历
            flag1 = flag
            for i in range(flag1, operate_number_count):  # 从可以添加右括号的位置往后随机添加右括号
                if (random.randint(1, 100) % 3 == 2 and exit[i] > 0 and left[i] == 0 and count > 0):
                    right[i] += 1
                    exit[i] -= 1
                    count -= 1
                    break
        question = ""
        for i in range(0, operate_number_count):
            while left[i] > 0:
                question = question + '('
                left[i] -= 1
            question = question + str(question_number[i])
            while right[i] > 0:
                question = question + ')'
                right[i] -= 1
            question = question + question_symble[i]
        ''' 
            在小学题目的基础上生成初中题目
            要求是至少有一个平方或开根号运算
        '''
        number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
        if level == 1 or level == 2:
            square_or_root_number = 0
            while square_or_root_number == 0:
                c = 0
                while 1:
                    if question[c] == "=":
                        break
                    if (question[c] in number and c == 0) or \
                            (c != 0 and question[c - 1] in basic_symble and question[c] in number) or \
                            (c != 0 and question[c] in number and question[c - 1] == '('):
                        j = 0
                        nnumber = ""
                        while question[c + j] in number:
                            nnumber = nnumber + question[c + j]
                            j += 1
                        is_square_and_root = random.randint(0, 1)  # 随机生成 是否添加平方或根号
                        if is_square_and_root == 1:
                            square_or_root = random.randint(0, 1)  # 随机生成  平方还是根号
                            if square_or_root == 0:
                                question = question[:c + j] + '²' + question[c + j:]
                                square_or_root_number += 1
                            elif square_or_root == 1:
                                question = question[:c] + '√' + question[c:]
                                square_or_root_number += 1
                            c = c + j
                        else:
                            c = c + j
                    else:
                        c += 1


            #print("初中的出完了")
            ''' 
                在小学题目的基础上生成高中题目
                要求是至少有一个三角函数运算
            '''
            if level == 2:
                #print("开始出高中的")
                #print(question)
                trig_number = 0
                while trig_number == 0:
                    #print("yes")
                    c = 0
                    while 1:
                        if question[c] == "=":
                            break
                        if (question[c] in number and c == 0) or \
                                (c != 0 and question[c - 1] in basic_symble and question[c] in number) or \
                                (c != 0 and question[c] in number and question[c - 1] == '('):
                            j = 0
                            nnumber = ""
                            while question[c + j] in number:
                                nnumber = nnumber + question[c + j]
                                j += 1
                            is_square_and_root = random.randint(0, 1)  # 随机生成 是否添加三角函数
                            if is_square_and_root == 1:
                                which_trig = random.randint(0, 2)  # 随机生成  sin/cos/tan
                                if which_trig == 0:
                                    question = question[:c] + 'sin' + question[c:]
                                elif which_trig == 1:
                                    question = question[:c] + 'cos' + question[c:]
                                elif which_trig == 2:
                                    question = question[:c] + 'tan' + question[c:]
                                trig_number += 1
                                c = c + j + 3
                            else:
                                c = c + j
                        elif (c!=0 and question[c-1] == '√'): #可以在根号前生成三角函数
                            j = 1
                            nnumber = ""
                            while question[c + j] in number:
                                nnumber = nnumber + question[c + j]
                                j += 1
                            is_square_and_root = random.randint(0, 1)  # 随机生成 是否添加三角函数
                            if is_square_and_root == 1:
                                which_trig = random.randint(0, 2)  # 随机生成  sin/cos/tan
                                if which_trig == 0:
                                    question = question[:c-1] + 'sin' + question[c-1:]
                                elif which_trig == 1:
                                    question = question[:c-1] + 'cos' + question[c-1:]
                                elif which_trig == 2:
                                    question = question[:c-1] + 'tan' + question[c-1:]
                                trig_number += 1
                                c = c + j + 3
                            else:
                                c = c + j
                        else:
                            c += 1
                #print(question)

        #print(qid)
        '''查重'''
        repeat = 0  # 是否重复的标志，初始化为未重复

        for que in gather:  # 遍历题目集合中的每一道题
            if question == que:  # 如果发现有重复的
                repeat = 1  # 标志为有重复
                break  # 并且不用再继续遍历，跳出次循环即可
        #print(repeat)
        if repeat == 1:  # 如果此题目是重复的
            continue  # 不执行以下操作zha
        '''如果生成的该题目没有重复，那么执行下面的操作'''
        qid += 1  # 题号+1
        gather.append(question)  # 该题目收入题目集合
        print(str(qid) + '. ' + question + '\n', file = data)  # 并把该题目输出在.txt文件中
        print(question)

    data.close()
    return gather