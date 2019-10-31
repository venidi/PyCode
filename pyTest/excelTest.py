import xlrd
import xlwt

endFilePath = r'C:\Users\Veniendeavor\Desktop\execlTest\end.xls'
# sheetTest = open(r'C:\Users\Veniendeavor\Desktop\execlTest\sheetTest.txt', 'w')
table = xlrd.open_workbook(r'C:\Users\Veniendeavor\Desktop\execlTest\2016-2017往来.xlsx')
sheet2016 = table.sheet_by_name(r'2016年往来')
sheet2017 = table.sheet_by_name(r'2017年往来')
sheet2018 = table.sheet_by_name(r'2018年')
sheet2019 = table.sheet_by_name(r'2019年')

book = xlwt.Workbook()
sheetNew = book.add_sheet('new')
book.save(endFilePath)
row = 0
col = 0

for i in range(sheet2016.nrows):
        ix = sheet2016.row_values(i)
        if ix[3] == '':
            continue
        # elif ix[3] == '济南热电有限公司':
        #     continue
        # elif ix[3] == '济南黄河路桥建设集团有限公司':
        #     continue
        else:
            # print(ix[3])
            for j in range(sheet2017.nrows):
                jx = sheet2017.row_values(j)
                for k in range(sheet2018.nrows):
                    kx = sheet2018.row_values(k)
                    for m in range(sheet2019.nrows):
                        mx = sheet2018.row_values(m)
                        if ix[3] == jx[3]:
                            if jx[3] == kx[3]:
                                if kx[3] == mx[3]:
                                    workb = open(endFilePath)
                                    com = [['2016', str(ix[3]), str(ix[8]), str(ix[9]), str(ix[1])],
                                           ['2017', str(jx[3]), str(jx[8]), str(jx[9]), str(jx[1])],
                                           ['2018', str(kx[3]), str(kx[8]), str(kx[9]), str(kx[1])],
                                           ['2019', str(mx[3]), str(mx[8]), str(mx[9]), str(mx[1])],
                                    ]
                                    for xx in com:
                                        col = 0
                                        for xxx in xx:
                                            print(xxx)
                                            sheetNew.write(row, col, xxx)
                                            col += 1
                                        row += 1
                                    row += 1
                                    book.save(endFilePath)


#                                     print('2016' + ix[3], '||' + str(ix[8]), '||' + str(ix[9]), '||' + str(ix[1]))
#                                     print('2017' + jx[3], '||' + str(jx[8]), '||' + str(jx[9]), '||' + str(jx[1]))
#                                     print('2018' + kx[3], '||' + str(kx[8]), '||' + str(kx[9]), '||' + str(kx[1]))
#                                     print('2019' + mx[3], '||' + str(mx[8]), '||' + str(mx[9]), '||' + str(mx[1]))
#                                     print('=======================================')
#
#                                     print('2016' + ix[3], '||' + str(ix[8]), '||' + str(ix[9]), '||' + str(ix[1]), file=sheetTest)
#                                     print('2017' + jx[3], '||' + str(jx[8]), '||' + str(jx[9]), '||' + str(jx[1]), file=sheetTest)
#                                     print('2018' + kx[3], '||' + str(kx[8]), '||' + str(kx[9]), '||' + str(kx[1]), file=sheetTest)
#                                     print('2019' + mx[3], '||' + str(mx[8]), '||' + str(mx[9]), '||' + str(mx[1]), file=sheetTest)
#                                     print('=======================================', file=sheetTest)
#                                     # print(ix[3], file=sheetTest)
# sheetTest.close()


