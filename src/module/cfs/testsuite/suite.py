# -*- coding: utf-8 -*- 
# @Time : 2022/3/21 16:55 
# @Author : crow
# @File : suite.py
import unittest

from src.module.cfs.testcase.follow_up_plan import test_follow_up_plan
from src.module.cfs.testcase.login import test_login

if __name__ == '__main__':
    tests = unittest.TestLoader().loadTestsFromNames(test_add)
    tests1 = unittest.TestLoader().loadTestsFromTestCase(test_follow_up_plan)
    suite = unittest.TestSuite()
    suite.addTests(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)
