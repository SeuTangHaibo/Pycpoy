# coding=utf-8
# __author__ = H.Tang

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil
import time
import sched

def quit_clicked(): 
    for i in range(len(CBvar_list)):
        if CBvar_list[i].get()==1:
            select_files.append(files[i])
    if orgin_path == '' or select_files==[]:
        messagebox.showwarning('警告','请选择原始文件夹')
    elif target_path == '':
        messagebox.showwarning('警告','请选择目标文件夹文件夹')
    else:
        window.destroy()
        
def op_clicked():
    global files,orgin_path
    CBvar_list.clear() 
    orgin_path = filedialog.askdirectory(initialdir=os.path.dirname(__file__))
    files = os.listdir(orgin_path)
    lbl = Label(window, text="选择需要拷贝的文件").grid(column=2,row=0)
    col,row = 3,0
    for f in files:
        CBvar_list.append(BooleanVar())
        chk = Checkbutton(window, text=f, var=CBvar_list[-1]).grid(column=col, row=row)
        col = col+1
    btn = Button(window, text="确认", command=quit_clicked)
    btn.grid(column=10, row=10)
    
def tp_clicked():
    global target_path
    target_path = filedialog.askdirectory(initialdir=os.path.dirname(__file__))
    
def copydirs(orgin_path,target_path):
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    files = select_files if set(select_files)<=set(os.listdir(orgin_path)) else os.listdir(orgin_path)
    for f in files:
        if os.path.isdir(orgin_path+'/'+f):
            copydirs(orgin_path+'/'+f,target_path+'/'+f)
        else:
            shutil.copyfile(orgin_path+'/'+f,target_path+'/'+f)

if __name__ == '__main__':
    __file__ = '/users'
    CBvar_list,select_files = [],[]
    window = Tk()
    window.title("批量文件拷贝")
    window.geometry('600x100')
    lbl = Label(window, text="选择原始文件夹").grid(column=0, row=0)
    lb2 = Label(window, text="选择目标文件夹").grid(column=0, row=1)
    btn = Button(window, text="Click Me", command=op_clicked)
    btn.grid(column=1, row=0)
    btn = Button(window, text="Click Me", command=tp_clicked)
    btn.grid(column=1, row=1)
    window.mainloop()
    copydirs(orgin_path,target_path)
