import json
import requests
import sys
sys.path.append('../..')


def login():
    url = "http://api.etmprot.etmcn.com/basic/auth/login"
    data = {"telephone": "15521283804","password": "666666","type": "PASSWORD"}
    headers = {"Content-Type": "application/json"}
    res = requests.post(url=url, data=json.dumps(data), headers=headers)  # 表单请求，数据转为字典格式
    token = res.json()["data"]["token"]
    # tok = re.findall(r'"token":"(.*)","firstLogin":', res.text)       # 正则表达式提取token
    print(token)
    return token


def update_token(token, case_data):
    toe = token
    authorization = {"Authorization": toe}
    headers = eval(case_data['headers'])
    headers.update(authorization)
    case_data['headers'] = headers
    case_data['headers'] = json.dumps(case_data['headers'])


def update_data(depend_dict, case_data):
    data = eval(case_data['data'])
    data.update(depend_dict)
    case_data['data'] = data
    case_data['data'] = json.dumps(case_data['data'])


if __name__ == '__main__':
    login()