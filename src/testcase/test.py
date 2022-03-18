# -*- coding: utf-8 -*-
# @Time : 2022/3/2 17:48
# @Author : crow
# @File : test.py

import unittest

import ddt

from src.module.exyz.script import login, follow_up_plan
from src.common import driver_generator


@ddt.ddt
class Test(unittest.TestCase):

    def setUp(self):
        print("测试开始")

    def test_login(self):
        login.login("18888888888", "Yy@123456")
        follow_up_plan.follow_up_plan_add()

    def tearDown(self):
        # driver_generator.quit_driver()
        print("测试结束")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test("test_login"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
