from base.base import Base
from page.page_ele import PageEle


class SettingPage(Base):
    def __init__(self):
        super().__init__()

    def click_search_btn(self):
        """点击搜索按钮"""
        self.click_ele(PageEle.search_btn_id)

    def click_view_btn(self):
        """点击显示按钮"""
        self.click_ele(PageEle.view_btn_xpath)
