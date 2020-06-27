from selenium.webdriver.support.wait import WebDriverWait

from base.driver import Driver


class Base:
    def __init__(self):
        self.driver = Driver.get_app_driver()

    def find_ele(self, loc, timeout=5, poll_frequency=0.5):
        """
        定位单个元素
        :param loc: (By.ID,id_value)
        :param timeout: 超时时间 默认值5s
        :param poll_frequency: 搜索元素间隔,默认值0.5s
        :return:查到到的元素对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def find_eles(self, loc, timeout=5, poll_frequency=0.5):
        """
        定位多个元素
        :param loc: (By.ID,id_value)
        :param timeout: 超时时间 默认值5s
        :param poll_frequency: 搜索元素间隔,默认值0.5s
        :return:查到到的元素对象列表
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_ele(self, loc, timeout=5, poll_frequency=0.5):
        """
        点击元素
        :param loc: (By.ID,id_value)
        :param timeout: 超时时间 默认值5s
        :param poll_frequency: 搜索元素间隔,默认值0.5s
        """
        self.find_ele(loc, timeout, poll_frequency).click()

    def send_ele(self, loc, send_text, timeout=5, poll_frequency=0.5):
        """
        输入方法
        :param loc: (By.ID,id_value)
        :param send_text: 输入的文本内容
        :param timeout: 超时时间 默认值5s
        :param poll_frequency: 搜索元素间隔,默认值0.5s
        """
        input_ele = self.find_ele(loc, timeout, poll_frequency)
        input_ele.clear()
        input_ele.send_keys(send_text)
