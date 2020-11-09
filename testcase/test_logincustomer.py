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

    # def test_logincustomer(self, get_session):
    #     case_data = get_test_data(self.excel_data, 'logincustomer')  # 从数据列表中查找到该用例数据
    #     res = send_request(get_session,case_data)
    #     assert case_data['expect_res'] == res["message"]
    #     assert_in_text(res, case_data['expect_res'])
    #     log_case_info(case_data, res)

    # def test_addstudent(self, get_session):
    #     case_data = get_test_data(self.excel_data, 'addstudent')
    #     res = send_request(get_session, case_data)
    #     assert_in_text(res, case_data['expect_res'])
    #     log_case_info(case_data, res)

    def test_add_contract01(self,get_session):
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


if __name__ == '__main__':   # 非必要，用于测试我们的代码
    pytest.main(['-s', 'test_logincustomer.py'])

    course = {"courseId": 22, "clazzId": 24, "classsroomId": 26, "teacherId": 2407, "helperTeacherIds": "2407",
     "courseDate": "2020-11-15", "colorCode": "rgb(255,69,0)", "courseTimePeriodId": 348, "formalChildIdList": [389],
     "expChildIdList": [373]}


    res = {"data":{"courseManagementId":131,"courseId":22,"clazzId":24,"classsroomId":26,"teacherId":2407,"helperTeacherIds":"2407",
        "courseDate":1605369600000,"colorCode":"rgb(255,69,0)","courseTimePeriodId":348,"totalFormalChildNum":10,"totalExpChildNum":10,
        "currentFormalChildNum":1,"currentExpChildNum": 1, "enterpriseId": 663,"courseTimePeriod":"08:00 - 09:00"}, "code": 0, "message":"成功",
           "traceId":"1a349ae0cea6466d9fc3f6ea066e682c", "detail": "null"}

    delete_url = 'http://api.etmprot.etmcn.com/daycare/course_management/131'
    delete_data = {"courseManagementId": 131}

    course2 = {"courseId": 22, "clazzId": 24, "classsroomId": 26, "teacherId": 2407, "helperTeacherIds": "2407",
               "courseDate": "2020-11-15",
               "colorCode": "rgb(255,69,0)", "courseTimePeriodId": 349, "formalChildIdList": [], "expChildIdList": []}

    res2 =  {"data": {"courseManagementId": 132, "courseId": 22, "clazzId": 24, "classsroomId": 26, "teacherId": 2407,
              "helperTeacherIds": "2407", "courseDate": 1605369600000, "colorCode": "rgb(255,69,0)",
              "courseTimePeriodId": 349, "totalFormalChildNum": 10, "totalExpChildNum": 10, "currentFormalChildNum": 0,
              "currentExpChildNum": 0, "enterpriseId": 663, "courseTimePeriod": "09:00 - 10:00"}, "code": 0,
     "message": "成功", "traceId": "f4a6d55be9024199a775d639ec1b1b6e", "detail": "null"}

    course3 = {"courseId":22,"clazzId":24,"classsroomId":26,"teacherId":2407,"helperTeacherIds":"2407","courseDate":"2020-11-14",
               "colorCode":"rgb(255,69,0)",
               "courseTimePeriodId":348,"formalChildIdList":[],"expChildIdList":[]}
    res3 = {"data":{"courseManagementId":133,"courseId":22,"clazzId":24,"classsroomId":26,"teacherId":2407,"helperTeacherIds":"2407",
                    "courseDate":1605283200000,"colorCode":"rgb(255,69,0)","courseTimePeriodId":348,"totalFormalChildNum":10,"totalExpChildNum":10,
                    "currentFormalChildNum":0,"currentExpChildNum":0,"enterpriseId":663,"courseTimePeriod":"08:00 - 09:00"},"code":0,
                    "message":"成功","traceId":"66db71d330db4d39aab9172a01d6443c","detail":"null"}

    course4 = {"courseId":22,"clazzId":24,"classsroomId":26,"teacherId":2407,"helperTeacherIds":"2407","courseDate":"2020-11-15",
               "colorCode":"rgb(255,69,0)",
               "courseTimePeriodId":350,"formalChildIdList":[],"expChildIdList":[]}
    res4 = {"data":{"courseManagementId":134,"courseId":22,"clazzId":24,"classsroomId":26,"teacherId":2407,"helperTeacherIds":"2407",
                    "courseDate":1605369600000,"colorCode":"rgb(255,69,0)","courseTimePeriodId":350,"totalFormalChildNum":10,"totalExpChildNum":10,
                    "currentFormalChildNum":0,"currentExpChildNum":0,"enterpriseId":663,
                    "courseTimePeriod":"10:00 - 11:00"},"code":0,"message":"成功","traceId":"bbcba7fa13c2446bbed09ff8776b8a35","detail":"null"}