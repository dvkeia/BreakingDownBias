import pandas as pd

test = pd.read_excel('GSNI2023_AnnexTables2.xlsx', sheet_name='Table A5')

print("first few rows")
print(test.head())

print("last few rows")
print(test.tail())

