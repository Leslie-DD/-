'''文件功能说明：
    用来判断改密码时是否符合要求
    '''
import sys
import database
def isChangeCorrect(username,oldPassword, NewPassword, repeat):
    isUserCorrect = database.selectDb(username, oldPassword)  # 判断用户旧密码是否正确，正确为1
    if isUserCorrect == 0:
        return "原始密码不正确！", 0    # 说明旧密码不正确
    '''判断密码长度是否符合标准'''
    if len(NewPassword) < 6 or len(NewPassword) > 10:
        returnString = "新密码长度不符合标准！"
        return returnString, 0
    '''判断密码格式是否正确'''
    isCapitalLettersExist = 0  # 是否存在大写字母
    isLowercaseLettersExist = 0  # 是否存在小写字母
    isNumberExist = 0  # 是否存在数字
    for c in NewPassword:
        if 'A' <= c <= 'Z':
            isCapitalLettersExist = 1
        if 'a' <= c <= 'z':
            isLowercaseLettersExist = 1
        if '0' <= c <= '9':
            isNumberExist = 1
    isSecretCorrect = isCapitalLettersExist + isLowercaseLettersExist + isNumberExist  # 密码整体格式是否正确
    if isSecretCorrect != 3:
        returnString = "密码格式不正确！"
        return returnString, 0
    if repeat != NewPassword:
        return "两次输入的密码不同！", 0
    return "", 1
