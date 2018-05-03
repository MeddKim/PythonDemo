import tkinter as tk
from mail_editor import *

class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.send_btn = tk.Button(self,text="新建",command=self.open_mail_editor)

		self.send_btn.pack()
	def open_mail_editor(self):
		mail_editor = MailEditor(self)
		mail_editor.grab_set()
if __name__ == '__main__':
	app = App()
	app.mainloop()