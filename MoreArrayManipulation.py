def findlargest(array):
    largest = array[0]
    samllest = [0]
    for i in range (1,len(array)):
        if array[i] > largest:
            largest = array[i]
            index = i
            print (i)
    return(largest)
found = (findlargest([1,8,4,6,2,7]))
print(found)