import time

import pytest

from base.driver import Driver
from base.page import Page


class TestFontSize:
    @pytest.fixture(scope="class", autouse=True)
    def click_view_btn(self):
        Page.setting_page().click_view_btn()

    # @pytest.fixture(autouse=True)
    # def click_font_size(self):
    #     time.sleep(1)
    #     Page.view_page().click_font_size()

    def teardown_class(self):
        Driver.quit_app_driver()

    def test_font_size(self):
        # # 选择小字体
        # small_result = Page.view_page().get_choice_small_size_result()
        # # 断言小字体
        # assert "小" in small_result

        # 选择普通字体
        general_result = Page.view_page().get_choice_general_size_result()
        # 断言普通字体
        assert "普通" in general_result
        # # 选择大字体
        # big_result = Page.view_page().get_choice_big_size_result()
        # # 断言大字体
        # assert "大" in big_result

        # 选择特大字体
        sbig_result = Page.view_page().get_choice_super_big_size_result()
        # 断言特大字体
        assert "超大" in sbig_result
