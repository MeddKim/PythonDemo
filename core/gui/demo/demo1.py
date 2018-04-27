import tkinter

root = tkinter.Tk()

label = tkinter.Label(root,text='Hello World!')
label.pack()

# quit_btn = tkinter.Button(root,text='Quit',command=root.quit)
quit_btn = tkinter.Button(root,text='Quit',command=root.quit,bg='red',fg='white')
quit_btn.pack(fill=tkinter.X,expand=1)

tkinter.mainloop()