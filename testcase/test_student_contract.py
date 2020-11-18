# -- coding:utf8 --
import allure
import pytest
import sys
from commen.operate_logger import log_case_info
from commen.readexcel import *
from commen.send_request import *
from page.student_page import StudentPage

sys.path.append('../..')


class Test_daycare:
    excel_data = []

    def test_add_contract01(self, get_session):
        case_data = get_test_data(self.excel_data, 'addcontract')
        a = StudentPage()
        da = a.student_contract_data()
        case_data['data'] = da
        res = send_request(get_session, case_data)
        assert case_data['expect_res'] == res["message"]
        log_case_info(case_data, res)

    def test_add_contract02(self, get_session):
        case_data = get_test_data(self.excel_data, 'actioncontract')
        a = StudentPage()
        da = a.contract_action_data()
        case_data['data'] = da
        res = send_request(get_session, case_data)
        assert case_data['expect_res'] == res["message"]
        log_case_info(case_data, res)

    def test_add_contract03(self, get_session):
        case_data = get_test_data(self.excel_data, 'deletecontract')
        a = StudentPage()
        da = a.delete_contract_data()
        case_data['data'] = da
        res = send_request(get_session, case_data)
        assert case_data['expect_res'] == res["message"]
        log_case_info(case_data, res)


if __name__ == '__main__':
    pytest.main(['-s', 'test_student_contract.py'])
