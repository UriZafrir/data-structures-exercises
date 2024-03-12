#User function Template for python3
import unittest
class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        M=N
        for i in range(N):
            for j in range(M):
                #count=0
                if A[i]==B[j]:
                    B.pop(j)
                    M-=1
                    break
                if M!=0 and j==(M-1):
                    return 0
        return 1

    


A=[1,2,5,4,0,7,2,12]
B=[2,4,5,0,1,2,20,7]
C=[7,1,2,3,4]
D=[1,2,3,4,7]
N=len(B)
M=len(D)
solution=Solution()
print(solution.check(A,B,N))



# class Solution:
#     #Function to check if two arrays are equal or not.
#     def check(self,A,B,N):
#         for i in range(N):
#             j=0
#             M=len(B)
#             while j<M:
#                 count=0
#                 if A[i]!=B[j]:
#                     j+=1
#                 if A[i]==B[j]:
#                     b.pop(j)
#                     break
#             if count==(N-1):
#                     return 0
#         return 1
#         #return: True or False


# class Test(unittest.TestCase):
#     def test_reverseWord(self):
#         test_cases = [
#             ("abc", "cba"),
#             ("abcd", "dcba"),
#             ("abcde", "edcba"),
#         ]
#         for input_str, expected_result in test_cases:
#             actual_result = check(input_str)  # Assuming reverseWordCalculation is defined
#             self.assertEqual(actual_result, expected_result)


# if __name__ == '__main__':
#   unittest.main()




'''
Given two arrays A and B of equal size N, the task is to find if given arrays are equal or not. Two arrays are said to be equal if both of them contain same set of elements, arrangements (or permutation) of elements may be different though.
Note : If there are repetitions, then counts of repeated elements must also be same for two array to be equal.

Example 1:

Input:
N = 5
A[] = {1,2,5,4,0}
B[] = {2,4,5,0,1}
Output: 1
Explanation: Both the array can be 
rearranged to {0,1,2,4,5}
Example 2:

Input:
N = 3
A[] = {1,2,5}
B[] = {2,4,15}
Output: 0
Explanation: A[] and B[] have only 
one common value.
Your Task:
Complete check() function which takes both the given array and their size as function arguments and returns true if the arrays are equal else returns false.The 0 and 1 printing is done by the driver code.

Expected Time Complexity : O(N)
Expected Auxilliary Space : O(N)

Constraints:
1<=N<=107
1<=A[],B[]<=1018

 


'''