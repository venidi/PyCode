import openpyxl


wb = openpyxl.load_workbook(r'C:\Users\Veniendeavor\Desktop\execlTest\2016-2017往来.xlsx')
sheet = wb[wb.active.title]

