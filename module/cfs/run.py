# -*- coding: utf-8 -*- 
# @Time : 2022/3/21 16:55 
# @Author : crow
# @File : run.py
import os
import sys
import unittest
from config import log

loader = unittest.TestLoader()
suite = unittest.TestSuite()
runner = unittest.TextTestRunner(verbosity=2)

# current_work_dir = os.path.dirname(__file__)
# # 获取 "test_case" 的绝对路径
# dir_test_case = current_work_dir + '/testcase'
# log.info("相对路径：" + dir_test_case)
# dir_test_case = r"D:\PycharmProjects\UIautomate\module\cfs\testcase"


# 把 "test_case" 的绝对路径 加入 sys.path


def test_suite1():
    # sys.path.append(dir_test_case)
    # log.info(sys.path)
    case_1 = loader.loadTestsFromName('testcase.login.test_login.test_login')
    suite.addTests(case_1)
    runner.run(suite)


if __name__ == '__main__':
    test_suite1()


