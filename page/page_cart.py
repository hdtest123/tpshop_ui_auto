import allure

import page
from base.base import Base
from base.get_driver import GetDriver


class PageCart(Base):
    # 打开首页
    @allure.step(title="打开首页")
    def page_index(self):
        self.base_back_home()

    # 输入搜索内容：小米手机
    @allure.step(title="搜索框中输入内容")
    def page_input_search_content(self,value):
        allure.attach("搜索商品", value, allure.attach_type.TEXT)
        self.base_input_element(page.cart_search, value)

    # 点击搜索
    @allure.step(title="点击搜索按钮")
    def page_click_search_btn(self):
        self.base_click_element(page.cart_search_btn)

    # 点击添加购物车
    @allure.step(title="点击添加购物车，进入详情页面")
    def page_click_add_cart(self):
        self.base_click_element(page.cart_add_btn)

    # 点击添加购物车详情
    @allure.step(title="点击添加按钮，添加到购物车")
    def page_click_add_to_cart(self):
        self.base_click_element(page.cart_add_to_cart_btn)

    # 切换frame,获取结果
    @allure.step(title="添加成功获取结果，弹出提示框")
    def page_get_add_success_info(self):
        self.base_switch_frame(self.base_find_element(page.cart_frame))
        allure.attach("提示框中的信息",self.base_get_text(page.cart_add_success_info), allure.attach_type.TEXT)
        return self.base_get_text(page.cart_add_success_info)

    # 回到默认目录，关闭窗口
    @allure.step(title="点击提示框中的关闭窗口")
    def page_back_default_content_close_window(self):
        self.base_switch_default_content()
        self.base_click_element(page.cart_close_window)

    # 截图
    @allure.step(title="断言错误时截图")
    def page_cart_get_screen_shot(self):
        allure.attach("截图", GetDriver.get_driver().get_screenshot_as_png(), allure.attach_type.PNG)
        self.base_get_screen_shot()
