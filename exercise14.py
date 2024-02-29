class Solution:
    def isPowerofTwo(self,n):
        return n > 0 and (n & (n - 1)) == 0

n=549755813888
s=Solution()
print(s.isPowerofTwo(n))


'''
a=b^x
log(b)a=x
'''

'''
Given a non-negative integer N. The task is to check if N is a power of 2. More formally, check if N can be expressed as 2x for some integer x. Return true if N is power of 2 else return false.

Example 1:

Input: 
N = 8
Output: 
YES
Explanation:
8 is equal to 2 raised to 3 (23 = 8).
Example 2:

Input: 
N = 98
Output: 
NO
Explanation: 
98 cannot be obtained by any power of 2.
Your Task:Your task is to complete the function isPowerofTwo() which takes n as a parameter and returns true or false by checking if the given number can be represented as a power of two or not.

Expected Time Complexity:O(log N).
Expected Auxiliary Space:O(1).

Constraints:
0 ≤ N < LLONG_MAX


'''