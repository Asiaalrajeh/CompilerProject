
from tkinter import *
from tkinter import ttk
import json
from NFA_And_DFA import *
from RE_To_DFA import CalcDfa
from PIL import Image, ImageTk
global u


def NFa():
 nfaObj = NFAfromRegex(u.get())
 nfa = nfaObj.getNFA()
 print ("\nNFA: ")
 nfaObj.displayNFA()
 Button(root, text="Convert to DFA", width=15, command = DFa, fg="red").place(x=90, y=230)
   


def DFa():
 nfaObj = NFAfromRegex(u.get())
 nfa = nfaObj.getNFA()
 dfaObj = DFAfromNFA(nfa)


 print ("\nDFA: ")
 dfaObj.displayDFA()

def ReDfa():
 z = open("input.txt","w")
 z.write(u.get())
 z.close()
 CalcDfa()
#  image = Image.open('dfa.png')
#  i = ImageTk.PhotoImage(image)
#  c = Canvas(root, width=300, height=400)
#  c.pack()
#  c.create_image(0,0, image=i , anchor="nw")
#  l = Label(root,image=i)
#  l.pack()



root = Tk()
root.title('compiler project') 
root .geometry("300x400")
root.configure(bg='lightBlue')
u = StringVar()




Label(root, text=" Enter Regex").place(x=120,y=70)
x = Entry(root , textvariable= u).place(x=90,y=90)
Button(root, text="Convert to NFA", width=15, command = NFa, fg="navy").place(x=90, y=130)
Label(root, text= "OR").place(x=140,y=160)
Button(root, text="Convert REG to DFA", width=20, command = ReDfa, fg="navy").place(x=90, y=190)



root.mainloop()


