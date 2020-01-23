from tkinter import Tk,scrolledtext,Menu,filedialog,END,messagebox,simpledialog  #filedilaog is used for the dialogue box to appear when opening a file from anywhere in the system 

 
root= Tk(className=" Notepad ")  #Creates the GUI window and gives name to header file
textArea =scrolledtext.ScrolledText(root,width=100,height=80) # trainer variable is assigned to the object and referenced to root which is the  main screen

#
#FUNCTIONS
#

def openFile():
    textArea.delete('1.0',END)
    file = filedialog.askopenfile(parent=root, title='Select a text file',filetypes=(("Text file","*.txt"),("All files","*.*")))

    if file!= None:
        contents=file.read()   #empty files are not loaded but have nothing to read
        textArea.insert('1.0' , contents)
        file.close()

def saveFile():
    file=filedialog.asksaveasfile(mode='w')

    if file!= None:
        data= textArea.get('1.0', END+'-1c') #slice off the last character from get as an extra return is added
        file.write(data)
        file.close()

def newFile():
    root.title("Untitled - Notepad") 
    file = None
    textArea.delete(1.0,END) 
 
   

def findInFile():
    findinString = simpledialog.askstring("Find....", "Enter Text")
    textdata= textArea.get('1.0', END)

    occurences = textdata.upper().count(findinString.upper())
 
     
    if textdata.upper().count(findinString.upper())>0:
        label = messagebox.showinfo("Results",findinString + " has multiple occurences : "+str(occurences))
    else:
        label= messagebox.showinfo("Results","No occureneces")
        
   
def about():
    label = messagebox.showinfo("About","Zuha Khan")

def exitroot():
    if messagebox.askyesno("Quit","Are you sure you want to quit?"):
        root.destroy()

def cut():
    textArea.event_generate("<<Cut>>")

def copy():
    textArea.event_generate("<<Copy>>")

def paste():
    textArea.event_generate("<<Paste>>")


         
#Menu Options

menu = Menu(root) #menu variable takes in Menu object
root.config (menu=menu) 
fileMenu = Menu (menu)  
menu.add_cascade(label="File", menu=fileMenu) 
fileMenu.add_command (label="New",command=newFile)
fileMenu.add_command (label="Open", command=openFile)
fileMenu.add_command (label="Save",command=saveFile)
fileMenu.add_command (label="Find",command=findInFile)
fileMenu.add_command (label="Zuha",command=about)
fileMenu.add_separator()
fileMenu.add_command (label="Exit", command=exitroot)

editMenu = Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)


helpMenu = Menu(menu)
menu.add_cascade(label="Help",menu=helpMenu)
helpMenu.add_command(label="About Notepad",command=about)

zuhaMenu= Menu(menu)
menu.add_cascade(label="Zuha", menu=zuhaMenu)


#the top line visible allows the options to be moved to anywhere on the screen


textArea.pack()  #fit in wherever there is space,no specific layout to GUI


 
root.mainloop() #to keep main window open

  
  
