import customtkinter as ctk
import time
import sqlite3

with sqlite3.connect(r"C:\Users\HP\Downloads\MyPythonDB.db") as conn:
    cur = conn.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS PyClass(
                Student_ID INT,
                Name TEXT,
                Gender TEXT,
                DOB TEXT,
                Score INT,
                Grade TEXT
                )
    ''')

def submit_func():
    student_id = id_entry.get()
    name = name_entry.get().title()
    gender = gender_entry.get().title()
    dob = dob_entry.get()
    score = int(score_entry.get())
    if score <= 100 and score > 69: grade = 'A'
    elif score >= 60: grade = 'B'
    elif score >= 50: grade = 'C'
    elif score >= 40: grade = 'D'
    elif score >= 0: grade = 'F'
    grade_entry.configure(state= 'normal')
    grade_entry.delete(0, ctk.END)
    grade_entry.insert(0, grade)
    grade_entry.configure(state= 'disabled')
    
    with sqlite3.connect(r"C:\Users\HP\Downloads\MyPythonDB.db") as conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO PyClass VALUES (?,?,?,?,?,?)',
                    (student_id, name, gender, dob, score, grade))

    notif_label.configure(text= 'Operation Successful!')
    window.after(3000, notif_manager)
    id_entry.delete(0, ctk.END)
    name_entry.delete(0, ctk.END)
    gender_entry.delete(0, ctk.END)
    dob_entry.delete(0, ctk.END)
    score_entry.delete(0, ctk.END)

def notif_manager():
    notif_label.configure(text= '')

def view_func():
    key = attr_options.get()
    value = attr_entry.get()
    print(value.isalpha())
    if value.isdigit(): value = int(value)
    else: value = f"{value.lower()}"
    print(value)
    with sqlite3.connect(r"C:\Users\HP\Downloads\MyPythonDB.db") as conn:
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM PyClass WHERE LOWER({key}) = ? or {key} = ?', (value, value))
        records = cur.fetchall()
    if not records: display_string = 'No Records Found'
    else:
        display_string_top = '%-15s | %-15s | %-15s | %-15s | %-15s | %-15s' %('Student_ID', 'Name','Gender', 'DOB','Score','Grade')
        display_string_body = ''
        for record in records:
            display_string_body += '\n%-15s | %-15s | %-15s | %-15s | %-15s | %-15s' %record
            
        display_string = display_string_top + display_string_body
    print(display_string)
    display_area.configure(text= display_string)
window = ctk.CTk()
window.geometry('900x900')
window.resizable(False, False)
window.grid_rowconfigure(0, weight= 1)
window.grid_columnconfigure(0, weight= 1)

main_tabview = ctk.CTkTabview(window)
main_tabview.grid(row= 0, column= 0, padx= 15, pady= 15, sticky= 'nsew')
add_tab = main_tabview.add('Add')
add_tab.grid_columnconfigure(1, weight= 1)
view_tab = main_tabview.add('View')
view_tab.grid_columnconfigure(1, weight= 1)
main_tabview.set('View')

### STUDENT INFO TAB
info_label = ctk.CTkLabel(add_tab, fg_color= 'transparent',
                          text= 'Student Information',
                          font= ('Times New Roman', 40,'bold'))
info_label.grid(row= 0, column= 0, padx= 15, pady= 15, sticky= 'nw', columnspan= 2)
id_label = ctk.CTkLabel(add_tab, fg_color= 'transparent',
                          text= 'Student ID: ',
                          font= ('Times New Roman', 30))
id_label.grid(row= 1, column= 0, padx= 15, pady= 15, sticky= 'nw')
id_entry = ctk.CTkEntry(add_tab, placeholder_text= 'Enter Student ID',
                          font= ('Times New Roman', 30), width= 500)
id_entry.grid(row= 1, column= 1, padx= 15, pady= 15, sticky= 'nsew')
name_label = ctk.CTkLabel(add_tab, fg_color= 'transparent',
                          text= 'Name: ',
                          font= ('Times New Roman', 30))
name_label.grid(row= 2, column= 0, padx= 15, pady= 15, sticky= 'nw')
name_entry = ctk.CTkEntry(add_tab, placeholder_text= 'Enter Name',
                          font= ('Times New Roman', 30), width= 500)
name_entry.grid(row= 2, column= 1, padx= 15, pady= 15, sticky= 'nsew')
gender_label = ctk.CTkLabel(add_tab, fg_color= 'transparent',
                          text= 'Gender: ',
                          font= ('Times New Roman', 30))
gender_label.grid(row= 3, column= 0, padx= 15, pady= 15, sticky= 'nw')
gender_entry = ctk.CTkEntry(add_tab, placeholder_text= 'Enter Gender',
                          font= ('Times New Roman', 30), width= 500)
gender_entry.grid(row= 3, column= 1, padx= 15, pady= 15, sticky= 'nsew')
dob_label = ctk.CTkLabel(add_tab, fg_color= 'transparent',
                          text= 'DOB: ',
                          font= ('Times New Roman', 30))
dob_label.grid(row= 4, column= 0, padx= 15, pady= 15, sticky= 'nw')
dob_entry = ctk.CTkEntry(add_tab, placeholder_text= 'Enter Date of Birth',
                          font= ('Times New Roman', 30), width= 500)
dob_entry.grid(row= 4, column= 1, padx= 15, pady= 15, sticky= 'nsew')
score_label = ctk.CTkLabel(add_tab, fg_color= 'transparent',
                          text= 'Score: ',
                          font= ('Times New Roman', 30))
score_label.grid(row= 5, column= 0, padx= 15, pady= 15, sticky= 'nw')
score_entry = ctk.CTkEntry(add_tab, placeholder_text= 'Enter Score',
                          font= ('Times New Roman', 30), width= 500)
score_entry.grid(row= 5, column= 1, padx= 15, pady= 15, sticky= 'nsew')
grade_label = ctk.CTkLabel(add_tab, fg_color= 'transparent',
                          text= 'Grade: ',
                          font= ('Times New Roman', 30))
grade_label.grid(row= 6, column= 0, padx= 15, pady= 15, sticky= 'nw')
grade_entry = ctk.CTkEntry(add_tab, placeholder_text= 'Enter Grade',
                           state= 'disabled', width= 500,
                          font= ('Times New Roman', 30))
grade_entry.grid(row= 6, column= 1, padx= 15, pady= 15, sticky= 'nsew')
submit_button = ctk.CTkButton(add_tab, text= 'Submit',
                              font= ('Times New Roman', 30),
                              command= submit_func)
submit_button.grid(row= 7, column= 0, columnspan= 2, padx= 15, pady= 15, sticky= 'ns')
notif_label = ctk.CTkLabel(add_tab, text= '', fg_color= 'transparent',
                           font= ('Times New Roman', 20), text_color= 'red')
notif_label.grid(row= 8, column= 0, columnspan= 2, sticky= 'ns')

### VIEW RECORDS TAB
view_label = ctk.CTkLabel(view_tab, fg_color= 'transparent',
                          text= 'View Records',
                          font= ('Times New Roman', 40,'bold'))
view_label.grid(row= 0, column= 0, columnspan= 2, padx= 15, pady= 15, sticky= 'nw')
attr_options = ctk.CTkOptionMenu(view_tab,font=('Times New Roman', 30),
                                 dropdown_font=('Times New Roman',15),
                                 values= ['Student_ID', 'Name', 'Gender', 'DOB', 'Score', 'Grade'])
attr_options.grid(row= 1, column= 0, padx= 15, pady= 15, sticky= 'nw')
attr_entry = ctk.CTkEntry(view_tab, placeholder_text= 'Student Info',
                          width= 450, font= ('Times New Roman', 30))
attr_entry.grid(row= 1, column= 1, padx= 15, pady= 15, sticky= 'nsew')
view_button = ctk.CTkButton(view_tab, text= 'View',
                            font= ('Times New Roman', 30),
                            command= view_func)
view_button.grid(row= 2, column= 0, columnspan= 2, padx= 15, pady= 15, sticky= 'ns')

display_area = ctk.CTkLabel(view_tab, height= 500, width= 800, anchor= 'center',
                            text= '', fg_color= 'grey',
                            text_color= 'white', corner_radius= 30,
                            font= ('Times New Roman', 21))
display_area.grid(row= 3, column= 0, columnspan= 2, padx= 15, pady= 15, ipadx= 10, sticky= 'nsew')


window.mainloop()


