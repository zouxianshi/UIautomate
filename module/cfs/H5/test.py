import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import log


class Test01(object):
    def __init__(self):
        # 微信配置文件
        caps = {
            "platformName": "Android",
            "deviceName": "ca2b3455",
            "appPackage": 'com.tencent.mm',
            "appActivity": 'com.tencent.mm.ui.LauncherUI',
            "autoGrantPermissions": True,
            # 指定目标小程序的进程名称
            "chromeOptions": {
                "androidProcess": "com.tencent.mm:appbrand0"
            },
            "noReset": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(60)  # 隐式等待

        log.info(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_01(self):
        """搜索"""
        self.driver.get("http://m.baidu.com")
        self.driver.find_element_by_id("index-kw").click()
        self.driver.find_element_by_id("index-kw").send_keys("appium")
        search_locator = (By.ID, "index-bn")
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(search_locator))  # 显式等待
        self.driver.find_element(*search_locator).click()


if __name__ == '__main__':
    test = Test01()
    test.test_01()
