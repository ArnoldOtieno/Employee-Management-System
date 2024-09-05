mport pymysql
from tkinter import messagebox


def connect_database():
    global mycursor, conn
    try:
        conn = pymysql.connect(host="localhost", user="root", password="root")
        mycursor = conn.cursor()
    except Exception as e:
        messagebox.showerror('error', f'Something went wrong: {e}')

    mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
    mycursor.execute('USE employee_data')
    mycursor.execute('''CREATE TABLE IF NOT EXISTS data(
                        Id VARCHAR(20),
                        Name VARCHAR(50),
                        Phone VARCHAR(15),
                        Role VARCHAR(70), 
                        Gender VARCHAR(20), 
                        Salary DECIMAL(10,2)
                     )''')


def insert(id_ent, name, phone, role, gender, salary):
    mycursor.execute('INSERT INTO data VALUES (%s,%s,%s,%s,%s,%s)', (id_ent, name, phone, role, gender, salary))
    conn.commit()


def idEntryexists(idval):
    mycursor.execute('SELECT COUNT(*) FROM data WHERE Id=%s', idval)
    result = mycursor.fetchone()
    return result[0] > 0


def employeesview():
    mycursor.execute('SELECT * FROM data')
    result = mycursor.fetchall()
    return result


def new_update(new_id, new_name, new_phone, new_role, new_gender, new_salary):
    mycursor.execute('UPDATE data SET Name=%s, Phone=%s, Role=%s, Gender=%s, Salary=%s WHERE Id=%s',(new_name, new_phone, new_role, new_gender, new_salary, new_id))
    conn.commit()


def delete(id_val):
    mycursor.execute('DELETE FROM data WHERE Id=%s', id_val)
    conn.commit()


def search(option, search_val):
    mycursor.execute(f'SELECT * FROM data WHERE {option}=%s', search_val)
    result = mycursor.fetchall()
    return result


def delete_all_data():
    mycursor.execute('TRUNCATE TABLE data')
    conn.commit()


connect_database()


