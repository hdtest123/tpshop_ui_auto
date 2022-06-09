import allure

import page
from base.base import Base
from base.get_driver import GetDriver


class PageLogin(Base):
    # 点击登录链接，进入登录页面
    @allure.step(title= "点击登录链接")
    def page_click_login_link(self):
        self.base_click_element(page.login_link)

    # 输入用户名
    @allure.step(title="输入用户名")
    def page_input_username(self, username):
        allure.attach("用户名", username, allure.attach_type.TEXT)
        self.base_input_element(page.login_username, username)

    # 输入密码
    @allure.step(title="输入密码")
    def page_input_password(self, password):
        allure.attach("密码", password, allure.attach_type.TEXT)
        self.base_input_element(page.login_password, password)

    # 输入验证码
    @allure.step(title="输入验证码")
    def page_input_verify_code(self, verify_code):
        allure.attach("验证码", verify_code, allure.attach_type.TEXT)
        self.base_input_element(page.login_verify_code, verify_code)

    # 点击登录按钮
    @allure.step(title="点击登录按钮")
    def page_click_login_button(self):
        self.base_click_element(page.login_button)

    # 点击安全退出
    @allure.step(title="点击安全退出链接")
    def page_click_login_out(self):
        self.base_click_element(page.login_out_link)

    # 获取错误信息
    @allure.step(title="获取错误提示信息")
    def page_get_error_info(self):
        allure.attach("错误提示信息",self.base_get_text(page.login_alert_window), allure.attach_type.TEXT)
        return self.base_get_text(page.login_alert_window)

    # 点击提示框的确定按钮
    @allure.step(title="点击错误提示框的确定按钮")
    def page_click_alert_window_ok_btn(self):
        self.base_click_element(page.login_alert_window_OK_btn)

    # 截图
    @allure.step(title="断言错误时截图")
    def page_get_screen_shot(self):
        allure.attach("截图",GetDriver.get_driver().get_screenshot_as_png(),allure.attach_type.PNG)
        self.base_get_screen_shot()

    # 判断元素是否存在
    @allure.step(title="查找元素是否存在")
    def page_is_exist_element(self, loc):
        return self.base_is_exist_element(loc)

    # 登录成功的方法，给购物车、下单、支付模块使用，因为这几个模块需要依赖登录成功
    @allure.step(title="登录成功")
    def page_login_success(self):
        self.page_click_login_link()
        self.page_input_username("13288888888")
        self.page_input_password("admin1234")
        self.page_input_verify_code("8888")
        self.page_click_login_button()