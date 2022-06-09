import time
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

import page


class Base:
    # 初始化：实例化时需要传入driver
    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, loc, time_out=30, poll=0.5):
        """
        查找元素
        :param loc: 元祖类型的元素定位的信息
        :param time_out: 超时时间
        :param poll: 查找频率
        :return: 返回元素
        """
        return WebDriverWait(self.driver,
                             timeout=time_out,
                             poll_frequency=poll).until(lambda x:x.find_element(*loc))

    # 点击元素
    def base_click_element(self, loc):
        self.base_find_element(loc).click()

    # 输入内容
    def base_input_element(self, loc, value):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)

    # 获取文本内容
    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    # 截图
    def base_get_screen_shot(self):
        self.driver.get_screenshot_as_file("/tpshop/image/{}.png".format(time.strftime("%Y-%m-%d_%H_%M_%S")))

    def base_switch_frame(self, frame):
        """
        切换frame
        :param frame: 传入frame元素，根据元素进行切换
        """
        self.driver.switch_to.frame(frame)

    # 回到默认目录
    def base_switch_default_content(self):
        self.driver.switch_to.default_content()

    # 切换窗口
    def base_switch_window(self, title):
        self.driver.switch_to.window(self.base_get_handle_by_title(title))

    def base_get_handle_by_title(self, title):
        """
        根据传入的title获取窗口句柄
        :param title: 传入需要获取窗口句柄的title
        """
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if title == self.driver.title:
                return handle

    # 判断元素是否存在
    def base_is_exist_element(self, loc, timeout=3):
        try:
            self.base_find_element(loc,timeout)
            return True
        except NoSuchElementException:
            return False


    # 打开首页
    def base_back_home(self):
        sleep(3)
        self.driver.get(page.URL)

