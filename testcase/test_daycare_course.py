# -- coding:utf8 --
import allure
import pytest
import sys
from commen.operate_logger import log_case_info
from commen.readexcel import *
from commen.send_request import *
from page.daycare_course_page import DayCareCourse
sys.path.append('../..')


class Test_daycare:
    excel_data = []

    def test_daycare_course01(self, get_session):
        case_data = get_test_data(self.excel_data, 'daycarecourse')
        a = DayCareCourse()
        da = a.add_course()
        case_data['data'] = da
        res = send_request(get_session, case_data)
        assert case_data['expect_res'] == res["message"]
        log_case_info(case_data, res)

    def test_daycare_course02(self, get_session):

        case_data = get_test_data(self.excel_data, 'deletedaycourse')
        res = send_request(get_session, case_data)
        assert case_data['expect_res'] == res["message"]
        log_case_info(case_data, res)


if __name__ == '__main__':
    pytest.main(['-s', 'test_daycare_course.py'])