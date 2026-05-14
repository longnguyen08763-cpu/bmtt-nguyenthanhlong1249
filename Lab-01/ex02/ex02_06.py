input_str = input("nhập x,Y:")
dimensions=[int(x)for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multillist = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multillist [row][col]= row*col
print (multillist)