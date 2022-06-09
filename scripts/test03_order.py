from base.get_driver import GetDriver
from page.page_login import PageLogin
from page.page_order import PageOrder


class TestOrder:
    def setup_class(self):
        # 实例化page_loing对象,依赖其登录成功方法
        PageLogin(GetDriver.get_driver()).page_login_success()
        self.page_order = PageOrder(GetDriver.get_driver())
        # 回到首页
        self.page_order.page_order_back_home()

    def test_order(self):
        # 首页，点击我的订单
        self.page_order.page_order_click_my_order()
        # 点击全选按钮
        self.page_order.page_order_click_checkbox()
        # 点击去结算
        self.page_order.page_order_go_to_account()
        # 点击提交订单
        self.page_order.page_order_submit_orders()
        # 提交成功，获取结果，进行断言
        msg = self.page_order.page_get_order_submit_result()
        try:
            assert msg == "订单提交成功，请您尽快付款！"
        except AssertionError as e:
            print(e)
            self.page_order.page_order_get_screen_shot()

    def teardown_class(self):
        GetDriver.driver_quit()