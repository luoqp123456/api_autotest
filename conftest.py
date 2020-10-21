# import pytest
# from commen.operate_token import login
# from config.confi import *
# sys.path.append('../..')
#
# @pytest.fixture(scope="session",autouse=True)
# def do_login():
#     token = login()
#     print("===全局设置的session====" + str(token))
#     yield token
#
# @pytest.fixture(scope="class")
# def get_info_class(request, do_login):
#     token = do_login
#     request.cls.token = token
#     print('======全局设置的class=====')
#     print(request.cls.token)
#
#
#
#
#
# if __name__ == '__main__':
#     pytest.main(['-s', 'conftest.py'])