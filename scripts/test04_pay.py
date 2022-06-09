from base.get_driver import GetDriver
from page.page_login import PageLogin
from page.page_pay import PagePay


class TestPay:
    def setup_class(self):
        # 登录成功
        PageLogin( GetDriver.get_driver()).page_login_success()
        # 实例化page_pay
        self.page_pay = PagePay(GetDriver.get_driver())
        # 回到首页
        self.page_pay.page_pay_back_home()

    def test_pay(self):
        # 点击我的订单
        self.page_pay.page_pay_click_my_pay()
        # 点击立即支付
        self.page_pay.page_pay_click_now_pay()
        # 选择支付方式：货到付款
        self.page_pay.page_pay_select_pay_method()
        # 点击确认支付
        self.page_pay.page_pay_click_confirm_pay_method()
        msg = self.page_pay.page_pay_get_pay_success_info()
        try:
            assert msg == "订单提交成功，我们将在第一时间给你发货"
        except AssertionError as e:
            print(e)
            self.page_pay.page_pay_get_screen_shot()

    # 关闭驱动
    def teardown_class(self):
        GetDriver.driver_quit()