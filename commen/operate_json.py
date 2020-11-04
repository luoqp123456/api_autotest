import json
import jsonpath
from config.confi import resdatajson_path, json_path


def writedata(data_json, dic_json=resdatajson_path):            #保持原有的json数据，再写上或更新数据
    data = dict(readdata(dic_json))
    data.update(data_json)
    # 写入 JSON 数据
    with open(dic_json, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def readdata(dic_json=resdatajson_path):
    # 读取数据
    with open(dic_json, 'r', encoding='utf-8') as f:
        dic_jsonread = f.read()
        if len(dic_jsonread) > 0:
            data_json = json.loads(dic_jsonread)
            return data_json
        else:
            print("该json文件没有数据")


def writeresdata(resdata, dic_json=resdatajson_path):
    # 写入 JSON 数据
    with open(dic_json, 'w', encoding='utf-8') as f:
        json.dump(resdata, f, ensure_ascii=False, indent=4)


def update_json_value(k, v, dic_json=json_path):                           #输入json文件，key，value值进行对json修改
    data_json = readdata(dic_json)                     #将json文件读取且内容转为字典
    for key in list(data_json):                          #字典不能在迭代中修改，转为list进行修改
        if key == k:                                        #判断不是dict，可直接取值并修改
            data_json[key] = v
            writedata(dic_json, data_json)
        elif isinstance(data_json[key], dict):              #判断是dict，取出字典
            in_datajson = data_json[key]
            for key_in in list(in_datajson):                #在取出的字典转为list，再次进行循环查找
                if key_in == k:
                    in_datajson[key_in] = v
                    writedata(dic_json, data_json)
        else:
            print("没有对应的value")


def getres_depend(result, json_k):
    depend_data = jsonpath.jsonpath(result, '$..{}'.format(json_k))
    return depend_data


if __name__ == '__main__':
    # logging.info("hello")
    # rewrite_json_file()
    # print(prj_path,data_path)
    data_jsonup = {"loginout2":{"loginout":"xiugai"}}
    # writejson_save(json_path,data_jsonup)
    # data_json = {"kk":"write"}
    writeresdata(data_jsonup)
    # url = "http://api.etmprot.etmcn.com/basic/auth/login"
    # headers = {"Content-Type": "application/json"}
    # data = {"telephone": "15521283804","password": "666666","type": "PASSWORD"}
    # result = requests.post(url=url, data=json.dumps(data), headers=headers).json()
    # ea = getres_depend(result,'name')
    # writeresdata(ea)
    # print(result, ea, type(ea))

    # {
    #
    #     "a": "123456",
    #     "b": "dsjfia",
    #     "c": "1245wefsdaf",
    #     "d": {"tt": "8888"},
    #     "e": {"uu": {"f": "9999"}}
    # }