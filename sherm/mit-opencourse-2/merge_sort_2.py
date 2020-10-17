def linear_sort(left_arr, right_arr):
	sorted_arr 	= []
	left_indx 	= 0
	right_indx 	= 0

	while(left_indx < len(left_arr) and right_indx < len(right_arr)):
		if left_arr[left_indx] < right_arr[right_indx]:
			sorted_arr.append(left_arr[left_indx])
			left_indx += 1
		else:
			sorted_arr.append(right_arr[right_indx])
			right_indx += 1

	if left_indx == len(left_arr):
		sorted_arr += right_arr[right_indx:]
	else:
		sorted_arr += left_arr[left_indx:]
	return sorted_arr

def mege_sort_2(arr, start, end):
	if end <= start + 1:
		return

	middle_indx = start + ((end - start) // 2)
	mege_sort_2(arr = arr, start = start, end = middle_indx)
	mege_sort_2(arr = arr, start = middle_indx, end = end)
	arr[start : end] = linear_sort(left_arr = arr[start : middle_indx], right_arr = arr[middle_indx : end])
	return

if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7,1,-10,3,100]  
    print ("Given array is", end ="\n")  
    print(arr) 
    mege_sort_2(arr, start = 0, end = len(arr)) 
    print("Sorted array is: ", end ="\n") 
    print(arr) 