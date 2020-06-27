from page.search_page import SearchPage
from page.setting_page import SettingPage
from page.setting_view_page import ViewPage


class Page:
    @classmethod
    def setting_page(cls):
        return SettingPage()

    @classmethod
    def search_page(cls):
        return SearchPage()

    @classmethod
    def view_page(cls):
        return ViewPage()
