from tkinter import *
win = Tk()

# add widgets from here
win.geometry("338x468")
win.title("Calculator")
win.resizable(0,0)
input_text = StringVar()

# Use the Frame widget to create a frame for the input field:
input_frame = Frame(win, width = 312, height = 100, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = TOP)

# Create an input field inside the Frame created in the previous step. Output aligned to the  right:
input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 50, bg = "#eee", bd = 0, justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10)

# add button widgets (line 1)
btn1 = Button(win,width = 9,height = 4,text="CE",fg="White",bg="#313131",font=("Times New Roman",12))
btn1.place(x = 4,y=54)
btn2 = Button(win,width = 9,height = 4,text="C",fg="White",bg="#313131",font=("Times New Roman",12))
btn2.place(x = 84,y=54)
btn3 = Button(win,width = 9,height = 4,text="Clear",fg="White",bg="#313131",font=("Times New Roman",12))
btn3.place(x = 164,y=54)
btn4 = Button(win,width = 9,height = 4,text = "+",fg="White",bg="#313131",font=("Times New Roman",12))
btn4.place(x = 244,y=54)

# add button widgets (line 2)
btn5 = Button(win,width = 9,height = 4,text="7",fg="White",bg="#313131",font=("Times New Roman",12))
btn5.place(x = 4,y=134)
btn6 = Button(win,width = 9,height = 4,text="8",fg="White",bg="#313131",font=("Times New Roman",12))
btn6.place(x = 84,y=134)
btn7 = Button(win,width = 9,height = 4,text="9",fg="White",bg="#313131",font=("Times New Roman",12))
btn7.place(x = 164,y=134)
btn8 = Button(win,width = 9,height = 4,text="-",fg="White",bg="#313131",font=("Times New Roman",12))
btn8.place(x = 244,y=134)

# add button widgets (line 3)
btn9 = Button(win,width = 9,height = 4,text="5",fg="White",bg="#313131",font=("Times New Roman",12))
btn9.place(x = 4,y=214)
btn10 = Button(win,width = 9,height = 4,text="6",fg="White",bg="#313131",font=("Times New Roman",12))
btn10.place(x = 84,y=214)
btn11 = Button(win,width = 9,height = 4,text="7",fg="White",bg="#313131",font=("Times New Roman",12))
btn11.place(x = 164,y=214)
btn12 = Button(win,width = 9,height = 4,text="x",fg="White",bg="#313131",font=("Times New Roman",12))
btn12.place(x = 244,y=214)

# add button widgets (line 4)
btn13 = Button(win,width = 9,height = 4,text="1",fg="White",bg="#313131",font=("Times New Roman",12))
btn13.place(x = 4,y=294)
btn14 = Button(win,width = 9,height = 4,text="2",fg="White",bg="#313131",font=("Times New Roman",12))
btn14.place(x = 84,y=294)
btn15 = Button(win,width = 9,height = 4,text="3",fg="White",bg="#313131",font=("Times New Roman",12))
btn15.place(x = 164,y=294)
btn16 = Button(win,width = 9,height = 4,text="/",fg="White",bg="#313131",font=("Times New Roman",12))
btn16.place(x = 244,y=294)

# add button widgets (line 5)
btn17 = Button(win,width = 9,height = 4,text="+/-",fg="White",bg="#313131",font=("Times New Roman",12))
btn17.place(x = 4,y=374)
btn18 = Button(win,width = 9,height = 4,text="0",fg="White",bg="#313131",font=("Times New Roman",12))
btn18.place(x = 84,y=374)
btn19 = Button(win,width = 9,height = 4,text=".",fg="White",bg="#313131",font=("Times New Roman",12))
btn19.place(x = 164,y=374)
btn18 = Button(win,width = 9,height = 4,text="=",fg="White",bg="Blue",font=("Times New Roman",12))
btn18.place(x = 244,y=374)

win.mainloop()