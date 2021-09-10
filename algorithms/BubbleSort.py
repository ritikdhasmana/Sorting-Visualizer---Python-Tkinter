import time
# import sounddevice as sd
# import numpy as np 
# from math import pi

def bubble_sort(arr,drawArray,delaytime):
	sz = len(arr)
	for i in range (sz-1):
		for j in range (sz -i -1):
			if arr[j] > arr[j+1]:
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
				drawArray(arr, ['red' if index == j or index == j+1 else 'white' for index in range(len(arr))])
		
				time.sleep(delaytime)

	drawArray(arr,['green' for i in range(len(arr))])	