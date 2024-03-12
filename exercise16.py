#User function Template for python3
import unittest

class Solution:
     def reverseWord(self, s: str) -> str:
        #if even, for each 
        chat_list = list(s)
        n=len(chat_list)
        #print(chat_list)
        if n%2==0:
            for i in range(int((n/2))):
                chat_list[i], chat_list[n-i-1] = chat_list[n-i-1], chat_list[i]
                #print(chat_list)
        if n%2==1:
            for i in range((n//2)):
                chat_list[i], chat_list[n-i-1] = chat_list[n-i-1], chat_list[i]
                #print(chat_list)
        s = ''.join(chat_list)
        return s



s="Geeksa"
#print(len(s))
solution=Solution()
print(solution.reverseWord(s))
#print(s)
#print (int((8/2)))



# class Test(unittest.TestCase):
#     def test_reverseWord(self):
#         test_cases = [
#             ("abc", "cba"),
#             ("abcd", "dcba"),
#             ("abcde", "edcba"),
#         ]
#         for input_str, expected_result in test_cases:
#             actual_result = reverseWord(input_str)  # Assuming reverseWordCalculation is defined
#             self.assertEqual(actual_result, expected_result)


# if __name__ == '__main__':
#   unittest.main()




'''
You are given a string s. You need to reverse the string.

Example 1:

Input:
s = Geeks
Output: skeeG
Example 2:

Input:
s = for
Output: rof
Your Task:

You only need to complete the function reverseWord() that takes s as parameter and returns the reversed string.

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).

Constraints:
1 <= |s| <= 10000


'''