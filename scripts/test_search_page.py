import pytest

from base.driver import Driver
from base.page import Page


class TestSearchPage:
    @pytest.fixture(scope='class', autouse=True)
    def click_search(self):
        Page.setting_page().click_search_btn()

    def teardown_class(self):
        Driver.quit_app_driver()

    @pytest.mark.parametrize('search_text,result_text', [("1", "休眠"), ("i", "IP地址"), ("m", "MAC地址")])
    def test_search_page(self, search_text, result_text):
        """
        搜索内容测试方法
        :param search_text: 搜索内容
        :param result_text: 搜索的结果
        """
        Page.search_page().send_search(search_text)
        assert result_text in Page.search_page().get_search_result()
