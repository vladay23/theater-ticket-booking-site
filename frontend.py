from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from PIL import Image, ImageTk

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk

from back import *

class Window_entrance(Tk):
    def __init__(self):
        super().__init__()

        self.title("Авторизация")
        self.geometry("600x300")

        self.label1 = Label(self, text="Это страница авторизации. Пожалуйста, введите данные")
        self.label1.place(x=20, y=0)

        self.label2 = Label(self, text="Введите email")
        self.label2.place(x=20, y=20)
        self.entry1 = Entry(self)
        self.entry1.place(x=20, y=55)
        self.button1 = ttk.Button(self, text="ввести")
        self.button1["command"] = self.button_clicked_2
        self.button1.place(x=20, y=85)
        self.label3 = Label(self, text="Ваше email: ")
        self.label3.place(x=200, y=85)
        self.label4 = Label(self)
        self.label4.place(x=300, y=85)

        self.label5 = Label(self, text="Введите пароль")
        self.label5.place(x=20, y=135)
        self.entry2 = Entry(self)
        self.entry2.place(x=20, y=165)
        self.button2 = ttk.Button(self, text="ввести")
        self.button2["command"] = self.button_clicked_3
        self.button2.place(x=20, y=195)
        self.label6 = Label(self, text="Ваш пароль: ")
        self.label6.place(x=200, y=195)
        self.label7 = Label(self)
        self.label7.place(x=300, y=195)

        self.button0 = ttk.Button(self, text="закрыть")
        self.button0["command"] = self.button_clicked_1_0
        self.button0.place(x=20, y=250)

        self.button = ttk.Button(self, text="готово")
        self.button["command"] = self.button_clicked_1_e
        self.button.place(x=125, y=250)

    def button_clicked_1_0(self):
        self.destroy()

    def button_clicked_1_e(self):
        command = create_show_window()
        self.destroy()

    def button_clicked_2(self):
        self.label4["text"] = self.entry1.get()
    def button_clicked_3(self):
        self.label7["text"] = self.entry2.get()


class Window_registration(Tk):
    def __init__(self):
        super().__init__()

        self.title("Регистрация")
        self.geometry("600x500")

        self.label1 = Label(self, text="Это страница регистрации. Пожалуйста, введите данные")
        self.label1.place(x=20, y=0)

        self.label2 = Label(self, text="Введите ФИО")
        self.label2.place(x=20, y=20)
        self.entry1 = Entry(self)
        self.entry1.place(x=20, y=55)
        self.button1 = ttk.Button(self, text="ввести")
        self.button1["command"] = self.button_clicked_2
        self.button1.place(x=20, y=85)
        self.label3 = Label(self, text="Ваше ФИО: ")
        self.label3.place(x=200, y=85)
        self.label4 = Label(self)
        self.label4.place(x=300, y=85)

        self.label5 = Label(self, text="Введите телефон")
        self.label5.place(x=20, y=135)
        self.entry2 = Entry(self)
        self.entry2.place(x=20, y=165)
        self.button2 = ttk.Button(self, text="ввести")
        self.button2["command"] = self.button_clicked_3
        self.button2.place(x=20, y=195)
        self.label6 = Label(self, text="Ваш телефон: ")
        self.label6.place(x=200, y=195)
        self.label7 = Label(self)
        self.label7.place(x=300, y=195)

        self.label8 = Label(self, text="Введите email (логин)")
        self.label8.place(x=20, y=245)
        self.entry3 = Entry(self)
        self.entry3.place(x=20, y=275)
        self.button3 = ttk.Button(self, text="ввести")
        self.button3["command"] = self.button_clicked_4
        self.button3.place(x=20, y=305)
        self.label9 = Label(self, text="Ваш email: ")
        self.label9.place(x=200, y=305)
        self.label10 = Label(self)
        self.label10.place(x=300, y=305)

        self.label11 = Label(self, text="Придумайте пароль")
        self.label11.place(x=20, y=355)
        self.entry4 = Entry(self)
        self.entry4.place(x=20, y=385)
        self.parol1 = ''
        self.label12 = Label(self, text="Повторите пароль") # Проверка совпадение пароля
        self.label12.place(x=200, y=355)
        self.entry5 = Entry(self)
        self.entry5.place(x=200, y=385)
        self.parol2 = ''

        self.button4 = ttk.Button(self, text="ввести")
        self.button4["command"] = self.button_clicked_5
        self.button4.place(x=20, y=415)
        self.label13 = Label(self)
        self.label13.place(x=300, y=415)

        self.button0 = ttk.Button(self, text="закрыть")
        self.button0["command"] = self.button_clicked_1_0
        self.button0.place(x=20, y=465)

        self.button = ttk.Button(self, text="готово")
        self.button["command"] = self.button_clicked_1_r
        self.button.place(x=125, y=465)

    def button_clicked_1_0(self):
        self.destroy()

    def button_clicked_1_r(self):
        command = create_show_window()
        self.destroy()

    def button_clicked_2(self):
        self.label4["text"] = self.entry1.get()
        fio = self.entry1.get().split()
        self.surname = fio[0]
        self.name = fio[1]
        self.patronic = fio[2]
    def button_clicked_3(self):
        self.label7["text"] = self.entry2.get()
        self.phone_number = self.entry2.get()
    def button_clicked_4(self):
        self.label10["text"] = self.entry3.get()
        self.mail = self.entry3.get()
    def button_clicked_5(self):
        self.parol1 = self.entry4.get()
        self.parol2 = self.entry5.get()
        if self.parol1 == self.parol2:
            self.label13["text"] = 'Пароль записан'
            parol = self.parol1
        else:
            self.label13["text"] = 'Пароли не совпали'

        print(f'ФИО: {self.surname} {self.name} {self.patronic}\nКонтактные данные: {self.mail}, {self.phone_number}.')
        print(f"Ваш пароль: {parol}")

    def save_info(self):
        #UserData.users.append([self.surname, self.name, self.patronic, self.phone_number, self.mail, self.parol1])
        UserData.users_table(self.surname, self.name, self.patronic, self.phone_number, self.mail, self.parol1)
        user_ = UserData(self.surname, self.name, self.patronic, self.phone_number, self.mail, self.parol1)

class Window_of_show(Tk):
    def __init__(self):
        super().__init__()

        self.title("Окно бронирования")
        self.geometry("300x300")

        self.show = ""
        self.date = ""
        self.place = 0

        self.label12 = Label(self, text="Выберите представление")
        self.label12.place(x=20, y=0)

        shows = ["Преступление и наказание", "Идиот", "Медный всадник", "Война и мир"]
        shows_var = StringVar(value=shows[0])

        self.label = ttk.Label(self, textvariable=shows_var)
        self.label.place(x=20, y=20)

        self.combobox = ttk.Combobox(self, textvariable=shows_var, values=shows)
        self.combobox.place(x=20, y=40)

        self.label2 = Label(self, text="Выберите дату")
        self.label2.place(x=20, y=80)
        self.button_date_1 = ttk.Button(self, text='Календарь', command=example1)
        self.button_date_1.place(x=20, y=130)
        #self.button_date_2 = ttk.Button(self, text='?', command=example2)
        #self.button_date_2.place(x=200, y=220)


        self.label3 = Label(self, text="Выберите место")
        self.label3.place(x=20, y=180)
        self.button_place = ttk.Button(self, text="1.1")
        self.button_place["command"] = self.button_place_1
        self.button_place.place(x=20, y=220)
        self.button2 = ttk.Button(self, text="1.2")
        self.button2["command"] = self.button_place_2
        self.button2.place(x=120, y=220)
        self.button3 = ttk.Button(self, text="1.3")
        self.button3["command"] = self.button_place_3
        self.button3.place(x=220, y=220)

        self.button = ttk.Button(self, text="готово")
        self.button["command"] = self.button_clicked
        self.button.place(x=20, y=465)

    def button_clicked(self):
        command = create_rezalt_window()
        self.destroy()

    def button_place_1(self):
        self.place = 1.1
        place = self.place
        print(f"Ваше место: {place}")
        cost = 5000
        print(f'Стоимость билета: {cost}')
    def button_place_2(self):
        self.place = 1.2
        place = self.place
        print(f"Ваше место: {place}")
        cost = 4000
        print(f'Стоимость билета: {cost}')
    def button_place_3(self):
        self.place = 1.3
        place = self.place
        print(f"Ваше место: {place}")
        cost = 3000
        print(f'Стоимость билета: {cost}')

class Window_of_rezalt(Tk):
    def __init__(self):
        super().__init__()

        self.title("Окно подтверждения брони")
        self.geometry("200x200")

        #self.label1 = Label(self, text="Вы забронировали место: ")
        #self.label1.place(x=20, y=0)

        print(f'Дата представления: {Ticket.timing}')

        #self.label2 = Label(self, text= place)
        #self.label2.place(x=100, y=0)

        #self.label1 = Label(self, text="На представление: ")
        #self.label1.place(x=20, y=40)

        #self.label1 = Label(self, text="Когда: ")
        #self.label1.place(x=20, y=80)

        self.label1 = Label(self, text="Спасибо за бронь!", font=("Arial", 14),
                                                foreground="#01579B",
                                                background="#B3E5FC",
                                                justify = CENTER)
        self.label1.place(x=20, y=120)

def create_entrance_window():
    window = Window_entrance()

def create_registration_window():
    window = Window_registration()

def create_show_window():
    window = Window_of_show()

def create_rezalt_window():
    window = Window_of_rezalt()

def example1():
    def print_sel():
        data = cal.selection_get()
        cost = 5000
        Ticket.tickets_table(data, cost)
        ticket_ = Ticket(data, cost)
        Ticket.timing = data

    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()

'''def example2():
    top = tk.Toplevel(root)

    ttk.Label(top, text='Choose date').pack(padx=10, pady=10)

    cal = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    cal.pack(padx=10, pady=10)'''

if __name__ == '__main__':

    root = Tk()
    root.title("Афиша театра")
    root.geometry("500x500") # свободное место - картинка

    label = ttk.Label(text="                               Добро пожаловать!", font=("Arial", 14),
                                                foreground="#01579B",
                                                background="#B3E5FC",
                                                justify = CENTER)
    label.pack(fill=X, expand=True, anchor=N)

    btn = ttk.Button(root, text="                Войти               ", command=create_entrance_window)
    btn.place(x=50, y=50)
    btn = ttk.Button(root, text="         Зарегистрироваться         ", command=create_registration_window)
    btn.place(x=230, y=50)

    canvas = Canvas(bg="white", width=400, height=400)
    canvas.pack(anchor=CENTER, expand=1)
    python_image = PhotoImage(file=r"C:\Users\vlada\OneDrive\Рабочий стол\1-03-1.png")
    canvas.create_image(200, 455, anchor=S, image=python_image)

    root.mainloop()
