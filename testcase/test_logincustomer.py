# -- coding:utf8 --
import allure
import pytest
import sys
from commen.operate_logger import log_case_info
from commen.operatr_assert import assert_in_text
from commen.readexcel import *
from commen.send_request import *
from page.student_page import StudentPage

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

    def test_logincustomer(self, get_session):
        case_data = get_test_data(self.excel_data, 'logincustomer')  # 从数据列表中查找到该用例数据
        res = send_request(get_session,case_data)
        assert case_data['expect_res'] == res["message"]
        assert_in_text(res, case_data['expect_res'])
        log_case_info(case_data, res)





if __name__ == '__main__':   # 非必要，用于测试我们的代码
    pytest.main(['-s', 'test_logincustomer.py'])

