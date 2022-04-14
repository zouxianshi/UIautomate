# -*- coding: utf-8 -*- 
# @Time : 2022/3/21 16:55 
# @Author : crow
# @File : run.py

import unittest

from config import log
from config.driver_generator import quit_driver

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
        quit_driver()

    # url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=edd0497d-9aa7-4196-9498-a4e32a4ab41e'  # 机器人的webhook地址
    # headers = {'Content-type': 'application/json'}
    # data = {
    #     "msgtype": "text",
    #     "text": {
    #         "content": "test",  # x为要发送的文字
    #         "mentioned_list": ["@all"]  # 可指定人
    #     }  # 更多用途可查询企业微信官方
    # }
    # resp = requests.post(url, headers=headers, json=data)
    # print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), resp.text)
    # resp.close()
