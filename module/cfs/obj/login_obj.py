# -*- coding: utf-8 -*- 
# @Time : 2022/3/4 15:53 
# @Author : crow
# @File : login_obj.py 

userName_Xpath = "//*[@id=\"userName\"]"

# 密码输入框
pwd_Xpath = "//*[@id=\"loginPassword\"]"

# 验证码输入框
valiCode_Xpath = "//*[@id=\"valiCode\"]"

# 登录按钮
button_Xpath = "//*[@type=\"submit\"]"

# 随访员角色
sfy_Xpath = "//*[@id=\"root\"]//div[@class=\"role-name\"][contains(text(),\"健康管理师\")]"

# 超管人角色
cgr_Xpath = "//*[@id=\"root\"]//div[@class=\"role-name\"][contains(text(),\"财务\")]"
