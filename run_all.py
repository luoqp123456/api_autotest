import os

# from commen.send_Email import EmailHandler
from config import *
import pytest


if __name__ == '__main__':
    # pytest.main()
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(['-s', '--env=set_excel_Sheet1','--alluredir', './report/report_json'])
    # 执行命令 allure generate ./temp -o ./report_json --clean ，生成测试报告
    os.system('allure generate ./report/report_json -o ./report/report --clean')
    # send_email(r'C:\Users\Administrator\PycharmProjects\pytest\report1\index.html')
    # eh = EmailHandler()
    # eh.send_email()
