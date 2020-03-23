from tkinter import *

flag =0
def add(text):
    global flag
    if flag == 1:
        clear()
    txt = nText.get()
    if txt == "Error":
        nText.set(text)
    else:
        nText.set(txt+text)
    flag = 0
def clear():
    nText.set("")

def backspace():
    nText.set(nText.get()[:-1])

def cal():
    global flag
    flag = 1
    try:
        nText.set(eval(nText.get()))
    except:
        nText.set("Error")


root = Tk()
root.title("Cal")
#root.iconbitmap(r"")
nText = StringVar()

et=Entry(root, textvariable=nText, justify=RIGHT, width=20, font="Arial 20")
et.grid(row=0, column=0, columnspan=4,padx=10,pady=10)
Button(root, text="<", command=backspace, width=20).grid(row=1, column=0, columnspan=2, sticky=W+E)
Button(root, text="C", command=clear, width=20).grid(row=1, column=2, columnspan=2, sticky=W+E)
Button(root, text="1", command=lambda: add("1")).grid(row=2, column=0,sticky=W+E)
Button(root, text="2", command=lambda: add("2")).grid(row=2, column=1,sticky=W+E)
Button(root, text="3", command=lambda: add("3")).grid(row=2, column=2,sticky=W+E)
Button(root, text="4", command=lambda: add("4")).grid(row=3, column=0,sticky=W+E)
Button(root, text="5", command=lambda: add("5")).grid(row=3, column=1,sticky=W+E)
Button(root, text="6", command=lambda: add("6")).grid(row=3, column=2,sticky=W+E)
Button(root, text="7", command=lambda: add("7")).grid(row=4, column=0,sticky=W+E)
Button(root, text="8", command=lambda: add("8")).grid(row=4, column=1,sticky=W+E)
Button(root, text="9", command=lambda: add("9")).grid(row=4, column=2,sticky=W+E)
Button(root, text="0", command=lambda: add("0")).grid(row=5, column=0,sticky=W+E)
Button(root, text=".", command=lambda: add(".")).grid(row=5, column=1,sticky=W+E)
Button(root, text="%", command=lambda: add("%")).grid(row=5, column=2,sticky=W+E)
Button(root, text="+", command=lambda: add("+")).grid(row=2, column=3,sticky=W+E)
Button(root, text="-", command=lambda: add("-")).grid(row=3, column=3,sticky=W+E)
Button(root, text="*", command=lambda: add("*")).grid(row=4, column=3,sticky=W+E)
Button(root, text="/", command=lambda: add("/")).grid(row=5, column=3,sticky=W+E)
Button(root, text="=",command=cal).grid(row=6,column = 0,columnspan=4,sticky=W+E+N+S)


root.resizable(0,0)
root.mainloop()