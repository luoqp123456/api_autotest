import requests
from commen.operate_json import *
import logging
logging.getLogger("requests").setLevel(logging.WARNING)


# class Api:
    # def __init__(self, base_url=None):
    #     self.base_url = base_url

def run_main(method, url, data, headers):

    if method == 'get':
        res = requests.get(url=url, data=data, headers=json.loads(headers)).json()
    elif method == 'post':
        res = requests.post(url=url, data=data, headers=json.loads(headers)).json()
    elif method == 'put':
        res = requests.put(url=url, data=data, headers=json.loads(headers)).json()
    else:
        res = requests.delete(url=url, data=data, headers=json.loads(headers)).json()
    return res


def send_request(case_data):  # 传递用例数据，发送请求
    url = case_data.get('url')
    data = case_data.get('data')
    headers = case_data.get('headers')
    method = case_data.get('method')
    depend = case_data.get('depend')
    dependdata = case_data.get('dependdata')
    # url = self.base_url + url if self.base_url else url

    if dependdata == "" and depend == "":
        res = run_main(method, url, data, headers)
    elif dependdata == "" and depend != "":
        case_data["depend"] = readdata()
        data = json.loads(case_data['data'])
        data.update(case_data["depend"])
        case_data['data'] = json.dumps(data)
        res = run_main(method, url, data, headers)
    elif dependdata != "" and depend == "":
        res = run_main(method, url, data, headers)
        resdatajson = getres_depend(res, case_data["dependdata"])
        writedata(resdatajson)
    elif dependdata != "" and depend != "":
        case_data["depend"] = readdata()
        data = json.loads(case_data['data'])
        data.update(case_data["depend"])
        case_data['data'] = json.dumps(data)
        res = run_main(method, url, data, headers)
        resdatajson = getres_depend(res, case_data["dependdata"])
        writedata(resdatajson)
    else:
        print("判断错误")
    return res