# -*- coding: utf-8 -*-
# @Time : 2022/3/2 17:48
# @Author : crow
# @File : test.py

import unittest

from src.Module.exyz.script import login
from src.common import driver_generator


class Test(unittest.TestSuite):
    def setUp(self):
        pass

    def test_login(self):
        login.login("18774388904", "Silvercrow@6133")

    def tearDown(self):
        driver_generator.quit_driver()
