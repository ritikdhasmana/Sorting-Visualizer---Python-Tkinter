import time 


def insertion_sort(arr,drawArray,delaytime):
	for i in range(1,len(arr)):
		val = arr[i]
		j = i-1
		while j>-1 and val < arr[j] :
			drawArray(arr, ['yellow'if index == j or index ==j+1 else 'red' if index <=i
							else 'white' for index in range(len(arr))])
			time.sleep(delaytime/2)
			arr[j+1] = arr[j]
			
			drawArray(arr, ['yellow'if index == j or index ==j+1 else 'red' if index <=i
							else 'white' for index in range(len(arr))])
			time.sleep(delaytime/2)
			j-=1

		drawArray(arr, ['green' if index <i
							else 'white' for index in range(len(arr))])
		time.sleep(delaytime)
		arr[j+1] =val


	drawArray(arr,['green' for i in range(len(arr))])	

