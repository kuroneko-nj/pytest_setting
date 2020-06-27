from base.base import Base
from page.page_ele import PageEle


class SearchPage(Base):
    def __init__(self):
        super().__init__()

    def send_search(self, send_text):
        """
        输入信息
        :param send_text: 要搜索的内容
        :return:
        """
        self.send_ele(PageEle.search_input_id, send_text)

    def get_search_result(self):
        """
        获取搜索到的文本信息列表
        :return:
        """
        result = self.find_eles(PageEle.search_result_id)
        return [i.text for i in result]
