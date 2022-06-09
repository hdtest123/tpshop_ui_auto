import pytest


from base.analyze_yaml import analyze_yaml
from base.get_driver import GetDriver
from page.page_cart import PageCart
from page.page_login import PageLogin


class TestCart:

    def setup_class(self):
        # 实例化page对象
        self.page_login = PageLogin( GetDriver.get_driver())
        self.page_cart = PageCart(GetDriver.get_driver())
        # 依赖登录成功
        self.page_login.page_login_success()
        self.page_cart.page_index()

    @pytest.mark.parametrize("args", analyze_yaml("cart_data.yaml", "test_cart"))
    def test_cart(self, args):
        # 输入搜索内容
        self.page_cart.page_input_search_content(args["prduct_name"])
        # 点击搜索按钮
        self.page_cart.page_click_search_btn()
        # 点击添加购物车
        self.page_cart.page_click_add_cart()
        # 点击添加购物车，进入详情页面
        self.page_cart.page_click_add_to_cart()
        # 添加成功，获取信息，进行断言
        success_msg =  self.page_cart.page_get_add_success_info()
        try:
            assert success_msg == "添加成功"
        except AssertionError as e:
            print(e)
            self.page_cart.page_cart_get_screen_shot()
        # 关闭提示窗口
        self.page_cart.page_back_default_content_close_window()

    # 关闭驱动对象
    def teardown_class(self):
        GetDriver.driver_quit()