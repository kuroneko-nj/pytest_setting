import allure


class TestSetup:
    @allure.severity(allure.severity_level.BLOCKER)  # 阻断性BUG(最严重)
    @allure.step(title="报告的步骤描述信息")
    def test_001(self):
        """添加测试步骤"""
        # 添加测试步骤的描述
        allure.attach("我是附件内容-用来记录步骤描述", "我是附件名字")

    @allure.severity(allure.severity_level.CRITICAL)  # 阻断性用例(比较重要的BUG)
    @allure.step(title="报告的步骤描述信息")
    def test_002(self):
        """添加测试步骤"""
        # 添加测试步骤的描述
        allure.attach("我是附件内容-用来记录步骤描述", "我是附件名字")
        assert False

    @allure.severity(allure.severity_level.NORMAL)  # 一般性用例
    @allure.step(title="报告的步骤描述信息")
    def test_003(self):
        """添加测试步骤"""
        # 添加测试步骤的描述
        allure.attach("我是附件内容-用来记录步骤描述", "我是附件名字")

    @allure.severity(allure.severity_level.MINOR)  # 比一般低一些的用例
    @allure.step(title="报告的步骤描述信息")
    def test_004(self):
        """添加测试步骤"""
        # 添加测试步骤的描述
        allure.attach("我是附件内容-用来记录步骤描述", "我是附件名字")

    @allure.severity(allure.severity_level.TRIVIAL)  # 可以忽略的用例
    @allure.step(title="报告的步骤描述信息")
    def test_005(self):
        """添加测试步骤"""
        # 添加测试步骤的描述
        allure.attach("我是附件内容-用来记录步骤描述", "我是附件名字")
