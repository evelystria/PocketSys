from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image

def mainWindow():
    global mainWindow, RFrame
    #Create main window
    mainWindow = Tk()
    mainWindow.geometry("425x425")
    mainWindow.resizable(width=False, height=False)
    
    mainWindow.title('AY2016/2017 - R31 - SEM 2 - Module Quizzes')   
    
    #LEFT FRAME
    LFrame = Frame(mainWindow)
    LFrame.grid(row=0, column=0, sticky="nsew")
    #Profile Button
    profile = Button(LFrame, command=profileButton)
        
    profile_image = ImageTk.PhotoImage(file="profile.jpg")            
    profile.config(image=profile_image)
    profile.pack(side=TOP, anchor=W)    
    #Quiz Button
    quiz = Button(LFrame, command=quizButton)
    
    quiz_image = ImageTk.PhotoImage(file="Quiz.png")
    quiz.config(image=quiz_image)
    quiz.pack(side=TOP, anchor=W)
    
    #RIGHT FRAME
    RFrame = Frame(mainWindow)
    RFrame.grid(row=0, column=1, sticky="nsew")
    
    #Exit Button
    menu = Menu(mainWindow)
    menu.add_command(label="Quit", command=on_closing)
    mainWindow.config(menu=menu)    
    mainWindow.protocol("WM_DELETE_WINDOW", on_closing)
    mainWindow.mainloop()
    
def profileButton():  
    try:
        a = Label(RFrame, text='Not available')
        a.config(font=("Arial", 15))
        a.grid(row=0, column=1, sticky='nsew')
        b.grid_remove()
        option.grid_remove()
        
        
    except NameError:
        pass

def quizButton():
    try:
        b = Label(RFrame, text='Quiz')
        b.config(font=("Arial", 15))
        b.grid(row=0, column=1, sticky='nsew')
        
        
        #
        quiz= {'C204':[("Is integer equivalent to float?", False),
                       ("Does the module csv exist?", True)],
               'G107':[("Is facial expression a non-verbal cue?", True),
                       ("Does noise cause physiological effects?", False)]
               }
        
        score= {"Correct": 0, "Incorrect": 0}
        
        modulelabel = Label(RFrame, text='Choose a module:')
        module.grid(row=1, column=1, sticky='nsew')
        var = StringVar(RFrame)
        modules = {'C204',
                   'G107'
                    }
        option = OptionMenu(RFrame, var, *modules)
        option.config(bg='White')
        option.grid(row=2, column=1, sticky='nsew')
        var.set('C204')   
        
        a.grid_remove()
           
            
            
        
    except NameError:
        pass
    
    
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        mainWindow.destroy()
        