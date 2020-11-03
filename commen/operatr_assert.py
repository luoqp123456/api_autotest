# -- coding:utf8 --
import json
import jsonpath


def assert_code(res, expected_code):
    """
    验证response状态码
    :param code:
    :param expected_code:
    :return:
    """
    try:
        res_code = jsonpath.jsonpath(res, res['code'])[0]
        assert res_code == expected_code
        return True
    except Exception as e:
        print("Exception is %s, statusCode error, expected_code is %s, statusCode is %s " % (e, expected_code, res_code))
        raise


def assert_in_text(res, expected_msg):
    """
    验证response body中是否包含预期字符串
    :param body:
    :param expected_msg:
    :return:
    """
    try:
        text = json.dumps(res, ensure_ascii=False)
        assert expected_msg in text
        return True
    except Exception as e:
        print("Exception is %s,Response body Does not contain expected_msg, expected_msg is %s" %(e, expected_msg))
        raise


def assert_time(time, expected_time):
    """
    验证response body响应时间小于预期最大响应时间,单位：毫秒
    :param body:
    :param expected_time:
    :return:
    """
    try:
        assert time < expected_time
        return True
    except Exception as e:
        print("Exception is %s,Response time > expected_time, expected_time is %s, time is %s" % (e,expected_time, time))
        raise


