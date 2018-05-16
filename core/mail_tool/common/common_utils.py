def cal_center_x(root):
    pass

def cal_center_y(root):
    pass

def cal_center_str(root,width,height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    return '%dx%d+%d+%d' % (width, height, (screen_width - width)/2, (screen_height - height)/2)
