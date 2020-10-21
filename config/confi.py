import os
import sys
sys.path.append('..')


# 项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的绝对路径的上一级，__file__指当前文件
data_path = os.path.join(prj_path, 'data')  # 数据目录
test_path = os.path.join(prj_path, 'testcase')   # 用例目录
conf_path = r'C:\Users\Administrator\PycharmProjects\pytest\config\config.ini'
depend_data_yaml_path = r'C:\Users\Administrator\PycharmProjects\pytest\data\depend_data.yaml'

# log_file = os.path.join(prj_path, 'log.txt')  # 也可以每天生成新的日志文件
# report_file = os.path.join(prj_path, 'report_json.html')  # 也可以每次生成新的报告
# report_html = os.path.join(prj_path, r'report\report')
report_path1 = os.path.join(prj_path, 'report')
report_path2 = r'C:\Users\Administrator\PycharmProjects\pytest\report\report\index.html'
json_path = r'C:\Users\Administrator\PycharmProjects\pytest\data\datajson.json'
resdatajson_path = r'C:\Users\Administrator\PycharmProjects\pytest\data\resdatajson.json'



