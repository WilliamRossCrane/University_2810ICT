# Program to Create a Simple GUI
# Calculator uses Tkinter 

# Import Everything for Tkinter
from tkinter import *
# Globally Declare the Expression Variable 
expression = ""
# Function to Update Expression, In a Text Entry Box
def press(num):
    # Point out the Global Expression Variable 
    global expression 
    # Concatenation of a String 
    expression = expression + str(num)
    # Update the String using the Set Method
    equation.set(expression)
# Function to Evaluate the Final Expression
def equalpress():
    # Try and Except are Use to Handle Division Errors
    try:
        global expression 
        # Evaluate the Expression and converts to a String
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    # If error occurs it is handled by the except black
    except:
        equation.set(" Error ")
        expression = ""
# Function to Clear the contents of text entry box 
def clear():
    global expression
    expression = ""
    equation.set("")
# Driver Code
if __name__ == "__main__":
    # Create GUI Window
    gui = Tk()
    # Updates the GUI Background
    gui.configure(background="pink")
    # Titles the GUI
    gui.title("Hello Kitty Calculator")
    # Sets the configuration of the GUI Window
    gui.geometry("270x150")
    # StringVar() is the variable class
    equation = StringVar()
    # Create a Text Entry Box
    expression_field = Entry(gui, textvariable=equation)
    # Grid Widgit is used to place buttons at specific locations
    expression_field.grid(columnspan=4, ipadx=70)
    # Create a button and place at particular location
    # When Button is Pressed Command will be executed that is affiliated with the button
    button1 = Button(gui, text=' 1 ', fg='black', bg='lavender',
                    command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)
 
    button2 = Button(gui, text=' 2 ', fg='black', bg='lavender',
                    command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)
 
    button3 = Button(gui, text=' 3 ', fg='black', bg='lavender',
                    command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)
 
    button4 = Button(gui, text=' 4 ', fg='black', bg='lavender',
                    command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)
 
    button5 = Button(gui, text=' 5 ', fg='black', bg='lavender',
                    command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)
 
    button6 = Button(gui, text=' 6 ', fg='black', bg='lavender',
                    command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)
 
    button7 = Button(gui, text=' 7 ', fg='black', bg='lavender',
                    command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)
 
    button8 = Button(gui, text=' 8 ', fg='black', bg='lavender',
                    command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)
 
    button9 = Button(gui, text=' 9 ', fg='black', bg='lavender',
                    command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)
 
    button0 = Button(gui, text=' 0 ', fg='black', bg='lavender',
                    command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)
 
    plus = Button(gui, text=' + ', fg='black', bg='lavender',
                command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)
 
    minus = Button(gui, text=' - ', fg='black', bg='lavender',
                command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)
 
    multiply = Button(gui, text=' * ', fg='black', bg='lavender',
                    command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)
 
    divide = Button(gui, text=' / ', fg='black', bg='lavender',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)
 
    equal = Button(gui, text=' = ', fg='black', bg='lavender',
                command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)
 
    clear = Button(gui, text='Clear', fg='black', bg='lavender',
                command=clear, height=1, width=7)
    clear.grid(row=5, column='1')
 
    Decimal= Button(gui, text='.', fg='black', bg='lavender',
                    command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)
    # start the GUI
    gui.mainloop()
    
        