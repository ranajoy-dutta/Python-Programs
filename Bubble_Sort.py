"Program to perform Bubble Sort"
def Bubble_Sort(array):
    for j in range(len(array)-1,0,-1):
        for i in range(j):
            if array[i]>array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp

array = list(map(int,input("Enter the elements in line separated by space:").split()))
Bubble_Sort(array)
print(array)
