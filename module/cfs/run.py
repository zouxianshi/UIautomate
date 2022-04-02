# -*- coding: utf-8 -*- 
# @Time : 2022/3/21 16:55 
# @Author : crow
# @File : run.py
import unittest

from common import automatic_operation
from config import log

loader = unittest.TestLoader()
suite = unittest.TestSuite()
runner = unittest.TextTestRunner(verbosity=2)


def test_suite1():
    case_1 = loader.loadTestsFromName('testcase.login.test_login.test_login')
    case_2 = loader.loadTestsFromName('testcase.follow_up_plan.test_follow_up_plan.test_add')
    suite.addTests([case_1, case_2])
    runner.run(suite)


if __name__ == '__main__':
    try:
        test_suite1()
    except Exception as e:
        log.info(e)
    finally:
        automatic_operation.quit_driver()
