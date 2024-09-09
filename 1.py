#Qestion 1

import numpy as np

arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1)
sum1=0
for i in range(0,3):
    sum1=sum1+arr1[i][i]
    
print("The sum of the Diagonal Elements of the array is :",sum1)