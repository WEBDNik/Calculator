from tkinter import *

root = Tk()
root.title("Калькулятор")

buttons = (('7', '8', '9', '/'),
           ('4', '5', '6', '*'),
           ('1', '2', '3', '-'),
           (',', '0', '=', '+'))

start = True
lastcommand = '='
final = 0

def click(text):
    global start
    global lastcommand
    global result
    if text.isdigit() or text == ',':
        if start:
            result.configure(text='')
            start = False
        if text != ',' or result.cget('text').find(',') == -1:
            result.configure(text=(result.cget('text')+text))
    else:
        if start:
            lastcommand = text
        else:
            calculate(float(result.cget('text')))
            lastcommand = text
            start = True

def calculate(a):
    global final
    global lastcommand
    global result
    if lastcommand == '+':
        final += a
    elif lastcommand == '-':
        final -= a
    elif lastcommand == '*':
        final *= a
    elif lastcommand == '/':
        try:
            final /= a
        except ZeroDivisionError:
            pass
    elif lastcommand == '=':
        final = a
    result.configure(text=final)

result = Label(root, text='0', font="Tahoma 20", bd=10)
result.grid(row=0, column=0, columnspan=4)

for row in range(4):
    for column in range(4):
        button = Button(root, text=buttons[row][column], font="Tahoma 20", command=lambda text=buttons[row][column]: click(text))
        button.grid(row=row+1, column=column, padx=5, pady=5, ipadx=20, ipady=20, sticky="nsew")

w = root.winfo_reqwidth()
h = root.winfo_reqheight()

ws = root.winfo_screenwidth()
wh = root.winfo_screenheight()

x = int(ws/2 - w/2)
y = int(wh/2 - h/2)

root.geometry("+{0}+{1}".format(x, y))

root.mainloop()