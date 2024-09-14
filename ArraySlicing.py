array = [1,2,3,4,5,6,7,8]
half1 = []
half2 = []
mid = (len(array) + 1) // 2
half1 = array[:mid]
half2 = array[mid:]
print(half1, half2)