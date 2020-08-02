def avg(listofnumbers):
    total = 0
    lengthoflist=0
    lengthoflist = len(listofnumbers)
    print(lengthoflist)
    for i in listofnumbers:
        print(i)
        total =  total + i
    avg = float(total/lengthoflist)
    print(avg)
    return avg


list = [2,5]
print(avg(list))
