#for a given array check if all elements are palindrome. if not then output 0
def PalinArray(arr ,n):
    for i in range(n):
        separated_digits = [int(a) for a in str(arr[i])]
        #print(separated_digits)
        if is_palindrome(separated_digits) != True:
            return 0
            break
        #else:
            #print("the same")
    #print ("1")
    return 1

#check if all elements in list are the same
def is_palindrome(list):
    list_length = len(list)
    #print(list_length)
    # Use a loop to compare elements
    # for even length:
    for i in range(list_length // 2):
    # Compare corresponding elements
        first_element = list[i]
        #print(first_element)
        last_element = list[list_length - 1 - i]
        #print(last_element)
        if first_element != last_element:
            #print("different!")
            return 0
            break
    return 1


n=5
arr=[12121,232,343,444,6556]
PalinArray(arr,n)