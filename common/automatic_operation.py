# -*- coding: utf-8 -*- 
# @Time : 2022/3/2 20:32 
# @Author : crow
# @File : automatic_operation.py
from time import sleep

import func_timeout
from func_timeout import func_set_timeout
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor, wait
import queue

from common import driver_generator, constant
from config import log

driver = driver_generator.get_driver()
queue = queue.Queue(maxsize=10)
pool = ThreadPoolExecutor(max_workers=10)
TYPE = (By.ID, By.XPATH)
loops = range(len(TYPE))
flag = True


def get_url(url):
    try:
        driver.get(url)
    except Exception as e:
        log.info(f"Get url: {url} failed." + e)


def wait():
    driver.implicitly_wait(constant.ELEMENT_WAIT_TIME)


def findelement(t, v):
    wait()
    result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((t, v)))
    return result


def findelements(t, v):
    wait()
    results = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((t, v)))
    return results


@func_set_timeout(5)
def get_element(flag, loops, queue):
    try:
        while flag:
            for i in loops:
                if queue.get(i) is None:
                    sleep(0.5)
                else:
                    return queue.get(i).result()
    except func_timeout.exceptions.FunctionTimedOut as e:
        log.info("元素定位超时")
        raise e


def find_element(value) -> WebElement:
    try:
        for i in TYPE:
            future = pool.submit(findelement, i, value)
            queue.put(future)
        element = get_element(flag, loops, queue)
        return element
    except Exception as e:
        log.info(f"元素定位失败,{value}\r\n{e}")


def find_elements(value):
    try:
        for i in TYPE:
            future = pool.submit(findelements, i, value)
            queue.put(future)
        elements = get_element(flag, loops, queue)
        return elements
    except Exception as e:
        log.info(f"元素定位失败,{value}\r\n{e}")
