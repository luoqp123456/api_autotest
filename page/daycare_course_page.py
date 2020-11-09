# -- coding:utf8 --
import datetime
import json
import time
from commen.operate_yaml import read_yaml_value, write_yaml


class DayCareCourse:

    def add_course(self):
        act_time = time.strftime("%Y-%m-%d", time.localtime())
        course_data = {"courseId": 22, "clazzId": 24, "classsroomId": 26, "teacherId": 2407, "helperTeacherIds": "2407",
                  "courseDate": f"{act_time}", "colorCode": "rgb(255,69,0)", "courseTimePeriodId": 348,
                  "formalChildIdList": [389],
                  "expChildIdList": [373]}
        j = json.dumps(course_data)
        return j

    def delete_course(self):
        courseManagementId = read_yaml_value("case_011","courseManagementId")
        new_courseManagementId = courseManagementId + 1
        write_yaml("case_011", 'courseManagementId', new_courseManagementId)


