import allure

import page
from base.base import Base
from base.get_driver import GetDriver


class PagePay(Base):

    # 点击我的订单
    @allure.step(title="点击我的订单")
    def page_pay_click_my_pay(self):
        self.base_click_element(page.pay_my_orders_btn)

    # 切换窗口点击立即支付
    @allure.step(title="切换窗口，点击立即支付按钮")
    def page_pay_click_now_pay(self):
        self.base_switch_window(page.pay_my_order_title)
        self.base_click_element(page.pay_now_pay)

    # 切换窗口选择货到付款
    @allure.step(title="切换窗口，选择付款方式")
    def page_pay_select_pay_method(self):
        self.base_switch_window(page.pay_order_pay_title)
        allure.attach("付款方式：","货到付款", allure.attach_type.TEXT)
        self.base_click_element(page.pay_method)

    # 点击确认支付方式
    @allure.step(title="点击确认支付按钮")
    def page_pay_click_confirm_pay_method(self):
        self.base_click_element(page.pay_confirm_pay_method)

    # 获取支付成功信息(订单提交成功，我们将在第一时间给你发货！)
    @allure.step(title="支付成功，获取提示信息")
    def page_pay_get_pay_success_info(self):
        allure.attach("提示信息：",self.base_get_text(page.pay_success_info), allure.attach_type.TEXT)
        return self.base_get_text(page.pay_success_info)

    # 截图
    @allure.step(title="断言错误时截图")
    def page_pay_get_screen_shot(self):
        allure.attach("截图", GetDriver.get_driver().get_screenshot_as_png(), allure.attach_type.PNG)
        self.base_get_screen_shot()

    # 回到首页
    @allure.step(title="回到首页")
    def page_pay_back_home(self):
        self.base_back_home()