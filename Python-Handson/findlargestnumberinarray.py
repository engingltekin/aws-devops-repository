from array import array

data = []
largestNumber = 0
# receive user input
n = int(input('Enter how many elements you want: '))

#loop through user input and built array and find largest number
for i in range(0, n):
    x = input('Enter the numbers into the array: ')
    if (int)(x)>largestNumber:
     largestNumber = (int)(x)
    data.append(x)
    #print both array and largest number
print(data)
print(f'Largest number in the array is {largestNumber}')

