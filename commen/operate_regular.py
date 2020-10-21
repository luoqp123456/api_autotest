import re


def regular_replace(regular_value, relevance):
    try:
        relevance_list = re.findall("\${(.*?)}\$", regular_value)  # 查找字符串中所有$key$ 作为关联对象
        for n in relevance_list:  # 遍历关联key
            pattern = re.compile('\${' + n + '}\$')  # 初始化正则匹配
            regular_value = re.sub(pattern, relevance[n], regular_value, count=1)  # 关联值1次
    except TypeError:
        pass
    return regular_value


p_data = r'\${(.*)}\$'


def res_sub(data, replace, pattern_data=p_data):
    pattern = re.compile(pattern_data)
    res = pattern.findall(data)
    if res:
        return re.sub(pattern_data, replace, data)


if __name__ == "__main__":
    regular_value = "这是一段${test}$用的数据"
    _relevance = {"test": "测试"}
    print(regular_replace(regular_value, _relevance))
