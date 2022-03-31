
def swapFileData():
    file1 = open('sample1.txt')
    file2 = open('sample2.txt')
    data_a = file1.read()
    data_b = file2.read()
    file1 = open('sample1.txt', 'w')
    file2 = open('sample2.txt', 'w')
    file1.write(data_b)
    file2.write(data_a)
    print(data_a)
    print(data_b)


swapFileData()

