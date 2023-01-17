from tkinter import *

#Define
def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    input_text.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    input_text.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    input_text.set(sumup)
    operator = ""

#Components

win = Tk()
win.geometry("371x342")
win.title("Calculator")
operator=""
win.resizable(0,0)
input_text = StringVar()

# Create an input field inside the Frame created in the previous step. Output aligned to the  right:
txtDisplay = Entry (win,font=('arial', 20,'bold') ,width=23, textvariable=input_text, bd=10, insertwidth=4,
                    bg="light grey", justify='right').grid(columnspan=4)

# add button widgets (line 1)
btn1 = Button(win,width = 9,height = 3,text="7",fg="White",bg="#313131",font=("Times New Roman",12,"bold"),command=lambda:btnClick(7))
btn1.place(x = 4,y=54)
btn2 = Button(win,width = 9,height = 3,text="8",fg="White",bg="#313131",font=("Times New Roman",12,"bold"),command=lambda:btnClick(8))
btn2.place(x = 95,y=54)
btn3 = Button(win,width = 9,height = 3,text="9",fg="White",bg="#313131",font=("Times New Roman",12,"bold"),command=lambda:btnClick(9))
btn3.place(x = 186,y=54)
btn4 = Button(win,width = 9,height = 3,text = "+",fg="White",bg="#C3B091",font=("Times New Roman",12,"bold"),command=lambda:btnClick("+"))
btn4.place(x = 277,y=54)

# add button widgets (line 2)
btn5 = Button(win,width = 9,height = 3,text="4",fg="White",bg="#313131",font=("Times New Roman",12,"bold"),command=lambda:btnClick(4))
btn5.place(x = 4,y=125)
btn6 = Button(win,width = 9,height = 3,text="5",fg="White",bg="#313131",font=("Times New Roman",12,"bold"),command=lambda:btnClick(5))
btn6.place(x = 95,y=125)
btn7 = Button(win,width = 9,height = 3,text="6",fg="White",bg="#313131",font=("Times New Roman",12,"bold"),command=lambda:btnClick(6))
btn7.place(x = 186,y=125)
btn8 = Button(win,width = 9,height = 3,text="-",fg="White",bg="#C3B091",font=("Times New Roman",12,"bold"),command=lambda:btnClick("-"))
btn8.place(x = 277,y=125)

# add button widgets (line 3)
btn9 = Button(win,width = 9,height = 3,text="1",fg="White",bg="#313131",font=("Times New Roman",12,"bold"),command=lambda:btnClick(1))
btn9.place(x = 4,y=196)
btn10 = Button(win,width = 9,height = 3,text="2",fg="White",bg="#313131",font=("Times New Roman",12,"bold"),command=lambda:btnClick(2))
btn10.place(x = 95,y=196)
btn11 = Button(win,width = 9,height = 3,text="3",fg="White",bg="#313131",font=("Times New Roman",12,"bold"),command=lambda:btnClick(9))
btn11.place(x = 186,y=196)
btn12 = Button(win,width = 9,height = 3,text="x",fg="White",bg="#C3B091",font=("Times New Roman",12,"bold"),command=lambda:btnClick("*"))
btn12.place(x = 277,y=196)

# add button widgets (line 4)
btn13 = Button(win,width = 9,height = 3,text="0",fg="White",bg="#313131",font=("Times New Roman",12,"bold"),command=lambda:btnClick(0))
btn13.place(x = 4,y=267)
btn14 = Button(win,width = 9,height = 3,text="C",fg="White",bg="#C3B091",font=("Times New Roman",12,"bold"),command=btnClearDisplay)
btn14.place(x = 95,y=267)
btn15 = Button(win,width = 9,height = 3,text="=",fg="White",bg="#C3B091",font=("Times New Roman",12,"bold"),command=btnEqualsInput)
btn15.place(x = 186,y=267)
btn16 = Button(win,width = 9,height = 3,text="/",fg="White",bg="#C3B091",font=("Times New Roman",12,"bold"),command=lambda:btnClick("/"))
btn16.place(x = 277,y=267)

win.mainloop()