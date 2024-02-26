
'''
printPat should receive a number. 
number of repeats should equal that number.
then it inputs the number and the number of repeats to inner function
then does the same with less repeats
call oneline(n, number of repeats)
call oneline(n, number of repeats-1)
repeat until number of repeats is smaller than 1
'''
def printPat(n):
    number_of_repeats=n
    for i in range (number_of_repeats, 0, -1):
        oneline(n, number_of_repeats)
        number_of_repeats-=1
        print("$", end="")
    

'''
oneline should get a number and decide to print it
several times depending on another number.
that means - print number exactly number of repeats, 
subtract number by 1, then print it number of repeats,
until number =1
'''
def oneline(n, number_of_repeats):
    for j in range(n, 0, -1):
        for k in range(number_of_repeats):
            print(n, end=" ")
        n-=1

n=1
printPat(n)
#number_of_repeats=3
#oneline(n, number_of_repeats)
'''
def printPat(n):
    for i in range(n, 0, -1):
        #for i in range
        oneline(i)

'''
'''
def oneline(n):
    for i in range(n, 0, -1):
        for j in range(n):
            print(i, end=" ")
    print()

def oneline2(n, number_of_repeats):
    for i in range(number_of_repeats):
        for j in range(n):
            print(n, end=" ")
        print(n, end=" ")
'''
'''
need to print additional numbers
'''

#oneline2(n, number_of_repeats)
#i need instead of 2 2 1 1 to get 3 3 2 2 1 1
#the function oneline should
#each line prints
'''
oneline should get a number and decide to print it
several times depending on another number.
that means - print number exactly number of repeats, 
subtract number by 1, then print it number of repeats,
until number =1

def oneline(n, number_of_repeats):
    for n in range(number_of_repeats):
        for i in range(number_of_repeats):
            print(n, end=" ")
        n-=1
if getting 3 it should output
3 3 3 2 2 2 1 1 1 
or 
3 3 2 2 1 1
so it should get another parameter - number of repeats




so outer function should receive a number. number of repeats should equal that number.
then it inputs the number and the number of repeats to inner function
then does the same with less repeats
def printPat(n):
    number_of_repeats=n
    for i in range (number_of_repeats, 1, -1)
        oneline(n, number_of_repeats)


def oneline(n):
    number_of_repeats=n
    for number_of_repeats:
        print n
'''


'''
while n>0:
    repeat=n
    while repeat > 0:
        #print n "repeat" times
        for j in range(repeat):
            print(repeat, end=" ")
        repeat -= 1
        n -= 1
'''

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