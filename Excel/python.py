import xlsxwriter
 
# Workbook() takes one, non-optional, argument 
# which is the filename that we want to create.
workbook = xlsxwriter.Workbook('hello.xlsx')
 
# The workbook object is then used to add new 
# worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet()
worksheet1 = workbook.add_worksheet()
worksheet2 = workbook.add_worksheet()

# Select the second worksheet (worksheet number 2)
worksheets = workbook.worksheets()
selected_worksheet = worksheets[1]  

# data via the write() method.
worksheet.write('A1', 'Hello..')
worksheet.write('B1', 'Geeks')
worksheet.write('C1', 'For')
worksheet.write('D1', 'Geeks')
 
# Finally, close the Excel file
# via the close() method.
workbook.close()