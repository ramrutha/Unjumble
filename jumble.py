#!/usr/bin/python

import sys

import Tkinter as tkinter
import tkFont

top = tkinter.Tk()
top.title("JUMBLE")
top.geometry("500x500")

photo = tkinter.PhotoImage(file = "jumb.gif")
ph = tkinter.Label(top, image=photo)
ph.place(x=0, y=0, relwidth=1, relheight=1)
helv36 = tkFont.Font(family="Helvetica", size=36, weight='bold')
lab = tkinter.Label(top, text = "Jumbled word", font = helv36, bg ='#000', fg='#fff', padx=2, pady=2)
lab.pack()

helv25 = tkFont.Font(family="Helvetica", size=25, weight='bold')
w = tkinter.Entry(top,bd = 5, font=helv25)
w.pack()

def getData():
	var = w.get()
	#var = raw_input("Enter the jumbled word\n")
	#print ("the first argument is %s" % str(sys.argv[1]))
	leng = len( var )
	#print ( leng )
	temp = open('d.txt','w+')
	with open('wordsEn.txt','rt') as f:
		for line in f:
			l = len( line )
			if l == leng+2:
				temp.write(line)
		temp.close()
	f.close()	
	#sort the input string
	b = sorted(var)
	c = ''.join(b)
	#print c

	with open('d.txt','rt') as f1:
		for line in f1:
			line = ''.join(line.splitlines())
			#if var == line:
				#print line
			t = sorted(line)
			p = ''.join(t)
			flag = 0
			for i in xrange(leng):
				if(p[i] != c[i]):	
					flag=1	
					break
			if flag==0:
				tex = tkinter.Label( top, text=line, font=helv25, bg ='#000', fg='#fff')
				tex.pack()		
		f1.close()
	
btn = tkinter.Button(top,text = "Unjumble",pady=10, font=helv25, command = getData)
btn.pack()

top.mainloop()

