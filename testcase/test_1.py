# # -*- coding: utf-8 -*-
# import pytest
# from commen.operate_json import writedata
#
# path = r'C:\Users\Administrator\PycharmProjects\pytest\data\datajson.json'
# @pytest.mark.usefixtures("get_token_class")
# @pytest.mark.usefixtures("do_login")
# @pytest.mark.usefixtures("get_excel")
# @pytest.mark.usefixtures("set_excel")
# class TestBaseCase:
#     token = {}
#     excel_data = {}
#
#     def test_get_info(self):
#         # token = self.token
#         print("***基础用例：获取用户个人信息***")
#         print(f"token:{self.token},=====test")
#         writedata(self.token,path)
#
#     def test_testexcel(self):
#         print(self.excel_data)
#
#     # def test_entripes(self):
#     #     case_data = get_test_data(self.excel_data, 'logincustomer')
#     #     updatetoken(self.token, case_data)
#     #     res = run_main(case_data)
#     #     print(f"==={case_data}===")
#     #     print(res)
#     #     assert case_data['expect_res'] == res["message"]
# if __name__ == '__main__':
#     pytest.main(['-s','test_1.py'])