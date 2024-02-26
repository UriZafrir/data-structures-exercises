#Given an array Arr of N positive integers. Your task is to find the elements whose value is equal to that of its index value ( Consider 1-based indexing ).

#User function Template for python3

def valueEqualToIndex(arr, n):
	result=[]
	for i in range(1,n):
		if arr[i]==i:
			result.append(arr[i])
	return result


n=5
arr = [15, 1, 45, 12, 7]
valueEqualToIndex(arr,n)