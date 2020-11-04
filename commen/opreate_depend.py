# -- coding:utf8 --
import json
import re
import jsonpath


# 保存实际响应
def save_actual_response(actual_response, case_key, case_response):
        # :param case_key:用例编号
        # :param case_response:对应用例编号的实际响应
        # :return:
    actual_response[case_key] = case_response
    return actual_response

# 读取依赖数据
def read_depend_data(actual_response, depend):
# :param depend: 需要依赖数据字典{"case_001":"['jsonpaht表达式1', 'jsonpaht表达式2']"}
#返回 depend_dict = {"name": "ceshi", "id": "1"}
    depend_dict = {}
    depend = json.loads(depend)
    for k, v in depend.items():
        # 取得依赖中对应case编号的值提取表达式
        try:
            for value in v:
                # value : '$.data.id'
                # 取得对应用例编号的实际响应结果
                actual = actual_response[k]
                # 返回依赖数据的key
                d_k = value.split('.')[-1]
                # 添加到依赖数据字典并返回
                depend_dict[d_k] = jsonpath.jsonpath(actual, value)[0]
        except TypeError as e:
            print(f'实际响应结果中无法正常使用该表达式提取到任何内容，发现异常{e}')
    return depend_dict

# key = {"case_001":[$.data.id], "case_002":[$.data.message]}
# {"key": {"id":1, "user":"lqp", "num":2 }}


def treating_data(actual_response, dependent, data):
    # 处理依赖数据data
    if dependent != '':
        if dependent.find('=') != -1:
            dependent_key = dependent.split('=')[0]
            dependent_value = dependent.split('=')[1]
            dependent_data = {dependent_key: read_depend_data(actual_response, dependent_value)}
        else:
            dependent_data = read_depend_data(actual_response, dependent)
        print(f'依赖数据解析获得的字典{dependent_data}')

        if data != '':
            data = json.loads(data)
            exists_key = False
            # 处理data与依赖中有相同key的问题, 目前之支持列表，字典,本地 列表形式调试通过，需要在定义时，data中该key定义成列表
            # 实例{"id": [1],"user":{"username":"123"}}
            for k, v in data.items():
                for dk, dv in dependent_data.items():
                    if k == dk:
                        if isinstance(data[k], list):
                            data[k].append(dv)
                        if isinstance(data[k], dict):
                            data[k].update(dv)
                        exists_key = True
            if exists_key is False:
                # 合并组成一个新的data
                dependent_data.update(data)
                data = dependent_data
                print(f'data有数据，依赖有数据时 {data}')

        else:
            # 赋值给data
            data = dependent_data
            print(f'data无数据，依赖有数据时 {data}')
    else:
        if data == '':
            data = None
            print(f'data无数据，依赖无数据时 {data}')
        else:
            data = json.loads(data)
            print(f'data有数据，依赖无数据 {data}')


# depend_data = {"id": "1"}
# data = {"sumid": "${id}$"}

def regular_data(depend_data, data):
    str_data = str(data)
    # 处理依赖数据data
    relevance_list = re.findall("\${(.*?)}\$", str_data)  # 查找字符串中所有$key$ 作为关联对象
    for n in relevance_list:  # 遍历关联key
        pattern = re.compile('\${' + n + '}\$')  # 初始化正则匹配
        analysis_data = re.sub(pattern, depend_data[n], str_data, count=1)  # 关联值1次
        evl_data = eval(str_data)
        an_data = eval(analysis_data)
        evl_data.update(an_data)
        return evl_data


def get_res_depend(result, json_k):
    depend_data = jsonpath.jsonpath(result, '$..{}'.format(json_k))
    return depend_data


if __name__ == '__main__':
    depend_data = {"id": "1"}
    data = {"sumid": "${id}$"}

    a = regular_data(depend_data, data)
    print(a)
