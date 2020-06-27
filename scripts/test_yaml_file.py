import pytest

from read_yaml_file import GetData


class TestSum:
    path = GetData.get_data_from_yaml(GetData.BASE_PATH()+'/data/test_data.yaml')
    @pytest.mark.parametrize("a,b,c", path)
    def test_sum(self, a, b, c):
        """判断两个数之和 等于 第三个数"""
        print("\n{}+{}={}".format(a, b, c))
        assert a + b == c
