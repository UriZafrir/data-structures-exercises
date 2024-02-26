
### Exercise 2: Lists and Sorting

#### Problem:
#Write a Python function that takes a list of integers as input and returns a new list with the elements sorted in non-decreasing order.

#### Example:
def sort_numbers(numbers):
    for i in range(1, len(numbers)):
        if numbers[i]<numbers[i-1]:
            print("one")
            print(numbers[i])
            print(numbers[i-1])
            numbers[i], numbers[i-1] = numbers[i-1], numbers[i]
            print(numbers[i])
            print(numbers[i-1])
    return numbers

numbers = [5, 2, 9, 1, 5, 6]
result = sort_numbers(numbers)
print(result)  # Output: [1, 2, 5, 5, 6, 9]

#first idea - take second number, if it's bigger than first then keep it. otherwise replace first with second
#then take 3rd number, if it's bigger than 2nd keep it,
#rule - take number in location 0+n
# i=1
#for i in numbers(count)
#
