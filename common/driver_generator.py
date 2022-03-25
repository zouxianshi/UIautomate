import platform

from selenium import webdriver
from common import constant
from config import log


def get_driver(dirver_type="chrome"):
    log.info("Chrome driver start begin.")
    global DRIVER_PATH, driver
    if dirver_type == "chrome":
        options = webdriver.ChromeOptions()
        if platform.uname().system.__contains__("Windows"):
            DRIVER_PATH = constant.DRIVER_PATH_WIN
        elif platform.uname().system.__contains__("Linux"):
            DRIVER_PATH = constant.DRIVER_PATH_LINUX
        # 设置Chrome静默模式
        # options.add_argument(constant.CHROME_SILENCE_MODE)
        # 最大化窗口
        options.add_argument(constant.CHROME_MAX_WINDOW)
        # 设置忽略并能正常打开不安全的页面
        options.accept_insecure_certs = True
        # 自定义浏览器窗口大小
        # options.add_argument('window-size=300,600')
        driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
        log.info("Chrome driver start end.")
    elif dirver_type == "firefox":
        print("没做")
    return driver


def quit_driver():
    log.info("Chrome driver quit.")
    driver.quit()

#
#
#     /**
#      * @author zouxianshi
#      * @description 获退出ChromeDriver
#      * @date 2020/7/20
#      */
#     public static void quitDriver(WebDriver driver){
#         try {
#             log.info("Chrome driver quit.");
#             driver.quit();
#         } catch (Exception e) {
#             log.error("Chrome driver quit failed.", e);
#         }
#     }

# if __name__ == "__main__":
#     getDriver()
