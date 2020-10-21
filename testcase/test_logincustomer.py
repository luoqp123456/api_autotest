# -- coding:utf8 --
import allure
import pytest
import sys
from commen.loggerhandler import log_case_info
from commen.operate_token import updatetoken
from commen.readexcel import *
from commen.send_request import *
sys.path.append('../..')

# @pytest.mark.usefixtures("do_login","get_excel")
# @pytest.mark.usefixtures("get_excel")
# @allure.severity("critical")               # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.feature("测试会员模块")           # 功能块，feature功能分块时比story大,即同时存在feature和story时,feature为父节点
# @allure.story("测试模块_demo2")             # 功能块，具有相同feature或story的用例将规整到相同模块下,执行时可用于筛选
# @allure.issue("BUG号：123")                 # 问题表识，关联标识已有的问题，可为一个url链接地址
# @allure.testcase("用例名：测试字符串相等")      # 用例标识，关联标识用例，可为一个url链接地址
class Testlogincustomer:
    excel_data = []
    token = []

    def logincustomer(self):
        case_data = get_test_data(self.excel_data, 'logincustomer')  # 从数据列表中查找到该用例数据
        # url = case_data.get('url')
        # data = case_data.get('data')
        # headers = case_data.get('headers')
        # method = case_data.get('method')
        # depend = case_data.get('depend')
        # dependdata = case_data.get('dependdata')
        updatetoken(self.token, case_data)
        res = send_request(case_data)
        assert case_data['expect_res'] == res["message"]
        log_case_info(case_data, res)
        # print(url, data, headers, method, depend, dependdata)


if __name__ == '__main__':   # 非必要，用于测试我们的代码
    pytest.main(['-s', 'test_logincustomer.py'])


    # name = case_data['case']
    # casename = case_data['casename']
    # url = case_data['url']  # 从字典中取数据，excel中的标题也必须是小写url
    # data = case_data['data']  # 注意字符串格式，需要用json.loads()转化为字典格式
    # expect_res = case_data['expect_res']  # 期望数据

    # {"name": "633", "contacts": [{"contactTypeId": 29, "name": "333dady", "phone": "15521222222"}],
    #  "birthday": "2017-06-21", "address": "", "gender": null, "eavAttributes": [], "icon": ""}
