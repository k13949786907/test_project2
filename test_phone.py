import pytest
import time
from base.base_action import init_driver
from page.page import Page

class TestPhone:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
    def teardown(self):
        time.sleep(3)
        self.driver.quit()
    @pytest.mark.parametrize(("name","phone"),[("zhangsan","18888888888"),("lisi","15555555555"),("wangwu","13333333333")])
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_phone(self,name,phone):
        self.page.phone_list_page.click_phone_list()
        self.page.new_phone_page.input_new_name(name)
        self.page.new_phone_page.input_new_phone(phone)

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_login1(self):
        assert 0

    def test_login2(self):
        assert 1

    def test_login3(self):
        assert 0

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_login4(self):
        assert 1


