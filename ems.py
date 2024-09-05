ustomtkinter import *
from PIL import Image
from tkinter import ttk, messagebox
import database


def delete_all():
    result = messagebox.askyesno('Confirm', 'Do you really want to delete entire data')
    if result:
        database.delete_all_data()


def show_all():
    view_employees()
    searchCombobox.set('Search By')
    searchEntry.delete(0, END)


def delete_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error', 'select data for deletion')
    else:
        database.delete(idEntry.get())
        view_employees()
        clear()
        messagebox.showerror('Error', 'Data deleted')


def search_employee():
    if searchCombobox.get() == 'Search By':
        messagebox.showerror('Error', 'Selection search option')
    elif searchEntry.get() == '':
        messagebox.showerror('Error', 'Enter value to search')
    else:
        searched_data = database.search(searchCombobox.get(), searchEntry.get())
        tree.delete(*tree.get_children())
        for employee in searched_data:
            tree.insert('', END, values=employee)


def update_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error', 'select employee to update')
    else:
        database.new_update(idEntry.get(), nameEntry.get(), phoneEntry.get(), roleCombobox.get(), genderCombobox.get(), salaryEntry.get())
        view_employees()
        clear()
        messagebox.showinfo('Success', 'Update successful')


def selection(event):
    selected_item = tree.selection()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        idEntry.insert(0, row[0])
        nameEntry.insert(0, row[1])
        phoneEntry.insert(0, row[2])
        roleCombobox.set(row[3])
        genderCombobox.set(row[4])
        salaryEntry.insert(0, row[5])


def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0, END)
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    roleCombobox.set('database engineer')
    genderCombobox.set('Male')
    salaryEntry.delete(0, END)
# Functions idEntry.get() == '' or nameEntry.get() == '' or phoneEntry.get() == '' or salaryEntry.get() == '':
#         mess


def addEmployee():
    if idEntry.get() == '' or nameEntry.get() == '' or phoneEntry.get() == '' or salaryEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    elif database.idEntryexists(idEntry.get()):
        messagebox.showerror('Error', 'Id already exists')
    elif not idEntry.get().startswith('EMP'):
        messagebox.showerror('error', 'id must start with EMP e.g {EMP1} FOR ID 1')
    else:
        database.insert(idEntry.get(), nameEntry.get(), phoneEntry.get(), roleCombobox.get(), genderCombobox.get(), salaryEntry.get())
        messagebox.showinfo('Success', 'Data added')
        clear()
        view_employees()


# displaying employees
def view_employees():
    tree.delete(*tree.get_children())
    employees = database.employeesview()
    for employee in employees:
        tree.insert('', END, values=employee)


# GUI part
window = CTk()
window.title('Employee Management System')
window.geometry('930x580+100+100')
window.resizable(0,0)
window.configure(fg_color='#161c30')
emsimage = CTkImage(Image.open('emp-payroll.jpeg'), size=(930,158))
emslogo = CTkLabel(window, image=emsimage, text='')
emslogo.grid(row=0, column=0, columnspan=2)

leftFrame = CTkFrame(window, fg_color='#161c30')
leftFrame.grid(row=1, column=0, padx=10, sticky='ew')

idLabel = CTkLabel(leftFrame, text='Id', font=('arial', 18, 'bold'), text_color='white')
idLabel.grid(row=0,column=0, padx=50, pady=10, sticky='ew')

idEntry = CTkEntry(idLabel, font=('arial', 15, 'bold'), width=180)
idEntry.grid(row=0, column=1)

nameLabel = CTkLabel(leftFrame, font=('arial', 18, 'bold'), text='Name', text_color='white')
nameLabel.grid(row=1, column=0, padx=50, pady=10, sticky='ew')

nameEntry = CTkEntry(nameLabel, font=('arial', 15, 'bold'), width=180)
nameEntry.grid(row=0, column=1)

phoneLabel = CTkLabel(leftFrame, text='Phone', font=('arial', 18, 'bold'), text_color='white')
phoneLabel.grid(row=2, column=0, padx=50, pady=10, sticky='ew')

phoneEntry = CTkEntry(phoneLabel, font=('arial', 15, 'bold'), width=180)
phoneEntry.grid(row=0, column=1, pady=0, sticky='e')

roleLabel = CTkLabel(leftFrame, text='Role', font=('arial', 18, 'bold'), text_color='white')
roleLabel.grid(row=3,column=0, padx=50, pady=10, sticky='ew')

roleValues = ['database engineer', 'cloud architect', 'Business Analyst', 'Technical Writer', 'Network Engineer', 'SOC Analyst']
roleCombobox = CTkComboBox(roleLabel, values=roleValues, width=180, font=('arisl', 15, 'bold'), state='readonly')
roleCombobox.grid(row=0, column=1)
roleCombobox.set(roleValues[0])

genderLabel = CTkLabel(leftFrame, text='Gender', font=('arial', 18, 'bold'), text_color='white')
genderLabel.grid(row=4, column=0, sticky='ew', padx=50, pady=10)

genderValues= ['Male','Female']
genderCombobox = CTkComboBox(genderLabel, font=('arial', 15, 'bold'), width=180, values=genderValues, state='readonly')
genderCombobox.grid(row=0, column=1)
genderCombobox.set(genderValues[0])

salaryLabel = CTkLabel(leftFrame, text='Salary', font=('arial', 18, 'bold'), text_color='white')
salaryLabel.grid(row=5, column=0, padx=50, pady=10, sticky='ew')

salaryEntry = CTkEntry(salaryLabel, font=('arial', 15, 'bold'), width=180)
salaryEntry.grid(row=0, column=1)


rightFrame = CTkFrame(window, fg_color='#161c30')
rightFrame.grid(row=1, column=1)

searchValues = ['Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary']
searchCombobox = CTkComboBox(rightFrame, state='readonly', values=searchValues)
searchCombobox.grid(row=0, column=0)
searchCombobox.set('Search By')

searchEntry = CTkEntry(rightFrame)
searchEntry.grid(row=0, column=1)

searchButton = CTkButton(rightFrame, text='Search', width=100, command=search_employee)
searchButton.grid(row=0, column=2, pady=5, padx=2)

showAllButton = CTkButton(rightFrame, text='Show all', width=100, command=show_all)
showAllButton.grid(row=0, column=3)

tree = ttk.Treeview(rightFrame, height=10)
tree.grid(row=1, column=0, columnspan=4)
tree['columns'] = ('Id',  'Name', 'Phone', 'Role', 'Gender', 'Salary')

tree.heading('Id', text='Id')
tree.heading('Name', text='Name')
tree.heading('Phone', text='Phone')
tree.heading('Role', text='Role')
tree.heading('Gender', text='Gender')
tree.heading('Salary', text='Salary')

tree.config(show='headings')
tree.column('Id', width=50)
tree.column('Name', width=100)
tree.column('Phone', width=100)
tree.column('Role', width=100)
tree.column('Gender', width=100)
tree.column('Salary', width=100)

style = ttk.Style()
style.configure('Treeview.Heading', font=('arial', 16, 'bold'))
style.configure('Treeview', font=('arial', 10, 'bold'), background='#161c30', rowheight=30, foreground='white')

buttonFrame = CTkFrame(window, fg_color='#161c30')
buttonFrame.grid(row=2, column=0, columnspan=2)

newEmployeeButton = CTkButton(buttonFrame, text='New Employee', width=160, font=('arial', 15, 'bold'), corner_radius=15, command=lambda : clear(True))
newEmployeeButton.grid(row=0, column=0, pady=5)
addEmployeeButton = CTkButton(buttonFrame, command=addEmployee,text='Add Employee', width=160, font=('arial', 15, 'bold'), corner_radius=15)
addEmployeeButton.grid(row=0, column=1, padx=10)
updateEmployeeButton = CTkButton(buttonFrame, text='Update Employee', command=update_employee, width=160, font=('arial', 15, 'bold'), corner_radius=15)
updateEmployeeButton.grid(row=0, column=2, padx=10)
deleteEmployeeButton = CTkButton(buttonFrame, text='Delete Employee', width=160, font=('arial', 15, 'bold'), corner_radius=15, command=delete_employee)
deleteEmployeeButton.grid(row=0, column=3, padx=10)
deleteAllEmployeeButton = CTkButton(buttonFrame, text='Delete All', command=delete_all, width=160, font=('arial', 15, 'bold'), corner_radius=15)
deleteAllEmployeeButton.grid(row=0, column=4, padx=10)

scrollBar = ttk.Scrollbar(rightFrame, orient=VERTICAL, command=tree.yview)
scrollBar.grid(row=1, column=4, sticky='ns')
tree.config(yscrollcommand=scrollBar.set)

view_employees()
window.bind('<ButtonPress>', selection)
window.mainloop()
