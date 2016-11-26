#PyNotes class

import tkinter
from tkinter import *
import sys
import tkinter.scrolledtext as tkst

FILEEXTENSIONS = dict(defaultextension='.pn',
                          filetypes=[('PyNote file','*.pn')])

class base:

    def quit():
        sys.exit()
        
    global FileContents
    global screen
    global textPad

    screen = tkinter.Tk()

    w = 800 
    h = 800 

    ws = screen.winfo_screenwidth() 
    hs = screen.winfo_screenheight()

    x = (ws/10) - (w/10)
    y = (hs/2) - (h/2)

    screen.title("PyNote Pad")
    screen.geometry('%dx%d+%d+%d' % (w, h, x, y))
    screen.resizable(width=False, height=False)

    textPad = tkst.ScrolledText(screen, width=500, height=500)
    textPad.pack()
        
    def open_command():
        file = filedialog.askopenfile(parent=screen,mode='rb',title='Select a file', **FILEEXTENSIONS)
        if file != None:
            textPad.delete('1.0', END)
            contents = file.read()
            textPad.insert('1.0',contents)
            file.close()

    def save_command():
        FileContents = textPad.get('1.0', END)
        
        file = filedialog.asksaveasfile(mode='w', **FILEEXTENSIONS)
        if file != None:
            data = FileContents
            file.write(data)
            
    def exit_command():
        if messagebox.askokcancel("Quit?", "Do you really want to quit?"):
            quit()
            
    def dummy():
        print("null")

    def new_command():
            if messagebox.askyesno("Save?", "Do you want to save?"):
                FileContents = textPad.get('1.0', END)
        
                file = filedialog.asksaveasfile(mode='w', **FILEEXTENSIONS)
                if file != None:
                    data = FileContents
                    file.write(data)
                    textPad.delete('1.0', END)
            else:
                textPad.delete('1.0', END)

    def bindNewCommand(event):
        if messagebox.askyesno("Save?", "Do you want to save?"):
                FileContents = textPad.get('1.0', END)
        
                file = filedialog.asksaveasfile(mode='w', **FILEEXTENSIONS)
                if file != None:
                    data = FileContents
                    file.write(data)
                    textPad.delete('1.0', END)
                else:
                    textPad.delete('1.0', END)

    def bindOpenCommand(event):
        file = filedialog.askopenfile(parent=screen,mode='rb',title='Select a file', **FILEEXTENSIONS)
        if file != None:
            textPad.delete('1.0', END)
            contents = file.read()
            textPad.insert('1.0',contents)
            file.close()

    def bindSaveCommand(event):
        FileContents = textPad.get('1.0', END)
        
        file = filedialog.asksaveasfile(mode='w', **FILEEXTENSIONS)
        if file != None:
            data = FileContents
            file.write(data)

    def bindExitCommand(event):
        if messagebox.askokcancel("Quit?", "Do you really want to quit?"):
            quit()
        
    menu = Menu(screen)
    filemenu = Menu(menu)
    screen.config(menu=menu)

    screen.bind("<Control-n>", bindNewCommand)
    screen.bind("<Control-o>", bindOpenCommand)
    screen.bind("<Control-s>", bindSaveCommand)
    screen.bind("<Escape>", bindExitCommand)
    
    menu.add_cascade(label="File", menu=filemenu)
    menu.add_command(label="Exit", command=exit_command)
    filemenu.add_command(label="New", command=new_command)
    filemenu.add_command(label="Open...", command=open_command)
    filemenu.add_command(label="Save", command=save_command)
        
    
    screen.mainloop()

    
