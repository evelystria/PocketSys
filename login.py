from tkinter import *
from tkinter import messagebox
import pymysql

from variables import *
from main import *

def loginWindow():   
    global loginWindow, loginentry, passentry
    #Create main window
    loginWindow = Tk()
    loginWindow.geometry(var_progGeometry)
    loginWindow.resizable(width=var_progResizable, height=var_progResizable)
    
    loginWindow.title(var_progName + ' - ' + var_progVersion)   
    
    #
    msg = Message(loginWindow, text='Please enter the necessary credentials for verification.', width=350)
    msg.pack()
    loginlabel = Label(loginWindow, text='Login:').pack()
    loginentry = Entry(loginWindow)
    loginentry.pack()
    passlabel = Label(loginWindow, text='Password:').pack()
    passentry = Entry(loginWindow, show="*")
    passentry.pack()
    
    enterbutton = Button(loginWindow, text='Enter', command=enterButton).pack()
    signup = Button(loginWindow, text='Sign up', command=signupButton).pack()
    


    loginWindow.mainloop()

def enterButton():
    getUsername = loginentry.get()
    getPassword = passentry.get()
    
    conn = pymysql.connect(host='localhost',
                            user='root',
                            passwd='',
                            db ='republicquiz')
            
    cursor = conn.cursor()
            
    strSQL = "SELECT * FROM `users` WHERE `username`='" + getUsername + "' AND `password`='" + getPassword + "'"
    if cursor.execute(strSQL):
        
        cursor.close()
        conn.close()   
            
        loginWindow.destroy()
        mainWindow()
    
    else:
        
        messagebox.showerror("Sorry!", "Invalid credentials!")
        
        loginentry.delete(0, END)
        passentry.delete(0, END)
        loginentry.focus()
    

def signupButton():
            global signupWindow, createButton, var, userentry, passwentry, fnentry, lnentry
            signupWindow = Toplevel()
            signupWindow.geometry("350x350")
            signupWindow.resizable(width=var_progResizable, height=var_progResizable)
            signupWindow.grab_set()
            signupWindow.focus()
    
            signupWindow.title('Create an account ...')
            
            #
            userlabel = Label(signupWindow, text='Username: (Limit: 16)').pack()
            userentry = Entry(signupWindow)
            userentry.pack()
            passwlabel = Label(signupWindow, text='Password: (Limit: 24)').pack()
            passwentry = Entry(signupWindow)
            passwentry.pack()
            fnlabel = Label(signupWindow, text='First Name').pack()
            fnentry = Entry(signupWindow)
            fnentry.pack()
            lnlabel = Label(signupWindow, text='Last Name').pack()
            lnentry = Entry(signupWindow)
            lnentry.pack()
            #
            schoollabel = Label(signupWindow, text='School:').pack()
            var = StringVar(signupWindow)
            schools = {'School of Applied Science',
                       'School of Engineering',
                       'School of Hospitality',
                       'School of Infocomm',
                       'School of Management and Communication',
                       'School of Sports, Health and Leisure',
                       'School of Technology of the Arts'
                       }
            option = OptionMenu(signupWindow, var, *schools)
            option.config(bg='White')
            option.pack()
            var.set('School of Applied Science')
            
            #
            createButton = Button(signupWindow, text='Create', command=createButton).pack()
    
def createButton():
    getUsername = userentry.get()
    getPassword = passwentry.get()
    getFirstname = fnentry.get()
    getLastname = lnentry.get()
    getSchool = var.get()
    
    conn = pymysql.connect(host='localhost',
                            user='root',
                            passwd='',
                            db ='republicquiz')
                
    cursor = conn.cursor()    
    
    checkSQL = "SELECT * FROM `users` WHERE `username`='" + getUsername + "'"
    if cursor.execute(checkSQL):
        
        cursor.close()
        conn.close()
        
        messagebox.showerror("Error!", "Username already exist in database!")
    
    else:
        
        strSQL = "INSERT INTO `users` (`username`, `password`, `firstname`, `lastname`, `school`) VALUES (%s, %s, %s, %s, %s)"
        data = (getUsername, getPassword, getFirstname, getLastname, getSchool)
        cursor.execute(strSQL, data)
                
        conn.commit() #save, store changes
                
        cursor.close()
        conn.close()    
    
        messagebox.showinfo("Success!", "Account creation success! Please go ahead and login.")
        signupWindow.destroy()
   


loginWindow()