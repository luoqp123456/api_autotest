import configparser as configparser
from config.confi import *


class Config:
    def __init__(self):
        self.conf = configparser.ConfigParser()  # 实例化
        self.conf_path = conf_path
        self.conf.read(conf_path, encoding='UTF-8')
        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")

    def get_conf(self, section, option):
        return self.conf.get(section, option)

    def set_conf(self, section, option, value):
        self.conf.set(section, option, value)
        with open(self.conf_path, "w+") as f:
            return self.conf.write(f)

    def add_conf(self, section):
        self.conf.add_section(section)
        with open(self.conf_path, "w+") as f:
            return self.conf.write(f)


if __name__ == '__main__':   # 非必要，用于测试我们的代码
    conf1 = Config()  # 实例化
    # 读取配置文件
    conf1.conf.read(conf_path, encoding='UTF-8')
    # 查看配置中的所有section
    sections = conf1.conf.sections()
    # print sections
    # 返回所有section和序列
    sub_conf = conf1.conf.options("environment")
    print(sub_conf)
    # 返回section中option的值
    value_sub_conf = conf1.conf.get("environment", "dev_env")
    print(value_sub_conf,type(value_sub_conf))
    # print(conf1.set_conf('test1', 'option','value1' ))
    test = conf1.get_conf('environment', 'test_env')
    print(test)