# -*- coding=utf8 -*-
import json
import random


# def creat_phone(number):
#     # 第二位
#
#     # num = []
#     second = [3, 4, 5, 7, 8][random.randint(0, 4)]
#     # 第三位的值根据第二位来确定
#     third = {
#         3: random.randint(0, 9),
#         4: [5, 7, 9][random.randint(0, 2)],
#         5: [i for i in range(10) if i != 4][random.randint(0, 8)],
#         7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
#         8: random.randint(0, 9)
#     }[second]
#     # 后8位随机抽取
#     num_list = []
#     num = "1{}{}".format(second, third)
#     for i in range(0, number):
#         suffix = ''
#
#         for x in range(8):
#             suffix = suffix + str(random.randint(0, 9))
#         num2 = num + suffix
#         num_list.append(num2)
#         print(num_list)
import pytest
import requests
import xlrd
from pyparsing import unicode

from commen.operate_action import login
from commen.readexcel import write_excel, excel_to_list


def raddomPhone():
    headList = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
                "186", "187", "188", "189"]
    num_list = []
    # for i in range(number):
    a = random.choice(headList)
    suffix = ''
    for x in range(8):
        suffix = suffix + str(random.randint(0, 9))
    sum = a + suffix

    return sum


def random_name():
    firstName = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻水云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳鲍史唐费岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅卞齐康伍余元卜顾孟平" \
                "黄和穆萧尹姚邵汪祁毛禹狄米贝明成戴宋茅庞熊纪舒屈项祝董粱杜阮席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田胡凌霍万柯卢莫房缪干解应宗丁宣邓郁单杭洪包诸左石崔吉" \
                "龚程邢滑裴陆荣翁荀羊芮储靳邴车侯伊宁仇武符刘龙叶幸司黎乔苍双闻莘劳冉牛寿通尚温庄瞿茹习鱼容向古耿弘国文东殴沃曾关闫"
    firstName2 = "万俟司马上官欧阳夏侯诸葛闻人东方赫连皇甫尉迟公羊澹台公冶宗政濮阳淳于单于太叔申屠公孙仲孙轩辕令狐钟离宇文长孙慕容鲜于闾丘司徒司空亓官司寇仉督子颛孙端木巫马公西漆雕乐正壤驷公良拓跋夹谷宰父谷梁段干百里东郭南门呼延羊舌微生梁丘左丘东门西门南宫南宫"
    girl = '秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽'
    boy = '伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家致树炎德行时泰盛雄琛钧冠策腾楠榕风航弘'
    true_name = '中笑贝凯歌易仁器义礼智信友上加金马钰玉忠孝杰豪平萍坪柳彩荣蓉榕鑫欣芯昕沁天田颖莹英亨恒芝玉萍红娥玲芬芳燕彩春宁贵福生龙元全国胜学祥才发武新利清飞'
    girl_name2 = '秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽'
    boy_name2 = '伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家致树炎德行时泰盛雄琛钧冠策腾楠榕风航弘'


    firstName_name = firstName[random.choice(range(len(firstName)))]
    if random.choice(range(100)) > 10:
        firstName_name = firstName[random.choice(range(len(firstName)))]
    else:
        i = random.choice(range(len(firstName2)))
        firstName_name = firstName2[i:i + 2]
    sex = random.choice(range(2))
    relation = random.choice(range(2))
    name_1 = ""
    if relation > 0:
        if sex > 0:
            female = '女'
            relatioshiplist_id = '妈妈'
            girl_name = girl[random.choice(range(len(girl)))]
            girl_name2 = girl_name2[random.choice(range(len(girl_name2)))]
            firstName2 = firstName2[random.choice(range(len(firstName2)))]
            name_1 = true_name[random.choice(range(len(true_name)))]
            stu_name = firstName_name + name_1 + girl_name
            relation_name = firstName2 + girl_name2 + girl_name
            return stu_name, relation_name, female, relatioshiplist_id

        else:
            male = '男'
            relatioshiplist_id = '妈妈'
            boy_name = boy[random.choice(range(len(boy)))]
            girl_name = girl[random.choice(range(len(girl)))]
            girl_name2 = girl_name2[random.choice(range(len(girl_name2)))]
            firstName2 = firstName2[random.choice(range(len(firstName2)))]
            name_1 = true_name[random.choice(range(len(true_name)))]
            stu_name = firstName_name + name_1 + boy_name
            relation_name = firstName2 + girl_name2 + girl_name
            return stu_name, relation_name, male, relatioshiplist_id
    else:
        if sex > 0:
            female = '女'
            relatioshiplist_id = '爸爸'
            girl_name = girl[random.choice(range(len(girl)))]
            boy_name = boy[random.choice(range(len(boy)))]
            boy_name2 = boy_name2[random.choice(range(len(boy_name2)))]
            name_1 = true_name[random.choice(range(len(true_name)))]
            stu_name = firstName_name + name_1 + girl_name
            relation_name = firstName_name + boy_name2 + boy_name
            return stu_name, relation_name, female, relatioshiplist_id

        else:
            male = '男'
            relatioshiplist_id = '爸爸'
            boy_name = boy[random.choice(range(len(boy)))]
            boy_name2 = boy_name2[random.choice(range(len(boy_name2)))]
            name_1 = true_name[random.choice(range(len(true_name)))]
            stu_name = firstName_name + name_1 + boy_name
            relation_name = firstName_name + boy_name2 + boy_name
            return stu_name, relation_name, male, relatioshiplist_id


def write_excel2(i):
    relatioshiplist = ['妈妈', '爸爸', '爷爷', '奶奶', '外公', '外婆']
    source = ['地推', '百度', '员工转介绍', '会员转介绍', '官网', '非会员转介绍']
    importanceAttrId = ['重要', '很重要', '非常重要']
    followerId = ['花旗参', '西瓜', '甘草', '苏木', '四叶草', '罗汉果', '生菜', '花椒']
    relatioshiplist_id = random.choice(relatioshiplist)
    telephone = raddomPhone()
    follower_id = random.choice(followerId)
    marketer_id = random.choice(followerId)
    source_id = random.choice(source)
    importanceAttr_id = random.choice(importanceAttrId)
    ceshi = random_name()
    child_name = ceshi[0]
    parentName = ceshi[1]
    gender = ceshi[2]
    relatioshiplist_id = ceshi[3]
    birt_day = get_birthday()
    from xlutils.copy import copy
    excel_path = r"D:\未成交导入模板-新.xlsx"
    save_path = r"D:\未成交导入模板-新.xlsx"
    # excel_path=unicode('D:\\测试.xls','utf-8')#识别中文路径
    rbook = xlrd.open_workbook(excel_path)  # 打开文件
    wbook = copy(rbook)  # 复制文件并保留格式
    w_sheet = wbook.get_sheet('未成交导入模板')  # 索引sheet表
    w_sheet.write(i, 0, child_name)
    w_sheet.write(i, 1, relatioshiplist_id)
    w_sheet.write(i, 2, parentName)
    w_sheet.write(i, 3, telephone)
    w_sheet.write(i, 10, gender)
    w_sheet.write(i, 11, birt_day)
    w_sheet.write(i, 15, '新客户')
    w_sheet.write(i, 16, importanceAttr_id)
    w_sheet.write(i, 17, source_id)
    w_sheet.write(i, 21, follower_id)
    w_sheet.write(i, 22, marketer_id)
    wbook.save(save_path)  # 保存文件


def get_birthday():
    start_birthday = (2014, 10, 10, 1, 10, 10, 10, 10, 10)  # 设置开始时间元组
    end_birthday = (2020, 5, 5, 10, 10, 10, 10, 10, 10)  # 设置结束时间元组
    import time
    start = time.mktime(start_birthday)  # 生成开始时间戳
    end = time.mktime(end_birthday)  # 生成结束时间戳
    for i in range(1):
        s = random.randint(start, end)  # 选择一个开始时间和结束时间
        date_touole = time.localtime(s)  # 将时间生成元组
        date1 = time.strftime("%Y/%m/%d", date_touole)  # 时间元组转换成格式化字符串
    return date1

def write_data():
    for i in range(3, 520):
        write_excel2(i)
        i += 1
        print(i)


def for_radomname(num):
    for i in range(num):
        random_name()

def get_intoday():

    while True:
        data1 = get_birthday()
        data2 = get_birthday()
        if data1 <= data2:
            continue
        else:
            return data1, data2

def write_baby(i):
    ceshi = random_name()
    child_name = ceshi[0]
    parentName = ceshi[1]
    gender = ceshi[2]
    relatioshiplist_id = ceshi[3]
    room = ['托中3班','托中2班','托中1班','托4班','托3班','托2班','托1班','大4班','大2班','大1班']
    room_id = random.choice(room)
    into_day, birthday = get_intoday()
    telephone = raddomPhone()
    from xlutils.copy import copy
    excel_path = r"F:\在园幼儿导入模板.xls"
    save_path = r"F:\在园幼儿导入模板.xls"
    # excel_path=unicode('D:\\测试.xls','utf-8')#识别中文路径
    rbook = xlrd.open_workbook(excel_path)  # 打开文件
    wbook = copy(rbook)  # 复制文件并保留格式
    w_sheet = wbook.get_sheet('在园幼儿导入模板（简版）')  # 索引sheet表
    w_sheet.write(i, 0, child_name)
    w_sheet.write(i, 1, gender)
    w_sheet.write(i, 2, birthday)
    w_sheet.write(i, 3, into_day)
    w_sheet.write(i, 4, room_id)
    w_sheet.write(i, 5, parentName)
    w_sheet.write(i, 6, relatioshiplist_id)
    w_sheet.write(i, 7, telephone)
    wbook.save(save_path)  # 保存文件

def for_write():
    for i in range(5, 520):
        write_baby(i)
        print(i)

if __name__ == '__main__':
    pytest.main(['-s', 'test_interface.py'])
    # test_get_birthday()
    # write_data()
    # for_write()
    a,b = get_intoday()
    print(a,b)
