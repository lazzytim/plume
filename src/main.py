import customtkinter as ctk
from PIL import Image, ImageTk
import sys, pathlib, os
import tkinter.filedialog as rf

def getPath(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = pathlib.Path(__file__).parent
    return os.path.join(base_path, relative_path)

root = ctk.CTk(fg_color='#181818')
root.title('Plume for Windows')
root.iconbitmap(getPath('icon.ico'))
root.geometry('400x500')
root.resizable(0, 0)

ctk.CTkLabel(root, text='', image=ImageTk.PhotoImage(Image.open(getPath('banner.png')))).place(x=0, y=0, anchor=ctk.NW)

tabview = ctk.CTkTabview(root, width=360, height=380, fg_color='#181818', segmented_button_selected_color='#ffd600', text_color='#181818', border_color='#434343', border_width=1)
tabview_shortcutarrow = tabview.add('   Shortcuts Icon   ')
tabview_taskbar = tabview.add('   Taskbar   ')
tabview.place(x=20, y=100, anchor=ctk.NW)

path = ctk.CTkEntry(tabview_shortcutarrow, fg_color='#181818', placeholder_text='Select a .ico to replace current one', border_width=1, width=245)
path.place(x=20, y=20, anchor=ctk.NW)

def shortcut_arrow_apply():
    os.mkdir('C:\\Plume')
    newpath = path.get().replace('/', '\\\\')
    os.rename(newpath, 'C:\\Plume\\shortcutarrow.ico')
    file = open('regs\\temp.reg', mode='w')
    file.write('Windows Registry Editor Version 5.00\n\n[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Icons]\n"29"="C:\\Plume\\shortcutarrow.ico"\n\n')
    os.open('regs\\temp.reg')
    
def shortcut_arrow_input():
    file = rf.askopenfile(title='Select a .ICO format to change the shortcut arrow with.', filetypes=[("Windows Icon File","*.ico")]).name
    path.insert(0, file)

ctk.CTkButton(tabview_shortcutarrow, text="•••", width=50, fg_color='#ffd600', hover_color='#434343', text_color='#181818', command=shortcut_arrow_input).place(x=280, y=20, anchor=ctk.NW)
ctk.CTkLabel(tabview_shortcutarrow, text='', image=ImageTk.PhotoImage(Image.open(getPath('assets\\preview1.png')))).place(x=20, y=65, anchor=ctk.NW)
ctk.CTkButton(tabview_shortcutarrow, text="Apply the modification", width=310, fg_color='#ffd600', hover_color='#434343', text_color='#181818', command=shortcut_arrow_apply).place(x=20, y=290, anchor=ctk.NW)

 
root.mainloop()