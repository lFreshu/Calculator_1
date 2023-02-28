from tkinter import *

def button_press(num):

    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equation():             #eval robi obliczenie np "4+5" interpretuje jako 9

    global equation_text

    try:

        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total

    except ZeroDivisionError:
        equation_label.set("Can't divide by 0")
        equation_text = ""

    except SyntaxError:
        equation_label.set("Syntax error!")
        equation_text = ""


def clear_label():

    global equation_text
    equation_label.set("")
    equation_text = ("")


window = Tk()
window.title("Kalkulator prosty")
window.geometry("500x500")
icon = PhotoImage(file='calculator-icon.png')
window.iconphoto(True, icon)

equation_text = ""
equation_label = StringVar()

label = Label(window,
              textvariable=equation_label,
              width=24,
              bg="white",
              height=2,
              font=("consolas",20)
              )
label.pack()

frame = Frame(window)
frame.pack()

#creating buttons
button1 = Button(frame, text=1, font=35, height=4, width=9,
                 command=lambda: button_press(1))
button2 = Button(frame, text=2, font=35, height=4, width=9,
                 command=lambda: button_press(2))
button3 = Button(frame, text=3, font=35, height=4, width=9,
                 command=lambda: button_press(3))
button4 = Button(frame, text=4, font=35, height=4, width=9,
                 command=lambda: button_press(4))
button5 = Button(frame, text=5, font=35, height=4, width=9,
                 command=lambda: button_press(5))
button6 = Button(frame, text=6, font=35, height=4, width=9,
                 command=lambda: button_press(6))
button7 = Button(frame, text=7, font=35, height=4, width=9,
                 command=lambda: button_press(7))
button8 = Button(frame, text=8, font=35, height=4, width=9,
                 command=lambda: button_press(8))
button9 = Button(frame, text=9, font=35, height=4, width=9,
                 command=lambda: button_press(9))
button0 = Button(frame, text=0, font=35, height=4, width=9,
                 command=lambda: button_press(0))
add = Button(frame, text='+', font=35, height=4, width=9,
                 command=lambda: button_press('+'))
minus = Button(frame, text='-', font=35, height=4, width=9,
                 command=lambda: button_press('-'))
multiply = Button(frame, text='*', font=35, height=4, width=9,
                 command=lambda: button_press('*'))
divide = Button(frame, text='/', font=35, height=4, width=9,
                 command=lambda: button_press('/'))
dot = Button(frame, text='.', font=35, height=4, width=9,
                 command=lambda: button_press('.'))
equal = Button(frame, text='=', font=35, height=4, width=9,
                 command=lambda: equation())
clear = Button(window, text="clear", height=2, width=14,
               command=clear_label)
clear.pack()

#row and column
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
button0.grid(row=3, column=0)
divide.grid(row=0, column=3)
multiply.grid(row=1, column=3)
minus.grid(row=2, column=3)
add.grid(row=3, column=3)
equal.grid(row=3, column=2)
dot.grid(row=3, column=1)

window.mainloop()