from commen.poerate_config import Config
from commen.readexcel import excel_to_list


class EnvMember:
    # conf = Config()

    def set_excel_Sheet1(self):
        excel_data = excel_to_list(r"C:\Users\Administrator\PycharmProjects\pytest\data\ceshi.xls", "Sheet1")
        return excel_data

    def set_excel_Sheet3(self):
        excel_data = excel_to_list(r"C:\Users\Administrator\PycharmProjects\pytest\data\ceshi.xls", "Sheet3")
        return excel_data
    # def test_env(self):
    #     ip_url = self.conf.get_conf('environment', 'test_env')
    #     return ip_url
    #
    # def dev_env(self):
    #     ip_url = self.conf.get_conf('environment', 'dev_env')
    #     return ip_url


