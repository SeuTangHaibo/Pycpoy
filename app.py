#coding=utf-8
#__author__=H.Tang,K.Zhang

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)

def copy_clicked():
    if orgin_path == '':
        messagebox.showwarning('Warning','Please select original path')
    else:
        global select_files
        select_files = []  
        files = os.listdir(orgin_path)        
        for i in range(len(CBvar_list)):  
            if CBvar_list[i].get()==1:
                select_files.append(files[i])
        if select_files==[]:
            messagebox.showwarning('Warning','Please select subfolder')
        elif target_path == '':
            messagebox.showwarning('Warning','Please select target path')
        else:
            if messagebox.askokcancel('Prompt','Sure to perform this operation?'):
                copydirs(orgin_path,target_path)
                messagebox.showinfo('Prompt','Files copied successfully')

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
    lbl = Label(window, text="Select file")
    Element_list.append(lbl)
    lbl.grid(column=1,row=2, padx = 5, pady = 5, sticky='w' )
    col,row = 2,2
    for f in files:
        CBvar_list.append(BooleanVar())
        chk = Checkbutton(window, text=f, var=CBvar_list[-1])
        Element_list.append(chk)
        chk.grid(column=col+(row-2)//6, row=(row-2)%6+2, padx = 5, pady = 5, sticky='w')
        row = row + 1

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

def dp_clicked():
    global delete_path
    global DBvar_list
    DBvar_list = []
    delete_path = filedialog.askdirectory(initialdir=os.path.dirname(__file__))
    dp_txt.configure(state='normal')
    dp_txt.delete('1.0','end')
    dp_txt.insert('insert', delete_path)
    dp_txt.configure(state='disabled')
    files = os.listdir(delete_path)
    lbl = Label(window, text="Select files to be deleted")
    Element_list.append(lbl)
    lbl.grid(column=1,row=2, padx = 5, pady = 5, sticky='w' )
    col,row = 2,2
    for f in files:
        DBvar_list.append(BooleanVar())
        chk = Checkbutton(window, text=f, var=DBvar_list[-1])
        Element_list.append(chk)
        chk.grid(column=col+(row-2)//6, row=(row-2)%6+2, padx = 5, pady = 5, sticky='w')
        row = row + 1
            
def del_clicked():
    if delete_path == '':
        messagebox.showwarning('Warning','Please select original path')
    else:
        global delete_files
        delete_files = []  
        files = os.listdir(delete_path)        
        for i in range(len(DBvar_list)):  
            if DBvar_list[i].get()==1:
                delete_files.append(files[i])
        if delete_files==[]:
            messagebox.showwarning('Warning','Please select subfolder')
        else:
            if messagebox.askokcancel('Prompt','Sure to perform this operation?'):
                del_files(delete_path)
                messagebox.showinfo('Prompt','Files deleted successfully')
    
def del_files(delete_path):
    files = delete_files if set(delete_files)<=set(os.listdir(delete_path)) else os.listdir(delete_path)
    for file in files:
        path_file = os.path.join(delete_path,file)
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            del_files(path_file)

def local_copy():
    while Element_list:
        element = Element_list.pop()
        element.destroy()
    op_btn = Button(window, text="Select orgional path", command=op_clicked)
    op_btn.grid(column=1, row=0, sticky='w', padx = 5, pady = 5) 
    tp_btn = Button(window, text="Select target path", command=tp_clicked)
    tp_btn.grid(column=1, row=1, sticky='w', padx = 5, pady = 5)
    global op_txt
    op_txt = Text(window, width=30, height=1)
    op_txt.grid(column=2,row=0, sticky='w', padx = 5, pady = 5)
    global tp_txt
    tp_txt = Text(window, width=30, height=1)
    tp_txt.grid(column=2,row=1, sticky='w', padx = 5, pady = 5)   

    copy_btn = Button(window, text="Copy", command=copy_clicked )
    copy_btn.grid(column=5, row=9, padx = 5, pady = 5)
    Element_list.append(op_btn);Element_list.append(tp_btn);Element_list.append(copy_btn)
    Element_list.append(op_txt);Element_list.append(tp_txt)

def local_delete():
    while Element_list:
        element = Element_list.pop()
        element.destroy()
    delete_path = ''
    dp_btn = Button(window, text="Select file", command=dp_clicked)
    dp_btn.grid(column=1, row=0, sticky='w', padx = 5, pady = 5) 
    global dp_txt
    dp_txt = Text(window, width=30, height=1)
    dp_txt.grid(column=2,row=0, sticky='w', padx = 5, pady = 5)
    del_btn = Button(window, text='delete', command=del_clicked )
    del_btn.grid(column=6, row=9, padx = 5, pady = 5)
    Element_list.append(dp_btn);Element_list.append(dp_txt);Element_list.append(del_btn)
    
def remote_delete():
    pass

def remote_copy():
    pass

if __name__ == '__main__':
    __file__ = '/users'
    orgin_path,target_path,delete_path = '','',''
    Element_list = []
    window = Tk()
    window.title("pycopy")
    window.geometry('1000x350')
    window.tk.call('tk', 'scaling', ScaleFactor/75)
    menubar = Menu(window)
    menubar.add_command(label="Local copy", command=local_copy)
    menubar.add_cascade(label="Local delete",command=local_delete)
    menubar.add_command(label="Remote copy", command=remote_copy)
    menubar.add_command(label="Remote delete", command=remote_delete)
    window.config(menu=menubar)
    window.mainloop()
