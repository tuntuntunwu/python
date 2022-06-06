import xlrd, xlwt
from xlutils.copy import copy
import os

filename = "test.xls"
if not os.path.exists(filename):
    book = xlwt.Workbook()  # create a workbook
    sheet1 = book.add_sheet("sheet1")  # the workbook don't contain any worksheet. You must create one by by yourself.
    book.add_sheet('sheet2')
    book.save(filename)  # the new workbook should be saved

# xlwt can write a workbook, but can't read a workbook
old_book = xlrd.open_workbook(filename)
new_book = copy(old_book)  # xlutils.copy convert xlrd to xlwt
sheet = new_book.get_sheet(0)
for i in range(10):
    sheet.write(0, i*3, str(i+1) + "-1")
    sheet.write(0, i*3+1, str(i+1) + "-2")
    sheet.write(0, i*3+2, str(i+1) + "-3")
# insert an image
sheet.insert_bitmap("test.bmp", 2, 0)  # xlwt can only insert .bmp
new_book.save(filename)  # the modified workbook should be saved

# xlrd can read a workbook, but can't write a workbook
old_book = xlrd.open_workbook(filename)
sheet1 = old_book.sheet_by_index(0)  # sheet index starts from 0
print(sheet1.cell(0,0).value)
print(sheet1.cell(0,0).value.encode('utf-8'))
print(sheet1.cell_value(0,1))
print(sheet1.row(0)[2].value)
print(sheet1.row(0))
print(sheet1.row_values(0))
print(sheet1.col_values(2))
# print(sheet1.row_values(2))  # the image can't be read

