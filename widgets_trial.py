import tkinter as tk

root = tk.Tk()
root.title('Calculator')
entry = tk.Entry(root,width=30)
entry.grid(row=0,column=0,columnspan=3)
def on_click(num):
    current=entry.get()
    entry.delete(0, tk.END)
    entry.insert(0,str(current) + str(num))

def on_clear():
    entry.delete(0,tk.END)

def on_add():
    first_num= entry.get()
    global f_num
    f_num = int(first_num)
    global math
    math='Add'
    entry.delete(0,tk.END)

def on_equal():
    last_num= entry.get()
    second_num = int(last_num)
    entry.delete(0,tk.END)
    if math == 'Add':
        entry.insert(0,second_num+f_num)
    elif math == 'Sub':
        entry.insert(0,f_num-second_num)
    elif math == 'Multiply':
        entry.insert(0,f_num*second_num)
    elif math == 'Divide':
        entry.insert(0,f_num/second_num)

def on_sub():
    first_num= entry.get()
    global f_num 
    f_num =int(first_num)
    global math
    math='Sub'
    entry.delete(0,tk.END)

def on_multiply():
    first_num= entry.get()
    global f_num 
    f_num =int(first_num)
    global math
    math='Multiply'
    entry.delete(0,tk.END)

def on_divide():
    first_num= entry.get()
    global f_num 
    f_num =int(first_num)
    global math
    math='Divide'
    entry.delete(0,tk.END)

button1 = tk.Button(root,text='1',height=2,width=8,command=lambda: on_click(1))
button2 = tk.Button(root,text=' 2',height=2,width=8,command=lambda: on_click(2))
button3 = tk.Button(root,text=' 3',height=2,width=8,command=lambda: on_click(3))
button4 = tk.Button(root,text='4',height=2,width=8,command=lambda: on_click(4))
button5 = tk.Button(root,text='5',height=2,width=8,command=lambda: on_click(5))
button6 = tk.Button(root,text='6',height=2,width=8,command=lambda: on_click(6))
button7 = tk.Button(root,text='7',height=2,width=8,command=lambda: on_click(7))
button8 = tk.Button(root,text='8',height=2,width=8,command=lambda: on_click(8))
button9 = tk.Button(root,text='9',height=2,width=8,command=lambda: on_click(9))
button_clear = tk.Button(root,text='Clear',height=2,width=8,command=on_clear)
button0 = tk.Button(root,text='0',height=2,width=8,command=lambda: on_click(0))
button_equals = tk.Button(root,text='=',height=2,width=8,command=on_equal)
button_add = tk.Button(root,text='+',height=2,width=8,command=on_add)
button_subtract = tk.Button(root,text='-',height=2,width=8,command=on_sub)
button_multiply = tk.Button(root,text='x',height=2,width=8,command=on_multiply)
button_divide = tk.Button(root,text='/',height=2,width=8,command=on_divide)


button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
button_clear.grid(row=4,column=0)
button0.grid(row=4,column=1)
button_equals.grid(row=4,column=2)
button_add.grid(row=5,column=0)
button_subtract.grid(row=5,column=1)
button_multiply.grid(row=5,column=2)
button_divide.grid(row=6,column=1)
root.mainloop()
