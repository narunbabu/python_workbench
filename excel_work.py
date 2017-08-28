# Import pandas
import pandas as pd

# Assign spreadsheet filename to `file`
file = '../DCHB_Village_Release_2800.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df = xl.parse('Village_Data_2800')
print(df.columns)
col_names=df.columns
# print(df1['Sepal width'])
print(df[col_names[0]])
####################
import numpy as np 
# df[col_names[41],col_names[42]]
i=0
for coln in col_names:
    i=i+1
    # print(i)
    print(i,coln)
cols2see=[35,36,37,38,39]

myarray=df[col_names[34]]
print(34+1,col_names[34])
for x in cols2see: #range(42, 45):
    print(x+1,col_names[x])
    # df[col_names[0]]
    myarray=np.vstack((myarray, df[col_names[x]]))

def myhist(y):
    yh= np.arange(0,40,1)
    for x in range(0,40):
        yh[x]=(y==x).sum()
    return yh


w=myarray.T
w[:,1]
for x in range(40, 42):
    print(x+1,col_names[x])


np.hstack((a,b))

x = np.arange(0,10,2)
#####################
# Install `XlsxWriter` 
pip install XlsxWriter

# Specify a writer
writer = pd.ExcelWriter('example.xlsx', engine='xlsxwriter')

# Write your DataFrame to a file     
yourData.to_excel(writer, 'Sheet1')

# Save the result 
writer.save()
##################
# Write the DataFrame to csv
df.to_csv("example.csv")
###########################
# Put the sheet values in `data`
data = sheet.values

# Indicate the columns in the sheet values
cols = next(data)[1:]

# Convert your data to a list
data = list(data)

# Read in the data at index 0 for the indices
idx = [r[0] for r in data]

# Slice the data at index 1 
data = (islice(r, 1, None) for r in data)

# Make your DataFrame
df = pd.DataFrame(data, index=idx, columns=cols)