'''文件说明：
    1、为Main.py判断是否满足发送验证码的条件，并生成验证码并发送
    2、为Main.py的注册模块判断是否满足注册条件
'''
import sys
import zhenzismsclient as smsclient
import random
import database

# 生成四位数的随机验证码
def SMS_code_creat():
    code = ''
    for num in range(1, 5):
        code = code + str(random.randint(0, 9))
    print(code)
    return code
def SMS_code_send(phonenumber, code):
    # 将AppId和AppSecret复制粘贴过来
    AppId = "102780"
    AppSecret="c196a62e-6828-44bc-9826-d77549af685b"
    client = smsclient.ZhenziSmsClient('https://sms_developer.zhenzikj.com', AppId,AppSecret )
    # 第一个参数为发送号码，第二个参数为发送的验证码内容
    result = client.send(phonenumber, '您的验证码为'+code)
    # 注意result为str类型，并不是字典
'''函数功能：
    发送验证码到指定手机号，返回值为发送的验证码
'''
def sendCode(phonenumber):
    code = SMS_code_creat()
    SMS_code_send(phonenumber, code)
    return code
'''函数功能：
    当点击发送验证码button时执行此函数判断是否符合发送验证码的条件
'''
def isSendOK(phonenumber):
    returnString = ""
    returnNumber = 0
    '''判断手机号格式是否符合要求'''
    isPhoneNumberCorrect = 1
    if len(phonenumber) != 11:
        isPhoneNumberCorrect = 0
    for c in phonenumber:
        if c < '0' or c > '9':
            isPhoneNumberCorrect = 0
    if isPhoneNumberCorrect == 0:
        returnString = "手机号码格式不正确！"
        return returnString, returnNumber
    return returnString, 1
'''函数功能：
    当点击注册button时执行此函数判断是否符合注册条件
'''
def writeInLast(username,password):
    f = open('User.txt', 'a')
    data = f.write("用户名：%s\n"%username)
    data = f.write("密码：%s\n"%password)
#writeInLast("丁亦凡", "345")

def isRegisterCorrect(username, secret, repeat, phonenumber, code, producedCode):
    returnString = ""
    returnNumber = 0
    '''判断手机号格式是否符合要求'''
    isPhoneNumberCorrect = 1
    if len(phonenumber) != 11:
        isPhoneNumberCorrect = 0
    for c in phonenumber:
        if c < '0' or c > '9':
            isPhoneNumberCorrect = 0
    if len(phonenumber) == 0:
        returnString = "请输入手机号"
        return returnString, returnNumber
    if isPhoneNumberCorrect == 0:
        returnString = "手机号码格式不正确！"
        return returnString, returnNumber
    '''判断验证码是否正确'''
    isCodeCorrect = 1
    if code == "":
        returnString = "请发送验证码并输入！"
        return returnString, returnNumber
    if code != producedCode:
        isCodeCorrect = 0
        returnString = "验证码输入不正确！"
        return returnString, returnNumber
    '''判断用户名是否已经存在'''
    if username == "":
        returnString = "请输入用户名！"
        return returnString, returnNumber
    prime = database.selectDb2(username)
    if prime == 1:
        returnString = "用户名已存在！"
        return returnString, returnNumber
    '''判断密码长度是否符合标准'''
    isSecretLenthCorrect = 1  # 密码长度是否符合标准
    if len(secret) < 6 or len(secret) > 10:
        isSecretLenthCorrect = 0
        returnString = "密码长度不符合标准！"
        return returnString, returnNumber
    '''判断密码格式是否正确'''
    isCapitalLettersExist = 0   # 是否存在大写字母
    isLowercaseLettersExist= 0  # 是否存在小写字母
    isNumberExist = 0       # 是否存在数字
    for c in secret:
        if 'A' <= c <= 'Z':
            isCapitalLettersExist = 1
        if 'a' <= c <= 'z':
            isLowercaseLettersExist = 1
        if '0' <= c <= '9':
            isNumberExist = 1
    isSecretCorrect = isCapitalLettersExist + isLowercaseLettersExist + isNumberExist  # 密码整体格式是否正确
    if isSecretCorrect != 3:
        returnString = "密码格式不正确！"
        return returnString, returnNumber
    '''判断两次输入的密码是否相同'''
    isSecretRepeat = 1      #密码和重新输入的密码是否相同
    if secret != repeat:
        isSecretRepeat = 0
        returnString = "两次输入的密码不同！"
        return returnString, returnNumber


    '''如果上述都符合标准，returnString为空'''
    return returnString, 1

'''
string, number = isRegisterCorrect("张三", "123qweQWE", "123qweQWE", "13278880691", "2345", "2345")
print(string)
print(number)
'''