import os
import yaml


class GetData:
    @classmethod
    def get_data_from_yaml(cls, path):
        # 打开文件
        with open(path, encoding="utf-8")as f:
            # 读取文件
            data_list = []
            data_dict = yaml.safe_load(f).values()
            # 调整文件格式
            for i in data_dict:
                data_list.append(tuple(i.values()))
        return data_list

    @classmethod
    def BASE_PATH(cls):
        return os.path.abspath(os.path.dirname(__file__))


if __name__ == '__main__':
    GetData.get_data_from_yaml(GetData.BASE_PATH() + "/data/test_data.yaml")
