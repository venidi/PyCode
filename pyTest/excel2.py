import xlrd
import xlwt
from xlutils.copy import copy

endFilePath = r'C:\Users\Veniendeavor\Desktop\execlTest\end2019.xls'
# sheetTest = open(r'C:\Users\Veniendeavor\Desktop\execlTest\sheetTest.txt', 'w')
table = xlrd.open_workbook(r'C:\Users\Veniendeavor\Desktop\execlTest\2016-2017往来2.xlsx')
sheet2019 = table.sheet_by_name(r'2019年')
book = xlwt.Workbook()
sheetNew = book.add_sheet('2019')
book.save(endFilePath)
com2016 = []

for i in range(sheet2019.nrows):
    row1 = sheet2019.row_values(i)
    com2016.append(row1)
    if row1[3] != '':
        for ix in range(i):
            if row1[3] == sheet2019.row_values(ix)[3] and row1[1] == sheet2019.row_values(ix)[1]:
                print(row1[3])
                com2016[ix][8] = row1[8] + com2016[ix][8]
                com2016[ix][9] = row1[9] + com2016[ix][9]
                for ixx in range(10):
                    row1[ixx] = ''
row = 0
for xx in com2016:
    col = 0
    for xxx in xx:
        sheetNew.write(row, col, xxx)
        col += 1
    row += 1
row += 1
book.save(endFilePath)
# for i in range(len(com2016)):
#     print(com2016[i])
    # print(str(com2016[i][3]) + str(com2016[i][8]))