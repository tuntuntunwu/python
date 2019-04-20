import xlrd, xlwt
from xlutils.copy import copy

workbook = xlrd.open_workbook(r"f:/L/G-研一下/助教/学分助教/!!评分表!!.xlsx")
opt_workbook = copy(workbook)
sheet = opt_workbook.get_sheet(0)
for i in range(18):
    sheet.write(0, i*3+5, str(i+1) + "-1")
    sheet.write(0, i*3+6, str(i+1) + "-2")
    sheet.write(0, i*3+7, str(i+1) + "-3")
opt_workbook.save(r'f:/L/G-研一下/助教/学分助教/!!评分表1!!.xls')
