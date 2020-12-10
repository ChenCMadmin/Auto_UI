from selenium.webdriver.common.by import By
from common.base import BasePage
from selenium import webdriver
from config.setting_path import yaml_local_path
from common.get_yaml import Get_yaml_data

file_path = yaml_local_path + "/" + "Login_local_data.yaml"
# 定位元素方法库
Testdata = Get_yaml_data(file_path)

# 登录操作的类
class LoginPage(BasePage):
    # 账号
    account_box = (By.ID, Testdata.get_element(0))
    # 密码
    password_box = (By.ID, Testdata.get_element(1))
    # 登录按钮
    click_btn = (By.ID, Testdata.get_element(2))
    # 密码错误文本内容
    error_pwd = (By.CLASS_NAME,Testdata.get_element(3))
    # 登录成功后个人账户
    account_num = (By.CLASS_NAME,Testdata.get_element(4))
    # 退出登录按钮
    logout_btn = (By.ID,Testdata.get_element(5))

    # 打开浏览器
    def login_index(self):
        self.open_browser()
    # 输入账号
    def input_account(self,account):
        self.send_key(self.account_box,account)
    # 输入密码
    def input_pwd(self,password):
        self.send_key(self.password_box,password)
    # 点击登录按钮
    def click_login_btn(self):
        self.click(self.click_btn)
    #检查提示信息
    def check_error_text(self):
        return self.get_text(self.error_pwd)
    # 获取账号信息
    def get_account_num(self):
        return self.get_text(self.account_num)
    # 退出登录
    def click_logout_btn(self):
        self.click(self.logout_btn)

if __name__ == "__main__":
    a = LoginPage(webdriver.Chrome(),"https://account.xiaomi.com/pass/serviceLogin")
    a.login_index()
    a.input_account("15599082962")
    a.input_pwd("19971212hzj")
    a.click_login_btn()
    # time.sleep(3)
    a.get_account_num()
    print(a.get_account_num())
    a.click_logout_btn()
