import tkinter as tk
import sys
sys.path.append('..')
from mail import sender



sender = sender.Sender()

#主容器
window = tk.Tk()
window.title('邮件发送')
window.geometry('800x300')


# 收件人
receive_label = tk.Label(window,text='收件人')
var_receiver_name = tk.StringVar()
receive_input = tk.Entry(window,textvariable = var_receiver_name)

receive_label.place(x=70,y=15)
receive_input.place(x=140,y=15)

# 标题
mail_title_label = tk.Label(window,text='标题')
var_mail_title = tk.StringVar()
mail_title_input = tk.Entry(window,textvariable = var_mail_title)


mail_title_label.place(x=70,y=50)
mail_title_input.place(x=140,y=50)

# 内容
mail_content_label = tk.Label(window,text='内容')
var_mail_content = tk.StringVar()
mail_context_text = tk.Text(window,height = 10)

mail_content_label.place(x=70,y=85)
mail_context_text.place(x=140,y=85)
# 按钮

def send_mail():
	print("收件人：%s"%receive_input.get())
	print("标题：%s"%mail_title_input.get())
	print("内容：%s"%mail_context_text.get('0.0',tk.END))

	sender.add_reciever(receive_input.get())
	sender.set_title(mail_title_input.get())
	sender.set_content(mail_context_text.get('0.0',tk.END))

	sender.send_mail();
def clear_input():
	pass

send_btn = tk.Button(window,text="发送",command=send_mail)
clear_btn = tk.Button(window,text="重置",command=clear_input)

send_btn.place(x=140,y=250)
clear_btn.place(x=250,y=250)


window.mainloop()

