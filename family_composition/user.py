from ..data_types.task import Task

class User:
    def __init__(self, first_name: str, second_name: str, email: str, password: str, age: int, info: str, list_of_events: list[Task]):
        self.first_name = first_name
        self.second_name = second_name
        self.email = email
        self.password = password
        self.age = age
        self.info = info
        self.list_of_events = list_of_events

    @property
    def first_name(self):
        return self.first_name
    @first_name.setter
    def first_name(self, value: str):
        self.first_name = first_name
    
    @property
    def second_name(self):
        return self.second_name
    @second_name.setter
    def second_name(self, value: str):
        self.second_name = second_name

    @property
    def email(self):
        return self.email
    @email.setter
    def email(self, value: str):
        self.email = email

    @property
    def password(self):
        return self.password
    @password.setter
    def password(self, value: str):
        self.password = password

    @property
    def age(self):
        return self.age
    @age.setter
    def age(self, value: int):
        self.age = age
    
    @property
    def list_of_events(self):
        return self.list_of_events
    @list_of_events.setter
    def list_of_events(self, value: list[Task]):
        self.list_of_events = list_of_events
