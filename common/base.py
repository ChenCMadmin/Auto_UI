from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.Log import Get_log
from config.setting_path import screen_path
from selenium.common.exceptions import TimeoutException
import time


# 公用的基础操作类
class BasePage(object):
    # 构造函数里面的参数就是类的所有参数
    def __init__(self,driver,url):
        self.driver = driver
        self.url = url
        self.log = Get_log()

    # 打开对应的网页
    def open_browser(self):
        self.driver.get(self.url)

    #查找元素，传入方法和元素两个参数
    def wait_element(self,ele):
        try:
            WebDriverWait(self.driver,5,0.5).until(EC.visibility_of_element_located(ele))
            return True
        except TimeoutException:
            self.log.log_error("没有定位到元素{0}".format(ele))
            return False
        except Exception as e:
            raise e

    def find_ele(self, ele):
        if self.wait_element(ele):
            try:
                return self.driver.find_element(*ele)
            except Exception as e:
                raise e
        else:
            self.log.log_error("没有定位到元素")
            return False
    # 点击定位的元素
    def click(self,div_click):
        self.find_ele(div_click).click()

    # 输入内容
    def send_key(self,div,data):
        self.find_ele(div).send_keys(data)

    # 获取定位元素文本内容
    def get_text(self,ele):
        return self.find_ele(ele).text

    # 获取当前网页url地址
    def get_curr_url(self):
        url = self.driver.current_url
        return url

    # 截图
    def get_screen_shot(self):
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        file_name = screen_path + '\\' + current_time + '.png'
        self.driver.get_screenshot_as_file(file_name)
        self.driver.save_screenshot(file_name)