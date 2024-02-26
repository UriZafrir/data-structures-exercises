def printAl(arr, n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(arr[i])
    result_string = ' '.join(map(str, result))
    print(result_string)

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(arr)
printAl(arr, n)