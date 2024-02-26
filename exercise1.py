
#### Problem:
#Write a Python function that takes a list of numbers as input and returns the sum of all even numbers in the list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sum_of_evens(numbers):
    sum_evens = 0
    for num in numbers:
        if num % 2 == 0:
            sum_evens = sum_evens + num
    return(sum_evens)

result = sum_of_evens(numbers)
print(result)  # Output: 30
