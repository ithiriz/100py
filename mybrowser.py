import youtube_dl
import urllib
import shutil
import webbrowser
import tkinter
from tkinter import filedialog
from tkinter import *
from googlesearch import search
root=Tk()
root.geometry("630x150")
root.title('Finder')
root.configure(bg='#fcfcec')
L1=Label(root,text="Find words :- ",bg='#fcfcec',fg="#4b7fa4",font=("time",20))
e=Entry(root,width=100,bg="white",fg="#cb464e",border=10)
def pas():
    for j in search(e.get(),tld="co.in",num=10,stop=10, pause=3):
        webbrowser.open(j)

mybutton=Button(root,text="Search",bg="#cb464e",fg="#fcfcec",command=pas,font=("time",20))
L1.grid(row=0,column=0)
e.grid(row=1,column=0)
mybutton.grid(row=2,column=0)
root.mainloop()
