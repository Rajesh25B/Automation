'''
This module helps to automate the format of an excel report using python.
'''

from openpyxl import load_workbook
from openpyxl.styles import Font

wb = load_workbook('pivot_table.xlsx')
sheet = wb['Report']

sheet['A1'] = 'Sales Report'
sheet['A2'] = 'Pivot Table'

sheet['A1'].font = Font(name='Comic Sans MS', bold=True, i=True, size=20)
sheet['A2'].font = Font(name='Comic Sans MS', bold=True, i=True, size=15)

wb.save('format.xlsx')
