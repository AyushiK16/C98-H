A = 'fileA.txt'
B = 'fileB.txt'
dataA = ''
dataB = ' '

def readData(file1, file2):
    global dataA
    global dataB

    fA = open(file1, 'r')
    fB = open(file2, 'r')

    dataA = fA.read()
    dataB = fB.read()

    print('FileA', dataA)
    print('FileB', dataB)

    file1.write(dataB)
    file2.write(dataA)
    print('FileA', dataA)
    print('FileB', dataB)


    print(dataA, dataB)

def writeData(file1, file2):
    global dataA
    global dataB
    
    file1.write(dataB)
    file2.write(dataA)
    print('FileA', dataA)
    print('FileB', dataB)


readData(A,B)
#writeData(A.B)


'''
readData(A,B)
print('FileA', dataA)
print('FileB', dataB)
writeData(A,B)
print('AFTER SWAP')
print('FileA', dataA)
print('FileB', dataB)

def readText(file):
    global totalCount
    f = open(file, 'r')
    lines = f.readlines()
    for i in lines:
        list = i.split()
        list2 = len(list)
        totalCount = totalCount + list2
            '''