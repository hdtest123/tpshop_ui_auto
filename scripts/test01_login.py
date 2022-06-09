import pytest

import page
from base.analyze_yaml import analyze_yaml

from base.get_driver import GetDriver

from page.page_login import PageLogin



class TestLogin:

    def setup_class(self):
        # 初始化page_login对象
        self.page_login = PageLogin(GetDriver.get_driver())

        # 点击首页登录链接
        self.page_login.page_click_login_link()

    # analyze_yaml返回的数据是列表中嵌套字段的格式，如[{},{}]
    @pytest.mark.parametrize("args", analyze_yaml("login_data.yaml", "test_login"))
    def test_login(self, args):
        # 输入用户名
        self.page_login.page_input_username(args["username"])
        # 输入密码
        self.page_login.page_input_password(args["password"])
        # 输入验证码
        self.page_login.page_input_verify_code(args["verify_code"])
        # 点击登录按钮
        self.page_login.page_click_login_button()

        # 如果是正向用例，判断安全退出是否存在，进行断言
        if args["status"] == "true":
            try:
                assert self.page_login.page_is_exist_element(page.login_out_link)
            except AssertionError as e:
                print(e)
                self.page_login.page_get_screen_shot()
            self.page_login.page_click_login_out()
            self.page_login.page_click_login_link()

        # 如果是逆向用例，获取错误信息，进行断言
        if args["status"] == "false":
            try:
                assert  args["except_result"] == self.page_login.page_get_error_info()
            except AssertionError as e:
                print(e)
                self.page_login.page_get_screen_shot()
            self.page_login.page_click_alert_window_ok_btn()

    def teardown_class(self):
        GetDriver.driver_quit()
