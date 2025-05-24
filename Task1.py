try:
    file1 = open('sample.txt','r')
    print("R`eading file content:")
    print("Line1: ",file1.readline())
    print("Line2: ",file1.readline())
    file1.close()
except FileNotFoundError:
    print("ERROR: The file 'sample.txt' was not found")
