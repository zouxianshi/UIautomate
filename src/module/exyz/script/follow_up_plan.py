# -*- coding: utf-8 -*- 
# @Time : 2022/3/14 18:10 
# @Author : crow
# @File : follow_up_plan.py
import time
import unittest

from selenium.webdriver import Keys
from src.module.exyz.obj import mainpage_obj as mpo, template_obj as to, follow_up_plan_obj as tno
from src.common import automatic_operation as ao
from config import log


# 新增随访计划
def follow_up_plan_add():
    log.info("新建随访计划开始")
    try:
        # 点击专业设置
        ao.find_element(mpo.zysz).click()
        # 点击随访计划
        ao.find_element(mpo.sfjh).click()
        # 点击新建
        ao.find_element(to.xinjian_xpath).click()
        # 输入随访计划名称
        ao.find_element(tno.sfmc).sendKeys("测试随访计划")
        # 选择科室
        ao.find_element(tno.ssks).click()
        ao.find_element(tno.ksyjxx).click()
        ao.find_element(tno.ksejxx).click()
        # 病种选择
        ao.find_element(tno.ssbz).click()
        ao.find_element(tno.bzyjxx).click()
        # 随访时间
        ao.find_element(tno.sfsj).click()
        ao.find_element(tno.sfsj).sendKeys("5")
        ao.find_element(tno.sfsjdw).click()
        ao.find_element(tno.t).click()
        # 随访方式
        ao.find_element(tno.wxsf).click()
        ao.find_element(tno.dxsf).click()
        ao.find_element(tno.dhsf).click()
        # 复诊计划
        ao.find_element(tno.fzjh_select).click()
        ao.find_element(tno.fzjh_input).click()
        ao.find_element(tno.fzjh_input).clear()
        ao.find_element(tno.fzjh_input).sendKeys(Keys.CONTROL, "a")
        ao.find_element(tno.fzjh_input).sendKeys("请于3天后来我院复诊")
        ao.find_element(tno.tqyy_input).click()
        ao.find_element(tno.tqyy_input).sendKeys(Keys.CONTROL, "a")
        ao.find_element(tno.tqyy_input).sendKeys("3")
        # 用药提醒
        ao.find_element(tno.yytx_select).click()
        ao.find_element(tno.yytx_input).sendKeys(Keys.CONTROL, "a")
        ao.find_element(tno.yytx_input).sendKeys("请及时吃药")
        # 患教资料
        ao.find_element(tno.hjzl_select).click()
        ao.find_element(tno.hjzl_add).click()
        ao.find_element(tno.hjzlbd_add).click()
        # 问诊表
        ao.find_element(tno.wzb_select).click()
        ao.find_element(tno.wzb_add).click()
        ao.find_element(tno.wzbbd_add).click()
        # 保存
        ao.find_element(tno.bc).click()
        ao.find_element(tno.BC).click()
        log.info("新建随访计划结束")

    except Exception as e:
        log.info(e)
