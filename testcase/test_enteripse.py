# -- coding:utf8 --
import json
import re
import sys
import allure
import pytest
from commen.operate_logger import log_case_info
from commen.readexcel import *
from commen.send_request import send_request
sys.path.append('../..')


class Testenterprise:
    excel_data = []
    token = []

    @allure.step("登录，组织架构中点击进行添加子企业")
    @allure.description("组织架构，添加子企业与员工")
    def test_addenterprise01(self, get_session):                #添加子企业与员工
        case_data = get_test_data(self.excel_data, 'addenterprise')  # 从数据列表中查找到该用例数据
        # updatetoken(self.token, case_data)
        res = send_request(get_session,case_data)
        assert case_data['expect_res'] == res["message"]
        log_case_info(case_data, res)

    def test_addenterprise02(self, get_session):            #禁用子企业员工
        case_data = get_test_data(self.excel_data,'forbenterprise')
        # updatetoken(self.token, case_data)
        takeid = re.findall(r'http://api.etmprot.etmcn.com/basic/v2/employee/(.*)/status', case_data["url"])
        sumid = str(int(takeid[0]) + 1)
        data = json.loads(case_data['data'])
        id = {"id": sumid}
        data.update(id)
        case_data['data'] = json.dumps(data)
        new_url = "http://api.etmprot.etmcn.com/basic/v2/employee/"+sumid+"/status"
        case_data["url"] = new_url
        res = send_request(get_session,case_data)
        assert case_data['expect_res'] == res["message"]
        log_case_info(case_data, res)
        write_excel(0, 5, 2, case_data["url"])
        write_excel(0, 5, 5, case_data['data'])

    def test_addenterprise03(self, get_session):          #删除子企业员工
        case_data = get_test_data(self.excel_data,'delenterprise')
        # updatetoken(self.token, case_data)
        takeid = re.findall(r'http://api.etmprot.etmcn.com/basic/v2/employee/(.*)', case_data["url"])
        sumid = str(int(takeid[0]) + 1)
        data = json.loads(case_data['data'])
        id = {"id": sumid}
        data.update(id)
        case_data['data'] = json.dumps(data)
        new_url = "http://api.etmprot.etmcn.com/basic/v2/employee/"+sumid
        case_data["url"] = new_url
        res = send_request(get_session,case_data)
        assert case_data['expect_res'] == res["message"]
        log_case_info(case_data, res)
        write_excel(0, 6, 2, case_data["url"])
        write_excel(0, 6, 5, case_data['data'])


if __name__ == '__main__':  # 非必要，用于测试我们的代码
    # pytest.main(['-s', 'test_enteripse.py'])
    pytest.main(['-s', 'test_enteripse.py','--env=set_excel_Sheet1'])
