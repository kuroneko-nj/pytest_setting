from appium import webdriver


class Driver:
    __app_driver = None

    @classmethod
    def get_app_driver(cls):
        """获取app_driver"""
        if cls.__app_driver is None:
            disired_caps = {
                "platformName": "Android",
                "platformVersion": "5.1",
                "deviceName": "samsung",
                "appPackage": "com.android.settings",
                "appActivity": ".Settings"
            }
            cls.__app_driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", disired_caps)
        return cls.__app_driver

    @classmethod
    def quit_app_driver(cls):
        """关闭并重置app_driver"""
        if cls.__app_driver:
            cls.__app_driver.quit()
            cls.__app_driver = None
