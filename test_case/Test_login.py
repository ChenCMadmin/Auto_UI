import pytest,sys,allure
# 把项目运行目录添加到path中，不加的话在terminal上运行会报错
sys.path.append('../')
from common.get_yaml import Get_yaml_data
from config.setting_path import case_data
from common.Log import Get_log



login_case_path = case_data + "/" + "Login_data.yaml"
login_case = Get_yaml_data(login_case_path).get_all_data()

# 登录用例的封装
@allure.feature("测试用例运行")
class Test_CaseRun():
    # 测试步骤
    @allure.story("测试登录")
    @allure.title("登录用例")
    @pytest.mark.parametrize("case_data",login_case)
    def test_search(self,case_data,open_baidu):
        log = Get_log()
        # 打开登录页面
        open_baidu.login_index()
        log.log_info("执行用例:{0}".format(case_data["id"]))
        if case_data["status"] == "login_success":
            open_baidu.input_account(case_data["data"]["account"])
            open_baidu.input_pwd(case_data["data"]["pwd"])
            open_baidu.click_login_btn()
            account_num = open_baidu.get_account_num()
            try:
                assert account_num == case_data["check"][0]
                log.log_info("登录成功")
                log.log_info("用例: {0}成功运行".format(case_data["id"]))
                # 退出登录状态
                open_baidu.click_logout_btn()
            except Exception as e:
                log.log_error("登录失败,原因{0}".format(e))
                log.log_error("用例: {0}运行失败".format(case_data["id"]))
                open_baidu.get_screen_shot()
                raise e
        else:
            open_baidu.input_account(case_data["data"]["account"])
            open_baidu.input_pwd(case_data["data"]["pwd"])
            open_baidu.click_login_btn()
            # 获取登录失败时的提示文本信息
            error_text = open_baidu.check_error_text()
            try:
                assert error_text == case_data["check"][0]
                log.log_info("断言成功")
                log.log_info("用例: {0}成功运行".format(case_data["id"]))
            except Exception as e:
                log.log_error("{0}与{1}不一致".format(error_text,case_data["check"][0]))
                log.log_error("用例: {0}运行失败".format(case_data["id"]))
                # 断言失败时进行截图操作
                open_baidu.get_screen_shot()
                raise e


if __name__ == "__main__":
    pytest.main()

    # 生成allure.josn文件
    # pytest.main(['-s', '--alluredir','../report/tmp/'])
    # 生成html文件
    # os.system("allure generate ../report/tmp -o ../report/allure_result --clean")