
class Solution:	
    def binarysearch(self, arr, n, k):
        '''what happens to the index when i cut the array? for array of n=3, cutting down (elements are 1 and 2), index stays the same. cutting up, index is pushed to 2 that means to (n/2)+1
        
        explanation for {1 2 3 4 5} - take middle element arr[n//2], is arr[n/2]<k ? if yes, then arr=arr[n/2+1, n], n=len(arr). else arr=arr[0,n/2], n=les(arr).
        take array which is arr=[4,5]. since it's even, take element in n/2
        if n=2, if arr[0]=k then return(original_array.index(k)), else return
        if array is odd and different than 1(for example n=3 (0,1,2)), take middle element (n/2), if that elements is smaller than k then arr=arr[n/2,n], n=len(arr). if array is 1 then k=
        if array is even (for example n=4(0,1,2,3)), if arr[(n/2)-1]<k then index+=n/2, arr=arr[n/2,n], n=len(arr), else arr=arr[0,(n/2)-1], n=len(arr)
        '''
        index=0
        if k>arr[-1] or k<arr[0]:
            return -1
        while len(arr)>2:
            #odd
            if len(arr)%2==1 and len(arr)!=2:
                if arr[(n//2)]<k:
                    index+=(n//2)+1
                    arr=arr[(n//2)+1:n]
                    n=len(arr)
                else:
                    arr=arr[0:n//2+1]
                    n=len(arr)
            #even
            if len(arr)%2==0 and len(arr)!=2:
                if arr[(n//2)-1]<k:
                    index+=n//2
                    arr=arr[n//2:n]
                    n=len(arr)
                else: 
                    arr=arr[0:(n//2)]
                    n=len(arr)
        if len(arr)==2:
            if arr[0]==k:
                return(index)
            elif arr[1]==k:
                return(index+1)
            else:
                return -1
        elif len(arr)==1:
            if arr[0]==k:
                return(index)
            else:
                return -1



arr=[1, 2, 3, 4, 5, 6, 8, 9,10,20,30,40,50,60]
n=len(arr)
k=7
s=Solution()

print(s.binarysearch(arr,n,k))








'''
Given a sorted array of size N and an integer K, find the position(0-based indexing) at which K is present in the array using binary search.

Example 1:

Input:
N = 5
arr[] = {1 2 3 4 5} 
K = 4
Output: 3
Explanation: 4 appears at index 3.

Example 2:

Input:
N = 5
arr[] = {11 22 33 44 55} 
K = 445
Output: -1
Explanation: 445 is not present.

Your Task:  
You dont need to read input or print anything. Complete the function binarysearch() which takes arr[], N and K as input parameters and returns the index of K in the array. If K is not present in the array, return -1.


Expected Time Complexity: O(LogN)
Expected Auxiliary Space: O(LogN) if solving recursively and O(1) otherwise.


Constraints:

1 <= N <= 105
1 <= arr[i] <= 106
1 <= K <= 106

'''