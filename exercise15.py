

class Solution:    
    def doUnion(self,a, n, b, m):
        # Using a set to store distinct elements
        union_set = set()

        # Adding elements from array 'a' to the set
        for i in range(n):
            union_set.add(a[i])

        # Adding elements from array 'b' to the set
        for i in range(m):
            union_set.add(b[i])

        # Returning the count of distinct elements in the union set
        return len(union_set)


s=Solution()
# Example usage:
a1 = [1, 2, 3, 4, 5]
b1 = [1, 2, 3]
print(s.doUnion(a1, 5, b1, 3))  # Output: 5

a2 = [85, 25, 1, 32, 54, 6]
b2 = [85, 2]
print(s.doUnion(a2, 6, b2, 2))  # Output: 7

'''
a=[5,3,60,50]
b=[1,2,3,4,5,6,13,22,25]
n=len(a)
m=len(b)
s=Solution()
print(s.doUnion(a,n,b,n))
'''
'''
        result=a+b
        result_range=range(len(result))
        for i in range(len(result)):
            if i>result_range:
                break
            for j in range(len(result)):
                if j>result_range:
                    break
                #print(result[i],result[j])
                if j==i:
                    continue
                if result[j]==result[i]:
                    result.pop(j)
                    result_range=range(len(result))
        return result

'''


'''
Given two arrays a[] and b[] of size n and m respectively. The task is to find the number of elements in the union between these two arrays.

Union of the two arrays can be defined as the set containing distinct elements from both the arrays. If there are repetitions, then only one occurrence of element should be printed in the union.

Note : Elements are not necessarily distinct.

Example 1:

Input:
5 3
1 2 3 4 5
1 2 3
Output: 
5
Explanation: 
1, 2, 3, 4 and 5 are the
elements which comes in the union set
of both arrays. So count is 5.
Example 2:

Input:
6 2 
85 25 1 32 54 6
85 2 
Output: 
7
Explanation: 
85, 25, 1, 32, 54, 6, and
2 are the elements which comes in the
union set of both arrays. So count is 7.
Your Task:
Complete doUnion function that takes a, n, b, m as parameters and returns the count of union elements of the two arrays. The printing is done by the driver code.

Constraints:
1 ≤ n, m ≤ 105
0 ≤ a[i], b[i] < 105

Expected Time Complexity : O(n+m)
Expected Auxilliary Space : O(n+m)

'''