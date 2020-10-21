import allure
import pytest
import sys
from commen.loggerhandler import log_case_info
from commen.readexcel import get_test_data
from commen.send_request import send_request
sys.path.append('../..')


@allure.severity("critical")               # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.feature("测试登录模块")           # 功能块，feature功能分块时比story大,即同时存在feature和story时,feature为父节点
# @allure.story("测试模块_demo2")             # 功能块，具有相同feature或story的用例将规整到相同模块下,执行时可用于筛选
# @allure.issue("BUG号：123")                 # 问题表识，关联标识已有的问题，可为一个url链接地址
# @allure.testcase("用例名：登录")      # 用例标识，关联标识用例，可为一个url链接地址

# @pytest.mark.usefixtures("do_login","get_excel")
class TestLogin:
    excel_data = []
    @allure.testcase("/basic/auth/login")
    @allure.story("测试登录密码错误")  # 功能块，具有相同feature或story的用例将规整到相同模块下,执行时可用于筛选
    # 登录失败，用户账户错误
    def test_user_login_wrong(self):
        case_data = get_test_data(self.excel_data, 'userloginwrong')  # 从数据列表中查找到该用例数据
        print(case_data['url'])
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        else:
            res = send_request(case_data)
            assert case_data['expect_res'] == res["detail"]
            log_case_info(case_data, res)

    @allure.link('/basic/auth/login', name='登录页面')
    @allure.story("测试登录成功")  # 功能块，具有相同feature或story的用例将规整到相同模块下,执行时可用于筛选
    def test_user_login_normal(self):
        case_data = get_test_data(self.excel_data,'userloginnormal')  # 从数据列表中查找到该用例数据
        res = send_request(case_data)
        assert case_data['expect_res'] == res["data"]["account"]["name"]
        log_case_info(case_data, res)


if __name__ == '__main__':   # 非必要，用于测试我们的代码
    # pytest.main(['-s', 'test_login.py'])
    # pytest.main(['-s', '--env=test_evn'])
    pytest.main(['-s', '--env=set_excel_Sheet1'])

