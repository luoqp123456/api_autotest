# -- coding:utf8 --
import json
import re

import jsonpath
import yaml
from config.confi import depend_data_yaml_path


def load_yaml(yaml_path):
    with open(yaml_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data


def write_yaml(option, key, value, yaml_path=depend_data_yaml_path):
    with open(yaml_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
        data[option][key] = value
    with open(yaml_path, 'w', encoding='utf-8') as file:
        yaml.dump(data, file, default_flow_style=False, sort_keys=False)


def read_yaml(option, key, value, yaml_path=depend_data_yaml_path):
    with open(yaml_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
        data[option][key] = value
    return data


def read_yaml_value(option, key,yaml_path=depend_data_yaml_path):
    with open(yaml_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
        value =data[option][key]
    return value


def write_depend_data_yaml(actual_response, transfer_data):
# :param depend: 需要依赖数据字典{"case_001":"['jsonpaht表达式1', 'jsonpaht表达式2']"}
#返回 depend_dict = {"name": "ceshi", "id": "1"}
    transfer_dict = {}
    # transfer = json.loads(transfer_data)
    for k, v in transfer_data.items():
        # 取得依赖中对应case编号的值提取表达式
        try:
            for value in v:
                # value : '$.data.id'
                # 返回依赖数据的key
                d_k = value.split('.')[-1]
                # 添加到依赖数据字典并返回
                transfer_dict[d_k] = jsonpath.jsonpath(actual_response, value)[0]
                write_yaml(k, d_k, transfer_dict[d_k])
        except TypeError as e:
            print(f'实际响应结果中无法正常使用该表达式提取到任何内容，发现异常{e}')


def read_depend_data_yaml(depend_data):
    depend_dict = {}
    # transfer = json.loads(transfer_data)
    for k, v in depend_data.items():
        # 取得依赖中对应case编号的值提取表达式
        try:
            if isinstance(v, list):
                for value in v:
                    val = read_yaml_value(k, value)
                    depend_dict[value] = val
            else:
                val = read_yaml_value(k, v)
                depend_dict[v] = val
        except TypeError as e:
            print(f'实际响应结果中无法正常使用该表达式提取到任何内容，发现异常{e}')
    return depend_dict


# regular = {"data":{"id01":'${case_001.id}$', "number":"15521283804", "name": "lqp"}}
def regular_data_yaml(case_data):
    data = case_data['data']
    data_str = str(data)
    if data_str.find('$') != -1:
        relevance_list = re.findall("\${(.*?)}\$", data_str)  # 查找字符串中所有$key$ 作为关联对象
        for n in relevance_list:  # 遍历关联key
            sp = n.split('.')
            case_value = sp[-1]
            case_num = sp[0]
            value = read_yaml_value(case_num, case_value)
            if type(value) != 'str':
                str_value = str(value)
                pattern = re.compile('\${' + n + '}\$')  # 初始化正则匹配
                analysis_data = re.sub(pattern, str_value, data_str, count=1)  # 关联值1次
                evl_data = eval(data_str)
                an_data = eval(analysis_data)
                evl_data.update(an_data)
                case_data['data'] = evl_data
                case_data['data'] = json.dumps(case_data['data'])
            return case_data['data']


def read_path_data_yaml(case_data):
    # 处理路径参数Path的依赖
    # 传进来的参数类似 {"case_002":"$.data.id"}/item/{"case_002":"$.meta.status"}，进行列表拆分
    path = case_data['url']
    path_list = path.split('/')
    # 获取列表长度迭代
    for i in range(len(path_list)):
        # 按着
        from json import JSONDecodeError
        try:
            # 尝试序列化成dict:   json.loads('2') 可以转换成2
            path_dict = json.loads(path_list[i])
        except JSONDecodeError as e:
            # 序列化失败此path_list[i]的值不变化
            print(f'无法转换字典，进入下一个检查,{e}')
            continue
        else:
            # 处理json.loads('数字')正常序列化导致的AttributeError
            try:
                for k, v in path_dict.items():
                    try:
                        value = read_yaml_value(k, v)
                        # 尝试从对应的case实际响应提取某个字段内容
                        path_list[i] = value
                    except TypeError as e:
                        print(f'无法提取，请检查响应字典中是否支持该表达式,{e}')
            except AttributeError as e:
                print(f'类型错误，本此将不转换值 {path_list[i]},{e}')
    # 字典中存在有不是str的元素:使用map 转换成全字符串的列表
    path_list = map(str, path_list)
    # 将字符串列表转换成字符：500/item/200
    parameters_path_url = "/".join(path_list)
    print(f'path路径参数解析依赖后的路径为{parameters_path_url}')
    case_data['url'] = parameters_path_url
    return case_data['url']


def write_path_data_yaml(actual_response, path_data):
# :param depend: 需要依赖数据字典{"case_001":"['jsonpaht表达式1', 'jsonpaht表达式2']"}
#返回 depend_dict = {"name": "ceshi", "id": "1"}
    path_dict = {}
    # transfer = json.loads(transfer_data)
    for k, v in path_data.items():
        # 取得依赖中对应case编号的值提取表达式
        try:
            for value in v:
                # value : '$.data.id'
                # 返回依赖数据的key
                d_k = value.split('.')[-1]
                # 添加到依赖数据字典并返回
                path_dict[d_k] = jsonpath.jsonpath(actual_response, value)[0]
                write_yaml(k, d_k, path_dict[d_k])
        except TypeError as e:
            print(f'实际响应结果中无法正常使用该表达式提取到任何内容，发现异常{e}')


if __name__ == '__main__':
    # data1 = load_yaml(depend_data_yaml_path)
    # print(data1)
    # # data12 = load_json(depend_data_yaml_path)
    # # print(data12)
    # token = {'data_source_id': 999}
    #
    # # data1['test_add_fuel_card_normal'].update(token)
    # print(data1)
    # write_yaml(depend_data_yaml_path,token)
    # write_yaml(depend_data_yaml_path,'test_add_fuel_card_normal','card_number',999)

    # regular = {"data":{"id01":'${case_001.id}$', "number":"15521283804", "name": "lqp"}}
    # v = regular_data_yaml(regular)
    # print(v)

    # actual_response = {"data": {"id": 333}, "num": "155212"}
    # transfer_data = {"case_001": ['$..id', '$..num'], "case_002": ['$..id']}
    # write_depend_data_yaml(actual_response, transfer_data)

    # transfer_data = {"case_001": ['id', 'num'], "case_002": 'id2'}
    # print(read_depend_data_yaml(transfer_data))

    path = {"url": '{"case_003":"path01"}/item/'}
    b = read_path_data_yaml(path)
    print(b,type(b))