import pytest
from commen.operate_token import login
from config.confi import *
from evn.get_evn import EnvMember
sys.path.append('../..')


@pytest.fixture(scope="session",autouse=True)
def do_login():
    token = login()
    return token


#将Token设置为全局变量
@pytest.fixture(scope="class",autouse=True)
def get_token_class(request, do_login):
    token = do_login
    request.cls.token = token


#将读取的数据设置为全局变量
@pytest.fixture(scope="class",autouse=True)
def get_excel(request, env):
    set_excel = env
    request.cls.excel_data = set_excel


def pytest_addoption(parser):  # 新增一个运行参数 --env
    parser.addoption(
        "--env", action="store", default="set_excel_Sheet1", choices=['set_excel_Sheet1', 'set_excel_Sheet3'],
        help="my option: type1 or type2"
    )


@pytest.fixture(scope="session")       # 指定获取环境信息，一个session获取一次
def addoption_env(pytestconfig):
    print(pytestconfig.getoption('--env'))
    return pytestconfig.getoption('--env')


@pytest.fixture(scope="session",autouse=True)
def env(addoption_env):
    envs = EnvMember()
    if addoption_env == 'set_excel_Sheet1':
        param = envs.set_excel_Sheet1()
    else:
        param = envs.set_excel_Sheet3()
    return param


# @pytest.fixture(scope='session')
# def api():
#     api = Api()
#     return api

@pytest.fixture
def case_data(request, data):
    case_name = request.function.__name__
    return data.get(case_name)




