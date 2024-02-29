

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        '''
        if element is in a and not in b then add to result, if element is in both a and b add to result, if element is in b and not in a then add to result
        otherwise, add all elements to array, then check for duplicates.
        connect a+b, its 1,2,3,4,5,5,3
        for first element i=0, for each element of array except i=j check if result[i]==result(j), if yes remove result(j) and update len(result)
        '''
        result=a+b
        result_range=range(len(result))
        for i in range(len(result)):
            if i>result_range[-1]:
                break
            for j in range(len(result)):
                if j>result_range[-1]:
                    break
                #print(result[i],result[j])
                if j==i:
                    continue
                if result[j]==result[i]:
                    result.pop(j)
                    result_range=range(len(result))
        return len(result)


a=[5,3,60,50]
b=[1,2,3,4,5,6,13,22,25]
n=len(a)
m=len(b)
s=Solution()

print(s.doUnion(a,n,b,n))
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