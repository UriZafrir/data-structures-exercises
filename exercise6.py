#Given a non-negative integer num, repeatedly add all its digits until the result has only
#one digit.
#For example:
#Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit,
#return it.

def add_digits(number):
    #print(number)
    sum_of_number=sum_up_digits(number)
    #print(sum_of_number)
    if sum_of_number < 10:
        #print("smaller than 10")
        #print(sum_of_number)
        return sum_of_number
    else:
        #print("bigger than 10")
        return add_digits(sum_of_number)

def sum_up_digits(number):
    # Convert the number to a string
    num_str = str(number)
    # Initialize a variable to store the sum
    digit_sum = 0
    # Iterate through each digit in the string and add it to the sum
    for digit in num_str:
        digit_sum += int(digit)
    return digit_sum

number=38
print(add_digits(number))