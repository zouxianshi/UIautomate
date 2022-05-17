import minium
import win32con
import win32gui
import time
from module.cfs.miniprogram.obj import index as idx
from common import win32


class AppTest(minium.MiniTest):

    def get_all_pages_path(self):
        win32.show_window("广西-患者端 - 微信开发者工具")

        self.app.redirect_to("/pages/home/home/index")
        self.page.get_element(idx.cxkp).click()
        self.page.get_element(idx.ssk).input("心血管")
        self.page.wait_for("rich-text[text(contains(\"测试患教资料\"))]")
        self.page.get_element("rich-text[text(contains(\"测试患教资料\"))]").click()
        self.app.go_home()
