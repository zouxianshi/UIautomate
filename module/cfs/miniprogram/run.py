# -*- coding: utf-8 -*-
# @Time : 2022/3/21 16:55
# @Author : crow
# @File : mini.py

import unittest

from common import win32
from config import log

loader = unittest.TestLoader()
suite = unittest.TestSuite()
runner = unittest.TextTestRunner(verbosity=2)


def test_suite1():
    case_1 = loader.loadTestsFromName('testcase.mini.AppTest.get_all_pages_path')
    suite.addTests([case_1])
    runner.run(suite)


if __name__ == '__main__':
    try:
        test_suite1()
    except Exception as e:
        log.info(e)
