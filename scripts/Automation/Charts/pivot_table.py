'''
This module creates a pivot table based on the excel report data.
A pivot table is a tool that summarizes and reorganizes data in a spreadsheet
or database table. It can help users analyze large amounts of data and
create reports.
'''

import pandas as pd

df = pd.read_excel('supermarket_sales.xlsx')

# use [[]] to select multiple cols, use [] to select single col.
df = df[['Gender', 'Product line', 'Total']]
# print(df)

# calculate the amount spent by each gender on different items.
pivot_table = df.pivot_table(
    index='Gender',
    columns='Product line',
    values='Total',
    aggfunc='sum'
)

pivot_table.to_excel('pivot_table.xlsx', 'Report', startrow=4)
