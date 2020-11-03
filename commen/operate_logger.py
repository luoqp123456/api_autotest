# -- coding:utf8 --
import logging
import sys
sys.path.append('..')

def log_case_info(case_data, res_text):
    case = case_data['case']
    case_name = case_data.get('casename')
    url = case_data.get('url')
    data = case_data.get('data')
    expect_res = case_data.get('expect_res')
    logging.info("用例名称：{}".format(case))
    logging.info("测试用例：{}".format(case_name))
    logging.info("url：{}".format(url))
    logging.info("请求参数：{}".format(data))
    logging.info("期望结果：{}".format(expect_res))
    logging.info("实际结果：{}".format(res_text))


# log配置
logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                    # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename='log.txt',  # 日志输出文件
                    filemode='a'
                    )  # 追加模式