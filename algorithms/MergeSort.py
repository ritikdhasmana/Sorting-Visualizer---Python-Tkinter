import time



def merge(arr, start, mid, end, drawArray, delaytime):
	i = start
	start2 = mid+1
	if(arr[mid]<=arr[start2]):
		return

	while ( start <= mid and start2 <= end) :
		if(arr[start] <= arr[start2]):
			start+=1
			drawArray(arr,['red' if x== i  or x==end else 'yellow' if x==start or x == start2
							else 'white' for x in range(len(arr))])
			time.sleep(delaytime)

		else :
			val  = arr[start2]
			ind = start2
			while(ind!=start) :
				drawArray(arr,['purple' if x == ind  or x == ind - 1 else 'red' if x== i  or x==end 
							else 'yellow' if x==start or x == start2
							else 'white' for x in range(len(arr))])
				time.sleep(delaytime/2)
				arr[ind] = arr[ind-1]
				drawArray(arr,['purple' if x == ind  or x == ind - 1 else 'red' if x== i  or x==end 
							else 'yellow' if x==start or x == start2
							else 'white' for x in range(len(arr))])
				time.sleep(delaytime/2)
				ind-=1
			
			arr[start] =val
			start +=1
			mid +=1
			start2 +=1
			drawArray(arr,['red' if x==i or x==end else 'yellow' if x==start or x == start2
							else 'white' for x in range(len(arr))])
			time.sleep(delaytime)



	#extra space merge sort
	# i = start
	# j = mid + 1
	# temp = []

	# for x in range(start, end+1):
	# 	if i > mid:
	# 		temp.append(arr[j])
	# 		j+=1

	# 	elif j > end :
	# 		temp.append(arr[i])
	# 		i+=1

	# 	elif arr[i] < arr[j]:
	# 		temp.append(arr[i])
	# 		i+=1

	# 	else :
	# 		temp.append(arr[j])
	# 		j+=1

	# for i in range(len(temp)):
	# 	arr[start] = temp[i]
	# 	start+=1










def merge_sort1(arr,start,end, drawArray,delaytime):
	if start < end :
		mid = int((start+end)/2)
		merge_sort1(arr, start, mid, drawArray, delaytime)
		merge_sort1(arr, mid+1, end, drawArray, delaytime)
		drawArray(arr,['green' if x >= start and x < mid else 'yellow' if x==mid
						else 'red' if x > mid and x <= end 
						else 'white' for x in range(len(arr))])
		time.sleep(delaytime)

		merge(arr, start, mid, end, drawArray, delaytime)
		



		

def merge_sort(arr, drawArray, delaytime):
	merge_sort1(arr, 0, len(arr)-1, drawArray, delaytime)
	# print(arr)
	drawArray(arr,['green' for i in range(len(arr))])	

