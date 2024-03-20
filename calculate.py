'''解题函数
    all()函数返回值为
    所有题目的正确答案集合
    和
    生成的每道题目的四个选项
'''
import os
import math
import cmath
from decimal import Decimal
import random
def read_questions(path1):
    files = os.listdir(path1)
    text = []
    for file in files:  # 遍历文件夹
        if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
            f = os.path.basename(file)
            paths = path1 + '\\' + f  # 确定文件路径
            with open(paths, encoding='utf-8')as f:
                text.extend(f.readlines())  # 注意extend 和 append的区别
    '''格式化题目'''
    for tex in text:
        text.remove('\n')
    for i in range(0, len(text)):
        text[i] = text[i][text[i].index('.') + 2: text[i].index('\n')]
    return text


def remove_square(ques):
    #print("去平方：")
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    i = 0
    while 1:
        if ques[i]=='=':
            break
        if ques[i] == '²' and ques[i - 1] in number:
            square_number = ""
            j = 1
            while ques[i - j] in number:
                square_number = ques[i - j] + square_number
                j += 1
            j = j - 1
            # print(square_number)
            result = float(square_number) * float(square_number)
            # print(result)
            ques = ques[:i - j] + str(result) + ques[i + 1:]
            i = i+len(str(result))-j
        else :
            i = i+1
    #print(ques)
    return ques


def remove_square_root(ques):
    #print("去根号")
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
    i = 0
    while 1:
        if ques[i]=='=':
            break
        if ques[i] == '√' and ques[i + 1] in number:
            square_root_number = ""
            j = 1
            while ques[i + j] in number:
                square_root_number = square_root_number + ques[i+j]
                j+=1
            result = cmath.sqrt(float(square_root_number))  # 结果为小数形式(1.4142135623730951+0j)
            stri = str(result)  # 转化成字符串形式
            stri = stri.strip('(')  # 去除首尾括号
            stri = stri.strip(')')
            stri = stri[0: len(stri)-3]  # 去除+0j
            ques = ques[0:i]+stri+ques[i+j:]
            i = i+len(stri)
        else:
            i = i+1

    #print(ques)
    return ques

def remove_trig_cos(ques):
    #print("去cos三角函数")
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
    i = 0
    while 1:
        if ques[i]=='=':
            break;
        if ques[i]=='c' and ques[i+3] in number:
            j=3
            trig_number = ""
            while ques[i+j] in number:
                trig_number = trig_number + ques[i+j]
                j+=1
            result = math.cos(float(trig_number))
            result = str(result)
            if result[0]=='-':
                result = '('+result+')'
            ques = ques[:i]+result+ques[i+j:]
            i=i+len(result)-3
        else :
            i=i+1
    return ques

def remove_trig_sin(ques):
    #print("去sin三角函数")
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
    i = 0
    while 1:
        if ques[i]=='=':
            break;
        if ques[i]=='s' and ques[i+1] == 'i' and ques[i+3] in number:
            j=3
            trig_number = ""
            while ques[i+j] in number:
                trig_number = trig_number + ques[i+j]
                j+=1
            result = math.sin(float(trig_number))
            result = str(result)
            if result[0]=='-':
                result = '('+result+')'
            ques = ques[:i]+result+ques[i+j:]
            i=i+len(result)-3
        else :
            i=i+1
    return ques

def remove_trig_tan(ques):
    #print("去tan三角函数")
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
    i = 0
    while 1:
        if ques[i]=='=':
            break;
        if ques[i]=='t' and ques[i+3] in number:
            j=3
            trig_number = ""
            while ques[i+j] in number:
                trig_number = trig_number + ques[i+j]
                j+=1
            result = math.tan(float(trig_number))
            result = str(result)
            if result[0] == '-':
                result = '('+result+')'
            ques = ques[:i]+result+ques[i+j:]
            i=i+len(result)-3
        else :
            i=i+1
    #print(ques)
    return ques

def calculate(ques):
    ques = ques.strip("=")
    #print(ques)
    n1 = eval(ques)
    n1 =round(n1, 5)   # 取小数点后5位
    print(n1)
    n = ['null','null','null','null']
    nindex = random.randint(0, 3)
    n[nindex]=n1
    for i in range(len(n)):
        if n[i] == 'null':
            if n1%1 == 0 :
                if n1 < 0:
                    n[i] = round(n1 + random.randint(0+n1, 0-n1), 5)
                else :
                    n[i] = round(n1 + random.randint(0-n1, 0+n1), 5)
            else:
                n[i] = round(n1 + random.uniform(0-n1,0+n1), 5)
    dict = {'A:' :n[0],'B:':n[1],'C:':n[2],'D:':n[3]}
    #print('A.' ,dict['A:'], 'B.', dict['B:'], 'C.' ,dict['C:'], 'D.', dict['D:'])
    return n1, nindex, dict # 返回正确答案和它所在的选项和所有选项

def all(question):
    answer= []
    diction = []

    for ques in question:
        ans, ind, dict= calculate(remove_trig_tan(remove_trig_sin(remove_trig_cos(remove_square_root(remove_square(ques))))))
        answer.append(ans)
        diction.append(dict)
    return answer, diction

