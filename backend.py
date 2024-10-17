class UserData:
    users = []

    def __init__(self, user_name, surname, patronymic, mail, phone_number, password):
        self.user = user_name
        self.surname = surname
        self.patronymic = patronymic
        self.mail = mail
        self.phone_number = phone_number
        self.password = password

    @classmethod
    def users_table(cls, surname, user, patronymic, mail, phone_number, password):
        cls.users.append([surname, user, patronymic, mail, phone_number, password])

    @staticmethod
    def add_user():
        #print("Здравствуйте! Введите Ваши данные(имя, фалимия, отчество, адрес почты, номер телефона, пароль): ")
        user_info = input().split()
        UserData.users_table(user_info[0], user_info[1], user_info[2], user_info[3], user_info[4], user_info[5])
        user_ = UserData(user_info[0], user_info[1], user_info[2], user_info[3], user_info[4], user_info[5])
        #print(user_.info_user)
        user_.output_users()

    @property
    def info_user(self):
        return f'ФИО: {self.surname} {self.user} {self.patronymic}\nКонтактные данные: {self.mail}, {self.phone_number}.'

    @staticmethod
    def delete_user():
        print('Введите id пользователя, данные которого необходимо удалить: ')
        del_user = input()
        ManageTheatre.schedule.pop(int(del_user))
        #ManageTheatre.schedule.remove(int(del_perf))
        #del ManageTheatre.schedule[int(del_perf)]

    def output_users(self):
        print('Данные о пользователях: ')
        for i in range(len(self.users)):
            print(f'{self.users[i]}')

    def __del__(self):
        #print('Информация о пользователе была удалена.')
        pass

class ManageTheatre:
    schedule = ["Преступление и наказание", "Идиот", "Медный всадник", "Война и мир"]

    def __init__(self, performance, quantity, cost, time_perf):
        self.performance = performance
        self.quantity = quantity
        self.cost = cost
        self.time_perf = time_perf

    @classmethod
    def schedule_table(cls, performance, quantity, cost, time_perf):
        cls.schedule.append([performance, quantity, cost, time_perf])

    @staticmethod
    def change_schedule():
        print("Введите данные о представлении(наименование, количество мест, цена билета, время выступления): ")
        schedule_info = input().split()
        ManageTheatre.schedule_table(schedule_info[0], schedule_info[1], schedule_info[2], schedule_info[3])
        schedule_id = ManageTheatre(schedule_info[0], schedule_info[1], schedule_info[2], schedule_info[3])
        schedule_id.output_schedule()
        #print(schedule_id.info_schedule)
        ManageTheatre.delete_performance()
        schedule_id.output_schedule()

    @staticmethod
    def delete_performance():
        print('Введите id представления, которое необходимо удалить: ')
        del_perf = input()
        ManageTheatre.schedule.pop(int(del_perf))
        #ManageTheatre.schedule.remove(int(del_perf))
        #del ManageTheatre.schedule[int(del_perf)]

    @property
    def info_schedule(self):
        return f'Название представления: {self.performance}, количество мест: {self.quantity}, '
        f'стоимость билета: {self.cost}, время выступлений: {self.time_perf}'

    @staticmethod
    def select_view():
        print('Введите название выбранного представления: ')
        selected_view = str(input())
        sch = ManageTheatre.schedule
        for view in sch:
            if view == selected_view:
                wallet = ManageTheatre.schedule[sch.index(view)]

    def output_schedule(self):
        print('Расписание действующих представлений: ')
        for i in range(len(self.schedule)):
            print(f'{self.schedule[i]}')

    def __del__(self):
        print('Представление удалено из расписания.')

class Ticket:
    ticket_info = []
    time_ = 0
    name_perf = []
    place = 0

    def __init__(self, timing, cost):
        self.timing = timing
        self.cost = cost

    @classmethod
    def tickets_table(cls, timing, cost):
        cls.ticket_info.append([timing, cost])

    @property
    def info_ticket(self):
        return f'Время представления: {self.timing}, стоимость билета: {self.cost}'

#UserData.add_user()
#ManageTheatre.change_schedule()
