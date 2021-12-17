from tkinter import *
import os
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo

mainMessage = "Studio: "

def newFile():
    global file
    root.title("Untitled - Coder Studio")
    file = None
    TextArea.delete(1.0, END)
    TextArea.pack(fill=BOTH, expand=TRUE)
    del_l()
    print(f"{mainMessage}Save file to view directory info \n...") 


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Coder Studio")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()
    info_insert()
    check_apply()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Coder Studio")
            print(f"{mainMessage}File Saved\n...")
            info_insert()
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
    

def sv(self):
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Coder Studio")
            print(f"{mainMessage}File Saved\n... ")
        info_insert()
    else:
        # Save the file
        try:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
        except:
            return None
    
def runb():
    import webbrowser
    if not file=="":
        try:
            if os.path.splitext(file)[1]=='.htm' or ".html":
                webbrowser.open(os.path.abspath(file))
        except TypeError:
            print(f"{mainMessage}Make sure that the file you want to open in browser is saved in your system \n...")
        else:
            return False
def run():
    import threading
    if os.path.splitext(file)[1]=='.py':
        os.system(f'cd {os.path.dirname(os.path.abspath(file))} && python "{file}"')
        

def info_insert():
    folderinfo.delete(0, END)
    try:
        os.chdir(os.path.dirname(os.path.abspath(file)))
    except Exception:
        print("...")
    folderlist = os.listdir()

    for folders in folderlist:
        folderinfo.insert(END, folders)

def del_l():
    if not file=="":    
        l.pack_forget()
        l1.pack_forget()

def check_apply():
    if file=="":
        global l
        global l1
        l = Label(TextFrame, text="<Coder-Studio>", font="comicsans 40 bold")
        l1 = Label(TextFrame, text="Developer's paradise can also be light-weight", font="comicsans 18 bold")
        del_l()
        l.pack( pady=125)
        l1.pack()
    else:
        TextArea.pack(fill=BOTH, expand=TRUE)
        del_l()
def Change_T():
    TextArea['bg']='grey'
    TextArea['fg']='white'
    TextFrame['bg']='grey'
    folderinfo['bg']='grey'
    folderinfo['fg']='white'
    root.configure(bg='black')
    l['bg']='grey'
    l['fg']='white'
    l1['bg']='grey'
    l1['fg']='white'
    btn['bg']='grey'
    btn['fg']='white'
    btn1['bg']='grey'
    btn1['fg']='white'
def Dtc():
    if os.path.exists('Theme'):
        Change_T()
def Dt():
    if os.path.exists('Theme'):
        Change_T()

    else:
        os.mkdir('Theme')
        Change_T()

def Lt():
    if os.path.exists('Theme'):
        os.rmdir('Theme')
        TextArea['bg']='white'
        TextArea['fg']='black'
        TextFrame['bg']='white'
        folderinfo['bg']='white'
        folderinfo['fg']='black'
        l['bg']='white'
        l['fg']='black'
        l1['bg']='white'
        l1['fg']='black'
        root.configure(bg = 'white')
        btn['bg']='white'
        btn['fg']='black'
        btn1['bg']='white'
        btn1['fg']='black'

if __name__ == "__main__":
    root=Tk()
    var1 = IntVar()
    root.title("Coder Studio")
    root.geometry('800x600')
    file = ""
    file_path = str(os.path.dirname(os.path.abspath(file)))
    #Menu Bar
    Mainmenu = Menu(root)
    #File Menu
    filemenu = Menu(Mainmenu)
    filemenu.add_cascade(label="Open File", command=openFile)
    filemenu.add_cascade(label="New File", command=newFile)
    filemenu.add_cascade(label="Save File", command=saveFile)
    Mainmenu.add_cascade(label="File", menu=filemenu)

    # Theme Menu
    Theme = Menu(Mainmenu, tearoff=0)
    Theme.add_command(label="Light Theme", command=Lt)
    Theme.add_command(label="Dark Theme", command=Dt)
    Mainmenu.add_cascade(label="Themes", menu=Theme)

    root.config(menu=Mainmenu)



    #main frame
    main_Frame = Frame(root, bg="black", borderwidth=6, relief=SUNKEN)
    main_Frame.pack(side=TOP, fill=X)
    main_label = Label(main_Frame, text="Coder Studio", bg="black", fg="white")
    main_label.pack()
    #folder info listbox

    fc = Scrollbar(root)
    folderinfo = Listbox(root, width=30, yscrollcommand=fc.set)
    folderinfo.pack(side=LEFT, fill=BOTH, pady=5, padx=5)
    fc.pack(side=LEFT, fill=Y, pady=5)
    fc.config(command=folderinfo.yview)
    
    #text area and scroll bar
    TextFrame= Frame(root)
    TextFrame.pack(fill=BOTH, expand=TRUE, pady=5, padx=5)
    scrollbar = Scrollbar(TextFrame, bg='black')   
    TextArea = Text(TextFrame, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=TextArea.yview)
    check_apply()
    #button to open file file in browser

    btn1 = Button(root, text="Open File In Browser", command=runb)
    btn1.pack(side=LEFT, padx=5)
    #button to run .py files 

    btn = Button(root, text="Run Python File", command=run)
    btn.pack(side=LEFT, padx=5)
    Dtc()
    TextArea.bind('<Control-s>', sv)
    root.mainloop()