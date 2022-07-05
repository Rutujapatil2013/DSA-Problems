#FIRST SOLUTION   
# Time complexity - O(n^2)
# Space complexity - O(1)
arr = [1, 2, 3, 4, 7, 2,8, 8, 3]
n=len(arr)
print('The duplicate element in array is: ')
for i in range(n):
    for j in range(i+1,n):
        if arr[i]==arr[j]:
            print(arr[i])
          
             
#SECOND SOLUTION  
            
            
            
            
