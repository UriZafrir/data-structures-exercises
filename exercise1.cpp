#include <iostream>

class Solution {
public:
        long long seriesSum(int n) {
        // Use long long to prevent overflow for large values of n
        return static_cast<long long>(n) * (n + 1) / 2;
    }
};

int main() {
    Solution solution;  // Create an instance of the Solution class
    int n = 10;
    long long result = solution.seriesSum(n);
    std::cout << result << "\n";
    return 0;
}