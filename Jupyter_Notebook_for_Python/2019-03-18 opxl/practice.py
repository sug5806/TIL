import openpyxl as op
import os

os.chdir('Z:\\GD\\Study\\Jupyter Notebook for Python\\2019-03-18 opxl')

wb = op.load_workbook('exam.xlsx')
ws = wb.active
g = ws.rows
a = next(g)

li = []
for cell in a:
    li.append(cell.value)
print(li)

student_data = []
for row in g:
    dic = {k :v.value for k, v in zip(li, row)}
    student_data.append(dic)
