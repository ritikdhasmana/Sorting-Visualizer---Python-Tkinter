from tkinter import *
from tkinter import ttk
import random
import sys
# sys.setrecursionlimit(100000000)

from algorithms.BubbleSort import bubble_sort
from algorithms.MergeSort import merge_sort
from algorithms.SelectionSort import selection_sort
from algorithms.InsertionSort import insertion_sort
from algorithms.QuickSort import quick_sort

# background_colour = ((0,0,0))
# (screen_width, Screen_height) = (1100, 600)
screen = Tk()
screen.title('Sorting Visualizer')
screen.geometry('1100x600')
screen.config(bg = 'black')
screen.resizable(True,True)




cur_algo = StringVar()
all_algo = ['Bubble Sort','Selection Sort', 'Insertion Sort' ,'Merge Sort','Quick Sort']
sort_speed = StringVar()
all_speeds = ['Super fast' ,'Fast','Medium', 'Slow']
arraysize = StringVar()
sizerange = [10,20, 40, 60, 80, 100, 120, 140]


myarray = []

#funtion for sort speed
def set_speed():
	if menu2.get() == 'Slow':
		return 0.66000
	elif menu2.get() ==  'Medium':
		return 0.1
	elif menu2.get() == 'Fast' :
		return 0.01
	else :
		return 0.0002



# This function will draw randomly generated list 
def drawArray(myarray, color):
	canvas.delete('all')
	canvas_width = 1080
	canvas_height = 475
	bar_width = canvas_width/(len(myarray)+1)
	offset = 5
	space = 2
	newarray = [ i/max(myarray) for i in myarray]

	for i, bar_ht in enumerate(newarray):
		x0 = i*bar_width + offset +space
		y0 = canvas_height - bar_ht*440
		x1 = (i + 1) * bar_width + offset + space
		y1 = canvas_height
		canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])

	screen.update()


def generateArray():
	global myarray
	myarray = []
	arraysize = menu3.get()
	for i in range (0 , int(arraysize)):
		val = random.randint(1, 400)
		while (val in myarray) :
			val = random.randint(1, 400)
		myarray.append(val)

	# print(myarray)
	drawArray((myarray),[ 'white' for i in range(len(myarray))])




# This function will generate array with random values every time we hit the generate button
def sortArray():
	global myarray
	delaytime  = set_speed()
	print(delaytime)
	print(menu2.get())
	print(menu1.get())
	if menu1.get() == 'Bubble Sort':
		bubble_sort(myarray, drawArray, delaytime)

	elif menu1.get() == 'Merge Sort':
		merge_sort(myarray, drawArray, delaytime)
	elif menu1.get() == 'Selection Sort':
		selection_sort(myarray, drawArray, delaytime)
	elif menu1.get() == 'Insertion Sort':
		insertion_sort(myarray, drawArray, delaytime)
	elif menu1.get() == 'Quick Sort':
		quick_sort(myarray, drawArray, delaytime)	



#GUI

GUI_FRAME = Frame(screen,width = 1200, height = 500, bg = 'black')
GUI_FRAME.grid(row=0,column=0,padx = 0,pady=7)


label1 = Label(GUI_FRAME, text = 'Algorithm: ', bg = 'white')
label1.grid(row=0, column=0, padx=17, pady=7, sticky=W)
menu1 = ttk.Combobox(GUI_FRAME,textvariable =cur_algo)
menu1['values'] = all_algo
menu1['state'] = 'readonly'  # normal
menu1.grid(row =0,column=1, padx=10, pady=7)
menu1.current(0)

label2 = Label(GUI_FRAME, text = 'Sort Speed: ', bg = 'white')
label2.grid(row=1, column=0, padx=17, pady=7, sticky=W)
menu2 = ttk.Combobox(GUI_FRAME,textvariable =sort_speed)
menu2['values'] = all_speeds
menu2['state'] = 'readonly'  # normal
menu2.grid(row =1,column=1, padx=10, pady=7)
menu2.current(3)


button1 = Button(GUI_FRAME,text = 'Sort', command = sortArray, bg = 'white',height = 1, width = 7)
button1.grid(row =1, column = 3, padx = 10, pady = 7)
button1 = Button(GUI_FRAME,text = 'Generate Array', command = generateArray, bg = 'white')
button1.grid(row =1, column = 4, padx = 10, pady = 7)





canvas = Canvas(screen, width=1070, height=475, bg= 'black')
canvas.grid(row=1, column=0, padx=10, pady=5)


Label(GUI_FRAME, text="Array Size", bg='white').grid(row=0, column=3, padx=10, pady=7, sticky=W)
menu3 = ttk.Combobox(GUI_FRAME,textvariable =arraysize)
menu3['values'] = sizerange
menu3['state'] = 'readonly'  # normal
menu3.grid(row =0,column=4, padx=10, pady=7)
menu3.current(2)






screen.mainloop()



