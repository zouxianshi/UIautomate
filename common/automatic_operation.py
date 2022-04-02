# -*- coding: utf-8 -*- 
# @Time : 2022/3/2 20:32 
# @Author : crow
# @File : automatic_operation.py
import os
import time
from pathlib import Path

from func_timeout import func_set_timeout
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor
import queue

from common import constant
from config import log, driver_generator

driver = driver_generator.get_driver()
queue = queue.Queue(maxsize=10)
pool = ThreadPoolExecutor(max_workers=10)
TYPE = [By.ID, By.XPATH, By.NAME, By.CSS_SELECTOR]
loops = range(len(TYPE))
flag = True


def get_url(url):
    try:
        driver.get(url)
    except Exception as e:
        log.info(f"Get url: {url} failed.")
        raise e


def wait():
    driver.implicitly_wait(constant.ELEMENT_WAIT_TIME)


def findelement(t, v) -> WebElement:
    wait()
    result = WebDriverWait(driver, constant.ELEMENT_WAIT_TIME).until(EC.presence_of_element_located((t, v)))
    return result


def findelements(t, v) -> WebElement:
    wait()
    results = WebDriverWait(driver, constant.ELEMENT_WAIT_TIME).until(EC.presence_of_all_elements_located((t, v)))
    return results


@func_set_timeout(10)
def get_element(flag, loops, queue) -> WebElement:
    try:
        while flag:
            for i in loops:
                try:
                    result = queue.get(i).result()
                    if result is not None:
                        return result
                except Exception:
                    pass
    except Exception as e:
        raise e


def find_element(value) -> WebElement:
    try:
        for i in TYPE:
            future = pool.submit(findelement, i, value)
            queue.put(future)
        element = get_element(flag, loops, queue)
        return element
    except Exception as e:
        log.info(f"元素定位失败,{value}")
        raise e


def find_elements(value) -> WebElement:
    try:
        for i in TYPE:
            queue.put(pool.submit(findelements, i, value))
        elements = get_element(flag, loops, queue)
        return elements
    except Exception as e:
        log.info(f"元素定位失败,{value}")
        raise e


def screen_shot():
    # 执行屏幕截图操作
    try:
        scrpath = os.path.abspath('.') + '\\screenshot\\'
        if Path(scrpath).is_dir():  # 判断文件夹路径是否已经存在
            pass
        else:
            Path(scrpath).mkdir()  # 如果不存在，创建文件夹
        name = scrpath + time.strftime('%Y%m%d%H%M%S', time.localtime()) + '.png'
        driver.get_screenshot_as_file(name)
    except Exception as e:
        raise e


def quit_driver():
    driver.quit()
