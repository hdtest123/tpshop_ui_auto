import allure

import page
from base.base import Base
from base.get_driver import GetDriver


class PageOrder(Base):

    # 首页，点击我的购物车
    @allure.step(title="点击我的购物车按钮")
    def page_order_click_my_order(self):
        self.base_click_element(page.order_my_cart_btn)


    # 点击全选
    @allure.step(title="购物车页面，勾选全选复选框")
    def page_order_click_checkbox(self):
        if not self.base_find_element(page.order_checkbox_btn).is_selected():
            self.base_click_element(page.order_checkbox_btn)

    # 点击去结算
    @allure.step(title="点击去结算按钮")
    def page_order_go_to_account(self):
        self.base_click_element(page.order_go_to_account)

    # 点击提交订单(收货人加载慢)
    @allure.step(title="点击提交订单按钮")
    def page_order_submit_orders(self):
        self.base_find_element(page.order_receipt)
        self.base_click_element(page.order_submit_orders_btn)

    # 获取订单提交结果
    @allure.step(title="获取提交成功后提示信息")
    def page_get_order_submit_result(self):
        allure.attach("提示信息",self.base_get_text(page.order_submit_result), allure.attach_type.TEXT)
        return self.base_get_text(page.order_submit_result)

    # 回到首页
    @allure.step(title="回到首页")
    def page_order_back_home(self):
        self.base_back_home()

    # 截图
    @allure.step(title="断言错误时截图")
    def page_order_get_screen_shot(self):
        allure.attach("截图", GetDriver.get_driver().get_screenshot_as_png(), allure.attach_type.PNG)
        self.base_get_screen_shot()