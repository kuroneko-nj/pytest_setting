from selenium.webdriver.common.by import By


class PageEle:
    """管理页面元素"""
    # ---设置页面---
    # 搜索按钮
    search_btn_id = By.ID, 'com.android.settings:id/search'
    # 显示按钮
    view_btn_xpath = By.XPATH, '//*[contains(@text,"显示")]'
    # ---搜索界面---
    # 搜索输入框
    search_input_id = By.ID, 'android:id/search_src_text'
    # 搜索的结果
    search_result_id = By.ID, 'com.android.settings:id/title'
    # ---显示界面---
    # 字体大小按钮
    font_size_btn_xpath = By.XPATH, '//*[contains(@text,"字体大小")]'
    # 字体大小选项-小
    font_size_small_xpath = By.XPATH, "//*[contains(@text,'小')]"
    # 字体大小选项-普通
    font_size_general_xpath = By.XPATH, "//*[contains(@text,'普通')]"
    # 字体大小选项-大
    font_size_big_xpath = By.XPATH, "//*[contains(@text,'大')]"
    # 字体大小选项-普通
    font_size_super_big_xpath = By.XPATH, "//*[contains(@text,'超大')]"
    # 显示界面的描述信息
    view_summary_id = By.ID, 'android:id/summary'
