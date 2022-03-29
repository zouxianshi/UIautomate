# -*- coding: utf-8 -*- 
# @Time : 2022/3/4 10:16 
# @Author : crow
# @File : login.py
import unittest

from module.cfs.obj import login_obj
from common import automatic_operation as ao
from config import log
from config.driver_generator import quit_driver


class test_login(unittest.TestCase):
    def test_login(self, username="18900000001", pwd="Yy@123456"):
        try:
            log.info("开始登陆")
            ao.get_url("https://ucfs.med.gzhc365.com/merchant/#/login")
            ao.find_element(login_obj.userName_Xpath).click()
            ao.find_element(login_obj.userName_Xpath).send_keys(username)
            ao.find_element(login_obj.pwd_Xpath).send_keys(pwd)
            ao.find_element(login_obj.valiCode_Xpath).send_keys("12hc#$")
            ao.find_element(login_obj.button_Xpath).click()
            # ao.find_element(login_obj.cgr_Xpath).click()
            log.info("登录成功")
        except Exception as e:
            log.info(e)
            quit_driver()