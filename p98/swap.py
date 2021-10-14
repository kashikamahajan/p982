def swapFiledata():
    fileOne=input("enter name of file one: ")
    fileTwo=input("Enter the name of file two: ")
    a=open(fileOne,'r') 
    data_a=a.read()
    b=open(fileTwo,'r')
    data_b=b.read()

    a=open(fileOne,'w')
    a.write(data_b)

    b=open(fileTwo,'w')
    b.write(data_a)


swapFiledata()