

class Solution:
    def _sum(self, arr, n):
        total_sum = 0
        for i in range(len(arr)):
            total_sum+=arr[i]
            pass
        return total_sum





solution=Solution()
arr=[1, 2, 3, 4]
n=len(arr)
print(solution._sum(arr, n))


'''
Given an integer array arr[] of size n. The task is to find sum of it.

Example 1:

Input:
n = 4
arr[] = {1, 2, 3, 4}
Output: 10
Explanation: 1 + 2 + 3 + 4 = 10.
Example 2:

Input:
n = 3
arr[] = {1, 3, 3}
Output: 7
Explanation: 1 + 3 + 3 = 7.
Your Task:
Complete the function sum() which takes array arr and single integer n, as input parameters and returns an integer denoting the answer. You don't have to print answer or take inputs.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= n <= 105
1 <= arr[i] <= 104

 
'''