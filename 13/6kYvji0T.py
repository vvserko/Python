import tkinter as tk
from user import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import pickle

# User
# ФИО entry
# Пол Radiobutton
# курит
# Адресс text
# Save = > в файл
# Load => загружать из файла

def save():
    name = ent_name.get()
    gender = selected_gender.get()
    smoking = selected_smoking.get()
    address = txt_address.get('1.1', tk.END)
    user = User(name, gender, smoking, address)
    path = asksaveasfilename()
    if not path:
        return
    with open(path, 'wb') as output_file:
        pickle.dump(user, output_file)

def load():
    path = askopenfilename()
    if not path:
        return
    with open(path, 'rb') as input_file:
        user = pickle.load(input_file)
        ent_name.delete(0)
        ent_name.insert(0, user.name)
        selected_gender.set(user.gender)
        selected_smoking.set(user.smoking)
        txt_address.delete('1.1', tk.END)
        txt_address.insert('1.0', user.address)

window = tk.Tk()
window.geometry('500x500')
window.title = 'Hello world'


lbl_name = tk.Label(master=window, text="ФИО")
lbl_name.grid(row=0, column=0)
ent_name = tk.Entry(master=window)
ent_name.grid(row=0, column=1)
lbl_gender = tk.Label(master=window, text= "Пол")
lbl_gender.grid(row=1, column=0)
frm_gender = tk.Frame(master=window)
frm_gender.grid(row=1, column=1)

selected_gender = tk.IntVar()
rdb_gender_m = tk.Radiobutton(master=frm_gender,
                              variable=selected_gender,
                              value=1,
                              text="М")
rdb_gender_m.pack()
rdb_gender_f = tk.Radiobutton(master=frm_gender,
                              variable=selected_gender,
                              value=0,
                              text="Ж")
rdb_gender_f.pack()

lbl_smoking = tk.Label(master=window, text='Курение')
lbl_smoking.grid(row=2, column=0)
selected_smoking = tk.BooleanVar()
chb_smoking = tk.Checkbutton(master=window, variable=selected_smoking)
chb_smoking.grid(row=2, column=1)
lbl_address = tk.Label(master=window, text='Адрес')
lbl_address.grid(row=3, column=0)
txt_address = tk.Text(master=window, height=20)
txt_address.grid(row=3, column=1)
bnt_save = tk.Button(master=window, text='Save', command=save)
bnt_save.grid(row=4, column=0)
bnt_load = tk.Button(master=window, text='Load', command=load)
bnt_load.grid(row=4, column=1)


if __name__ == '__main__':
    window.mainloop()