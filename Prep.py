import random
frequency=[0]*10

for i in range(200):
    num = random.randint(1,10)
    frequency[num-1] = frequency[num-1] +1

print('The extpected frequency is 20')
print('Number','Frequency','Difference')

for i in range(10):
    print(i+1,' ',frequency[i],' ',20-frequency[i])
