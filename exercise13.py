
class Solution:	
    def binarysearch(self, arr, n, k):
        '''
        if array has 4 elements, n=4, mid=1, if k is bigger than mid 
        '''
        start=0
        end=n-1
        while start<=end:
            mid=(start+end)//2
            if arr[mid]==k:
                return mid
            elif arr[mid]<k:
                start=mid+1
            elif arr[mid]>k:
                end=mid-1
        return -1


arr=[1, 2, 3, 4, 5, 6, 8, 9,10,20,30,40,50,60]
n=len(arr)
k=8
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