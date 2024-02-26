import math
class Solution:
    
    def find_median(self, v):
        self.bubbleSort(v)
        lstLen = len(v)
        index = (lstLen - 1) // 2
        if (lstLen % 2):
            return math.floor(v[index])
        else:
            return math.floor((v[index] + v[index + 1]) / 2)
    
    def bubbleSort(self, arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

 
# Driver code to test above
n=5
arr = [90, 100, 78, 89, 67] 
#bubbleSort(arr)
find_median(arr)


'''
Given an array arr[] of N integers, calculate the median.

NOTE: Return the floor value of the median.
 

Example 1:

Input: N = 5
arr[] = 90 100 78 89 67
Output: 89
Explanation: After sorting the array 
middle element is the median 
'''