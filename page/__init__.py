from selenium.webdriver.common.by import By


""" 以下项目地址信息"""
URL = "http://localhost:9090/index.php"


""" 以下是登录页面的配置数据"""
login_link = By.PARTIAL_LINK_TEXT, "登录"
login_username = By.CSS_SELECTOR, "#username"
login_password = By.CSS_SELECTOR, "#password"
login_verify_code = By.CSS_SELECTOR, "#verify_code"
login_button = By.CSS_SELECTOR, ".J-login-submit"
login_alert_window = By.CSS_SELECTOR, ".layui-layer-content"
login_out_link = By.PARTIAL_LINK_TEXT, "安全退出"
login_alert_window_OK_btn = By.CSS_SELECTOR, ".layui-layer-btn0"


"""  以下是购物车页面的配置数据 """
cart_search =By.CSS_SELECTOR,"#q"
cart_search_btn =By.CSS_SELECTOR, ".ecsc-search-button"
cart_add_btn =By.CSS_SELECTOR, ".p-btn>a"
cart_add_to_cart_btn =By.CSS_SELECTOR, "#join_cart"
cart_frame=By.CSS_SELECTOR, "#layui-layer-iframe1"
cart_add_success_info =By.CSS_SELECTOR,".conect-title>span"
cart_close_window =By.CSS_SELECTOR, ".layui-layer-close1"


"""  以下是订单页面的配置数据 """
order_my_cart_btn = By.CSS_SELECTOR, ".c-n"
order_checkbox_btn = By.CSS_SELECTOR, ".checkCartAll"
order_go_to_account = By.CSS_SELECTOR, ".gwc-qjs"
order_receipt = By.CSS_SELECTOR, ".consignee>b"
order_submit_orders_btn = By.CSS_SELECTOR, ".Sub-orders"
order_submit_result = By.CSS_SELECTOR, ".erhuh>h3"


"""  以下是支付页面的配置数据 """
pay_my_orders_btn = By.PARTIAL_LINK_TEXT, "我的订单"
pay_my_order_title= "我的订单"
pay_now_pay = By.PARTIAL_LINK_TEXT, "立即支付"
pay_order_pay_title = "订单支付-开源商城 | B2C商城 | B2B2C商城 | 三级分销 | 免费商城 | 多用户商城 | tpshop｜thinkphp shop｜TPshop 免费开源系统 | 微商城"
pay_method =By.CSS_SELECTOR, "[src='/plugins/payment/cod/logo.jpg']"
pay_confirm_pay_method =By.CSS_SELECTOR,".button-confirm-payment"
pay_success_info=By.CSS_SELECTOR, ".erhuh>h3"