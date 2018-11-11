import time
import webbrowser

break_time = 0
print("This program started on "+ time.ctime())
#play video after every 2hrs
while(break_time < 3):
	time.sleep(2*60*60) #time in seconds
	webbrowser.open("https://www.youtube.com/watch?v=-qlJiGGvPUI")
	break_time +=1;
