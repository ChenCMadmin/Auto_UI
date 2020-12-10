import pytest,sys
sys.path.append('../')
from common.driver import driver
from page_obj.login_obj import LoginPage
from common.get_config import Get_config


@pytest.fixture(scope="function")
def open_baidu():
    selenium_driver = driver()
    url = Get_config().read_config("URL", "test_url")
    baidu = LoginPage(selenium_driver,url)
    yield baidu
    selenium_driver.quit()
