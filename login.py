
m customtkinter import *
from PIL import Image
from tkinter import messagebox
root = CTk()

def login():
    if userNameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Fill in username and password')
    elif userNameEntry.get() == 'Arnold' and passwordEntry.get() == '1234':
        messagebox.showinfo('Login successful')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error', 'wrong credentials')


root.geometry('930x478')
root.resizable(0, 0)
root.title('Login page')
image = CTkImage(Image.open('bgimage.jpeg'), size=(930, 478))
imageLabel = CTkLabel(root, image=image, text='')
imageLabel.place(x=0, y=0)
headingLabel = CTkLabel(root, text = 'Employee Management System', bg_color='#FAFAFA', font=('Goudy Old Style', 20, 'bold'), text_color='dark blue')
headingLabel.place(x=20, y=100)
userNameEntry = CTkEntry(root,placeholder_text='Enter Your Username', width = 180)
userNameEntry.place(x=50, y=150)

passwordEntry = CTkEntry(root,placeholder_text='Enter Your Password', width=180, show='*')
passwordEntry.place(x=50, y=200)

loginButton = CTkButton(root, text='Login', cursor='hand2', command=login)
loginButton.place(x=70, y=250)
root.mainloop()
