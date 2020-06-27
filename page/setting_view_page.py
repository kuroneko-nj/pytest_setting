import time

from base.base import Base
from page.page_ele import PageEle


class ViewPage(Base):
    def __init__(self):
        super().__init__()

    # def click_font_size(self):
    #     self.click_ele(PageEle.font_size_btn_xpath)

    def get_choice_small_size_result(self):
        """点击小字体,返回显示页面修改之后的描述信息"""
        self.click_ele(PageEle.font_size_btn_xpath)
        time.sleep(1)
        self.click_ele(PageEle.font_size_small_xpath)
        result_list = self.find_eles(PageEle.view_summary_id)
        return [i.text for i in result_list]

    def get_choice_general_size_result(self):
        """点击普通字体,返回显示页面修改之后的描述信息"""
        self.click_ele(PageEle.font_size_btn_xpath)
        time.sleep(1)
        self.click_ele(PageEle.font_size_general_xpath)
        time.sleep(1)
        result_list = self.find_eles(PageEle.view_summary_id)
        return [i.text for i in result_list]

    def get_choice_big_size_result(self):
        """点击大字体,返回显示页面修改之后的描述信息"""
        self.click_ele(PageEle.font_size_btn_xpath)
        time.sleep(1)
        self.click_ele(PageEle.font_size_big_xpath)
        time.sleep(1)
        result_list = self.find_eles(PageEle.view_summary_id)
        return [i.text for i in result_list]

    def get_choice_super_big_size_result(self):
        """点击超大字体,返回显示页面修改之后的描述信息"""
        self.click_ele(PageEle.font_size_btn_xpath)
        time.sleep(1)
        self.click_ele(PageEle.font_size_super_big_xpath)
        time.sleep(1)
        result_list = self.find_eles(PageEle.view_summary_id)
        return [i.text for i in result_list]
