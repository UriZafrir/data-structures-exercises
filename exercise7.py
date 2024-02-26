
def printPat(n):
    #for each line
    for i in range(n):
        #in first line, as long as n<0 print n times the n, then n-1 times (n-1)
        while n>0:
            repeat=n
            while repeat > 0:
                #print n "repeat" times
                for j in range(repeat):
                    print(repeat, end=" ")
                repeat -= 1
                n -= 1


    #i need a line for each number
    #each number should appear as many times as the number on the first line
    # then second line one time less etc
    
n=3
printPat(n)


"""
You are given a number N. You need to print the pattern for the given value of N.

For N = 2 the pattern will be 
2 2 1 1
2 1

For N = 3 the pattern will be 
3 3 3 2 2 2 1 1 1
3 3 2 2 1 1
3 2 1

Note: Instead of printing a new line print a "$" without quotes. After printing the total output, end of the line("$") is expected.

Example 1:

Input: 2
Output:
2 2 1 1 $2 1 $

Example 2:

Input: 3
Output:
3 3 3 2 2 2 1 1 1 $3 3 2 2 1 1 $3 2 1 $

Your Task:
Since this is a function problem, you don't need to worry about the test cases. Your task is to complete the function printPat() which takes one argument 'N' denoting the length of the pattern.

"""