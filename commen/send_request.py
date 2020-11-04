from commen.operate_json import *
import logging
from commen.operate_action import update_data
from commen.operate_yaml import write_depend_data_yaml, read_depend_data_yaml, regular_data_yaml

logging.getLogger("requests").setLevel(logging.WARNING)


# class Api:
    # def __init__(self, base_url=None):
    #     self.base_url = base_url

def run_main(s, method, url, data, headers):

    # if method == 'get':
    #     res = requests.get(url=url, data=data, headers=json.loads(headers)).json()
    # elif method == 'post':
    #     res = requests.post(url=url, data=data, headers=json.loads(headers)).json()
    # elif method == 'put':
    #     res = requests.put(url=url, data=data, headers=json.loads(headers)).json()
    # else:
    #     res = requests.delete(url=url, data=data, headers=json.loads(headers)).json()
    # return res
    if method == 'get':
        res = s.get(url=url, data=data, headers=json.loads(headers)).json()
    elif method == 'post':
        res = s.post(url=url, data=data, headers=json.loads(headers)).json()
    elif method == 'put':
        res = s.put(url=url, data=data, headers=json.loads(headers)).json()
    else:
        res = s.delete(url=url, data=data, headers=json.loads(headers)).json()
    return res


def send_request(s, case_data):  # 传递用例数据，发送请求
    url = case_data.get('url')
    data = case_data.get('data')
    headers = case_data.get('headers')
    method = case_data.get('method')
    transfer_data = case_data.get('transfer_data')
    depend_data = case_data.get('depend_data')
    dif_data = case_data.get('dif_data')
    # url = self.base_url + url if self.base_url else url

    if transfer_data == "" and depend_data == "":
        if dif_data == "":
            res = run_main(s, method, url, data, headers)
        else:
            case_data['data'] = regular_data_yaml(case_data)
            res = run_main(s, method, url, data, headers)

    elif transfer_data != "" and depend_data == "":
        if dif_data == "":
            res = run_main(s, method, url, data, headers)
            write_depend_data_yaml(res, transfer_data)
        else:
            case_data['data'] = regular_data_yaml(case_data)
            res = run_main(s, method, url, data, headers)
            write_depend_data_yaml(res, transfer_data)

    elif transfer_data == "" and depend_data != "":
        if dif_data == "":
            depend = read_depend_data_yaml(case_data["depend_data"])
            update_data(depend, case_data)
            res = run_main(s, method, url, data, headers)
        else:
            case_data['data'] = regular_data_yaml(case_data)
            depend = read_depend_data_yaml(case_data["depend_data"])
            update_data(depend, case_data)
            res = run_main(s, method, url, data, headers)

    elif transfer_data != "" and depend_data != "":
        if dif_data == "":
            depend = read_depend_data_yaml(case_data["depend_data"])
            update_data(depend, case_data)
            res = run_main(s, method, url, data, headers)
            write_depend_data_yaml(res, transfer_data)
        else:
            case_data['data'] = regular_data_yaml(case_data)
            depend = read_depend_data_yaml(case_data["depend_data"])
            update_data(depend, case_data)
            res = run_main(s, method, url, data, headers)
            write_depend_data_yaml(res, transfer_data)
    else:
        print("判断错误")
    return res
