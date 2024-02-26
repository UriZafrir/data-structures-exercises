/* 
Given an array Arr of N positive integers. Your task is to find the elements whose value is equal to that of its index value ( Consider 1-based indexing ).

Note: There can be more than one element in the array which have the same value as its index. You need to include every such element's index. Follows 1-based indexing of the array.

Example 1:

Input:
N = 5
Arr[] = {15, 2, 45, 12, 7}
Output: 2
Explanation: Only Arr[2] = 2 exists here.
Example 2:

Input: 
N = 1
Arr[] = {1}
Output: 1
Explanation: Here Arr[1] = 1 exists.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function valueEqualToIndex() which takes the array of integers arr[] and n as parameters and returns an array of indices where the given conditions are satisfied. When there is no such element exists then return an empty array of length 0.
*/
#include <iostream>
#include <vector>

class Solution {
public:
    std::vector<int> valueEqualToIndex(int arr[], int n) {
        std::vector<int> result;
        for (int i = 0; i < n; ++i) {
            if (i + 1 == arr[i]) {
                result.push_back(i + 1);
            }
        }
        return result;
    }
};

int main() {
    Solution solution;  // Create an instance of the Solution class
    int n = 4;
    int arr[] = {3, 2, 5, 6};
    std::vector<int> result = solution.valueEqualToIndex(arr, n);
    
    if (result.empty()) {
        std::cout << "No such elements found.\n";
    } else {
        //std::cout << "Elements whose value is equal to their index: ";
        for (int i = 0; i < result.size(); ++i) {
            std::cout << result[i] << " ";
        }
        std::cout << "\n";
    }

    return 0;
}
