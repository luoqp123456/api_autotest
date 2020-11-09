# -- coding:utf8 --
import datetime
import json
import time

from commen.operate_yaml import read_yaml_value, write_yaml


class StudentPage:

    def student_contract_data(self):
        dt_ms = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')  # 含微秒的日期时间，来源 比特量化
        a = dt_ms.replace('-', '')
        b = a.replace(':', '')
        c = b.replace('.', '')
        d = c.replace(' ', '')
        li = list(d)
        li.pop()
        li.pop()
        cc = ''.join(li)
        act_time = time.strftime("%Y-%m-%d", time.localtime())
        data = {"contractNo": f"{cc}", "childId": 398, "contractType": "NEW_SIGNING",
                 "receivable": "100.00", "paid": "100.00", "paymentId": 247, "date": f"{act_time}",
                 "validBeginTime": f"{act_time}", "validEndTime": f"{act_time}", "mainPerformanceId": 2407,
                 "mainPercentage": 100, "secondaryPerformanceId": "",
                 "secondaryPercentage": 0, "remake": "", "earnestMoneyId": "null",
                 "listPurchaseItemsDTO": [{"id": 152, "name": "兴趣班", "modify": "false",
                                           "netReceipts": 100, "receivable": 100, "img": "", "purchase": 1, "give": 0,
                                           "receivableNotes": 100, "netReceiptsNotes": 100,
                                           "cacSetMealEnum": "COURSE_TYPE"}]}
        aj = json.dumps(data)
        return aj

    def contract_action_data(self):
        transer_id = read_yaml_value('case_009', 'id')
        new_id = transer_id + 1
        write_yaml('case_009', 'id', new_id)
        data = {"id": f'{new_id}', "toExamineState": "true"}
        aj = json.dumps(data)
        return aj

    def delete_contract_data(self):
        act_time = time.strftime("%Y-%m-%d", time.localtime())
        data = {"refund": 100, "refundId": 247, "refundDate": f"{act_time}", "refundRemake": ""}
        aj = json.dumps(data)
        return aj


if __name__ == '__main__':
    a = StudentPage()
    print(a.student_contract_data())