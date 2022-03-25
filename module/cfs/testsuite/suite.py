# -*- coding: utf-8 -*- 
# @Time : 2022/3/21 16:55 
# @Author : crow
# @File : suite.py
import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner(verbosity=2)

    login = loader.loadTestsFromName('login.test_login.test_login')
    # test_follow_up_plan = loader.loadTestsFromNames("test_add")
    suite.addTests(login)
    runner.run(suite)
