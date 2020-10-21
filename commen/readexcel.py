import xlrd
from xlutils.copy import copy


def excel_to_list(xls_name, sheet_name):     #读取Excel表格sheet下的用例数据
    data_list = []
    worksheet = xlrd.open_workbook(xls_name)  #打开表
    sheet = worksheet.sheet_by_name(sheet_name)      #获取表的sheet
    header = sheet.row_values(0)                         #获取sheet的第一行的数据
    for i in range(1, sheet.nrows):  # 跳过标题行，从第二行开始取数据
        d = dict(zip(header, sheet.row_values(i)))  # 将标题和每行数据组装成字典
        data_list.append(d)                             #添加到list中
    return data_list  # 列表嵌套字典格式，每个元素是一个字典


def get_test_data(data_list, casename):       #传递表格的全部数据，根据用例的名称获取数据
    for case_data in data_list:
        if casename == case_data['casename']:  # 如果字典数据中case_name与参数一致
            return case_data
            # 如果查询不到会返回None


def write_excel(sheetindex, row, col, value):
    # excel_path = r"F:\ceshi.xls"  # 文件路径
    excel_path = r"C:\Users\Administrator\PycharmProjects\pytest\data\ceshi.xls"
    # excel_path=unicode('D:\\测试.xls','utf-8')#识别中文路径
    rbook = xlrd.open_workbook(excel_path, formatting_info=True)  # 打开文件
    wbook = copy(rbook)  # 复制文件并保留格式
    w_sheet = wbook.get_sheet(sheetindex)# 索引sheet表
    w_sheet.write(row, col, value)
    wbook.save(excel_path)  # 保存文件


