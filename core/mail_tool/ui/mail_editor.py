import tkinter as tk
import tkinter.messagebox as mb
from mail import sender

class MailEditor(tk.Toplevel):
    """邮件编辑"""
    def __init__(self,parent):
        super().__init__(parent)
        self.reciever_label = tk.Label(self,text="收件人")
        self.reciever_entry = tk.Entry(self)
        self.subject_label = tk.Label(self,text="标题")
        self.subject_entry = tk.Entry(self)
        self.content_label = tk.Label(self,text="内容")
        self.content_entry = tk.Entry(self)
        self.send_btn = tk.Button(self,text="发送",command=self.send_mail)
        self.save_btn = tk.Button(self,text="保存为模板",command=self.save_mail)


        self.reciever_label.pack()
        self.reciever_entry.pack()
        self.subject_label.pack()
        self.subject_entry.pack()
        self.content_label.pack()
        self.content_entry.pack()
        self.send_btn.pack()
        self.save_btn.pack()

    def send_mail(self):

        pass
    def save_mail(self):
        pass