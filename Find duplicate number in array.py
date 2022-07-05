
numRay = [0, 4, 3, 2, 7, 8, 2, 3, 1]
arr_size = len(numRay)
for i in range(arr_size):
    x = numRay[i] % arr_size
    numRay[x] = numRay[x] + arr_size
print("The repeating elements are : ")
for i in range(arr_size):
    if (numRay[i] >= arr_size*2):
        print(i, " ")
 
Output: 
The repeating elements are : 
2 
3

Complexity Analysis: 
Time Complexity: O(n). 
Only two traversals are needed. So the time complexity is O(n).
Auxiliary Space: O(1). 
No extra space is needed, so the space complexity is constant.

##############################################################################  
# Time complexity - O(n^2)
# Space complexity - O(1)
code:)
arr = [1, 2, 3, 4, 7, 2,8, 8, 3]
n=len(arr)
print('The duplicate element in array is: ')
for i in range(n):
    for j in range(i+1,n):
        if arr[i]==arr[j]:
            print(arr[i])
  
######################################################################################

             
#SECOND SOLUTION  
Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
Output : output_list = [20, 30, -20, 60]
Method 1: Using the Brute Force approach  
Code:)
# Python program to print
# duplicates from a list
# of integers
def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated
# Driver Code
list1 = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]
print (Repeat(list1))


######################################################################################
#THIRD SOLUTION
Method 2: Using Counter() function from collection module
Code:)
from collections import Counter
l1 = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
d = Counter(l1)
print(d)
new_list = list([item for item in d if d[item]>1])
print(new_list)
Output
Counter({1: 4, 2: 3, 5: 2, 9: 2, 3: 1, 4: 1, 6: 1, 7: 1, 8: 1})
        [1, 2, 5, 9]

    

####################################################################    
Method 3: Using count() method
# program to print duplicate numbers in a given list
# provided input
list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
new = []  # defining output list
# condition for reviewing every
# element of given input list
for a in list:
     # checking the occurrence of elements
    n = list.count(a)
    # if the occurrence is more than
    # one we add it to the output list
    if n > 1:
        if new.count(a) == 0:  # condition to check
            new.append(a)
print(new)

######################################################################################
def duplicate(arr):
    n=len(arr)
    d={}
    for i in arr:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
        
    for key,val in d.items():
        if val>1:
            print(key,end=' ')
            
    
arr= [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
print('Duplicate elements is: ',end=' ')
duplicate(arr)

######################################################################################
    

            
            
            
            
