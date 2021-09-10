import time




def selection_sort(arr,drawArray,delaytime):

	for i in range(len(arr)):
		min_index = i
		for j in range(i+1,len(arr)):
			if(arr[min_index]>arr[j]):
				min_index = j

			drawArray(arr, ['green' if index <i  else 'yellow'if index == min_index
							else 'red' if index < j
							else 'white' for index in range(len(arr))])
			time.sleep(delaytime)

		arr[i],arr[min_index] = arr[min_index], arr[i]
		# drawArray(arr, ['green' if index <= i  else 'yellow'if index = min_index
		# 					else 'white' for index in range(len(arr))])
		# 	time.sleep(delaytime)

	drawArray(arr,['green' for i in range(len(arr))])	