# coding = utf-8
# __author__ = H.Tang
#              K.Zhang
# version = 2.0_2020-11-20
# env: win10, python 3.6
'''
Notes: 
    (1) 1.0中 select_files 传入 quit_clicked 始终为空，修改措施：将 select_files 赋值语句放在 quit_clicked 函数中.
    (2) 调整部分外观.
    (3) 在quit_clicked中执行copydirs，在copydirs执行成功后提示执行成功信息，删除部分控件，允许重复操作。

'''
'''
Problems:
    (1) 目标路径下子文件夹较多时显示问题.
    (2) 删除操作待补充.
    (3) SSH连接待补充.
'''

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil
import time
import sched

def copy_clicked(): # 拷贝执行命令
    global select_files
    select_files = []  
    files = os.listdir(orgin_path)
        
    for i in range(len(CBvar_list)):  
        if CBvar_list[i].get()==1:
            select_files.append(files[i])

    if orgin_path == '' or select_files==[]:
        print('op and sf judge: ', orgin_path,select_files)
        messagebox.showwarning('警告','请选择原始文件夹')
    elif target_path == '':
        messagebox.showwarning('警告','请选择目标文件夹文件夹')
    else:
        if messagebox.askokcancel('提示','确定要执行此操作吗？'):
            copydirs(orgin_path,target_path)
            messagebox.showinfo('提示','文件复制成功')
            # window.destroy()

def del_clicked():
    """
    不删除目录,只删除目标目录中的子文件

    """
    pass


def op_clicked():
    global orgin_path
    global CBvar_list
    CBvar_list = []
    orgin_path = filedialog.askdirectory(initialdir=os.path.dirname(__file__))

    op_txt.configure(state='normal')
    op_txt.delete('1.0','end')
    op_txt.insert('insert', orgin_path)
    op_txt.configure(state='disabled')

    files = os.listdir(orgin_path)
    lbl = Label(window, text="选择需要拷贝的文件").grid(column=1,row=2, padx = 5, pady = 5, sticky='w' )
    col,row = 2,2
    for f in files:

        CBvar_list.append(BooleanVar())
        chk = Checkbutton(window, text=f, var=CBvar_list[-1]).grid(column=col, row=row, padx = 5, pady = 5, sticky='w')
        row = row + 1


    copy_btn = Button(window, text="拷贝", command=copy_clicked )
    copy_btn.grid(column=5, row=5, padx = 5, pady = 5)

    del_btn = Button(window, text='删除', command=del_clicked )
    del_btn.grid(column=6, row=5, padx = 5, pady = 5)


def tp_clicked():
    global target_path
    target_path = filedialog.askdirectory(initialdir=os.path.dirname(__file__))

    tp_txt.configure(state='normal')
    tp_txt.delete('1.0','end')
    tp_txt.insert('insert',target_path)  
    tp_txt.configure(state='disabled') 



def copydirs(orgin_path,target_path):
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    
    files = select_files if set(select_files)<=set(os.listdir(orgin_path)) else os.listdir(orgin_path)
    
    for f in files:
        if os.path.isdir(orgin_path+'/'+f):
            copydirs(orgin_path+'/'+f,target_path+'/'+f)
        else:
            shutil.copyfile(orgin_path+'/'+f,target_path+'/'+f)
    
    
    

''' select_check —— K.Zhang
def select_check():  
    for i in range(len(CBvar_list)):  
        print('CBvar_list[%d].get() = ' %  i , CBvar_list[i].get())
    print('select_files =', select_files)
'''

if __name__ == '__main__':
    __file__ = '/users'
    window = Tk()
    window.title("批量文件拷贝")
    window.geometry('600x300')

    orgin_path,target_path = [],[]

    ''' # —— K.Zhang
    lbl = Label(window, text="选择原始文件夹").grid(column=0, row=0)
    lb2 = Label(window, text="选择目标文件夹").grid(column=0, row=1)
    '''
    op_btn = Button(window, text="选择原始文件夹", command=op_clicked)
    op_btn.grid(column=1, row=0, sticky='w', padx = 5, pady = 5)
    
    # 显示原始文件夹路径
    op_txt = Text(window, width=30, height=1)
    op_txt.grid(column=2,row=0, sticky='w', padx = 5, pady = 5)

    tp_btn = Button(window, text="选择目标文件夹", command=tp_clicked)
    tp_btn.grid(column=1, row=1, sticky='w', padx = 5, pady = 5)

    # 显示目标文件夹路径
    tp_txt = Text(window, width=30, height=1)
    tp_txt.grid(column=2,row=1, sticky='w', padx = 5, pady = 5)


    ''' # select_check —— K.Zhang
    b1=Button(window, text = '复选检测', command=button_click)
    b1.grid(column=1, row=2)
    '''

    window.mainloop()
