import time 



def partition(arr,start,end,drawArray, delaytime):
	piv_ind = start
	pivot = arr[start]
	i = start
	j = end 
	while i < j :

		while i < len(arr) and arr[i] <= pivot :
			
			drawArray(arr,['red' if x ==start or x==end  else 'yellow' if x== i 
							else 'white' for x in range(len(arr))])
			time.sleep(delaytime)
			i+=1
		while  arr[j] > pivot :
			
			drawArray(arr,['red' if x ==start or x==end  else 'yellow' if x== j
							else 'white' for x in range(len(arr))])
			time.sleep(delaytime)
			j-=1

		if(i<j) :
			
			drawArray(arr,['red' if x ==start or x==end  else 'purple' if x== i or x == j
							else 'white' for x in range(len(arr))])
			arr[i],arr[j] = arr[j], arr[i]
			time.sleep(delaytime/2)
			drawArray(arr,['red' if x ==start or x==end  else 'purple' if x== i or x == j
							else 'white' for x in range(len(arr))])
			time.sleep(delaytime/2)
			
	drawArray(arr,['purple' if x== piv_ind or x == j
							else 'white' for x in range(len(arr))])
	time.sleep(delaytime/2)
	arr[j],arr[piv_ind] = arr[piv_ind], arr[j]
	drawArray(arr,['purple' if x== piv_ind or x == j
							else 'white' for x in range(len(arr))])
	time.sleep(delaytime)
	return j 








def quick_sort1(arr,start,end,drawArray,delaytime):
	if(start < end):
		drawArray(arr,['red' if x ==start or x==end 
							else 'white' for x in range(len(arr))])
		time.sleep(delaytime)
		p = partition(arr,start,end,drawArray,delaytime)

		quick_sort1(arr, start, p-1, drawArray, delaytime)
		quick_sort1(arr, p+1, end, drawArray, delaytime)




def quick_sort(arr,drawArray,delaytime):
	quick_sort1(arr,0,len(arr)-1,drawArray,delaytime)
	drawArray(arr,['green' for i in range(len(arr))])	
