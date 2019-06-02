import shutil,xlrd,os
file_path="../02.config/testcase.xlsx"
file_path_end="../02.config/testcase_temp.xlsx"
shutil.copyfile(file_path,file_path_end)
excel=xlrd.open_workbook(file_path_end)
sheet=excel.sheets()[0]
print(type(sheet))
print(str(sheet.nrows))
print(str(sheet.ncols))
for i in range(sheet.nrows):
	if sheet.cell(i,0).value==60:
		y=i
		break
for i in range(sheet.ncols):
	if sheet.cell(0,i).value==3:
		x=i
		break
print(y,x)
print(sheet.cell(y,x).value)
os.remove(file_path_end)

