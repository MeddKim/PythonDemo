import tkinter

root = tkinter.Tk()

def resize(ev=None):
	label.config(font='Helvetica -%d bold' %scale.get())

root = tkinter.Tk()
root.geometry('250x150')

label = tkinter.Label(root,text='Hello World!',font='Helvetica -12 bold')
label.pack(fill=tkinter.Y, expand=1)

scale = tkinter.Scale(root,from_=10,to=40,orient=tkinter.HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=tkinter.X,expand=1)

quit_btn = tkinter.Button(root,text='Quit',command=root.quit,activeforeground='white',activebackground='red')
quit_btn.pack(fill=tkinter.X,expand=1)

tkinter.mainloop()