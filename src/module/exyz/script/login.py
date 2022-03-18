# -*- coding: utf-8 -*- 
# @Time : 2022/3/4 10:16 
# @Author : crow
# @File : login.py

from src.module.exyz.obj import login_obj
from src.common import automatic_operation as ao
from config import log


def login(username, pwd):
    try:
        log.info("开始登陆")
        ao.get_url("https://ufsmch.med.gzhc365.com/#/login")
        ao.find_element(login_obj.userName_Xpath).click()
        ao.find_element(login_obj.userName_Xpath).send_keys(username)
        ao.find_element(login_obj.pwd_Xpath).send_keys(pwd)
        ao.find_element(login_obj.valiCode_Xpath).send_keys("12hc#$")
        ao.find_element(login_obj.button_Xpath).click()
        ao.find_element(login_obj.cgr_Xpath).click()
        log.info("登录成功")
    except Exception as e:
        log.info(e)


if __name__ == '__main__':
    login("18774388904", "SIlvercrow@6133")
