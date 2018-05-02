import tkinter as tk

root = tk.Tk()
root.title('测试按钮')
root.geometry('300x200')

btn1 = tk.Button(root,activebackground='#2B2B2B',activeforeground='#BBBBBB ',text='按钮一',bg='#3C3F41')
btn1.pack()

root.mainloop()

