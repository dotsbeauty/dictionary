import json
from tkinter import *
from tkinter import messagebox
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate():
	word = x1.get()
	word = word.lower()
	if word in data:
		return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	elif len(get_close_matches(word, data.keys())) > 0:
		decide = messagebox.askquestion('Not Found', "did you mean {} instead".format(get_close_matches(word, data.keys())[0]))
		if decide == "yes":
			e1.delete("0",END)
			e1.insert("0",get_close_matches(word, data.keys())[0])
			return data[get_close_matches(word, data.keys())[0]]
		else:
			return word + " not found"
	else:
		return word + " not found"

def show():
	e2.delete('1.0', END)
	meaning = translate()
	if type(meaning) == list:
		for each in meaning:
			e2.insert(END,each)
	else:
		e2.insert(END,meaning)

def show_mng(event = None):
	show()
win = Tk()
win.title("Dictionary")
win.configure(bg="thistle1")
win.geometry('450x300')

l1 = Label(win, text = "Enter word",font = ('calibri', 12), background = "thistle1")
l1.grid(row = 1, column = 0, sticky = W)

l2 = Label(win, text = "Meaning",font = ('calibri', 12), background = "thistle1")
l2.grid(row = 2, column = 0,sticky = W)

x1 = StringVar()
e1 = Entry(win,textvariable = x1)
e1.grid(row = 1, column = 2,sticky = W)

e2 = Text(win, height = 10, width=40, wrap= WORD)
e2.grid(row = 2, column = 2,sticky = W)

Button(win, text='Quit',command=win.destroy).grid(row=3, column=2,sticky = W)
Button(win, text='Show', command=show).grid(row=3, column=0, sticky = W)

win.bind('<Return>', show_mng)
win.mainloop()