import copy
from .name import Name
from .phone import Phone
from .birthday import Birthday
from .errorhandler import input_error

class Record():
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
    
    def __getstate__(self):
        return copy.deepcopy(self.__dict__)

    def __setstate__(self, state):
        self.__dict__.update(state)

    def get_name(self):
        return self.name
    
    def get_phones(self):
        return self.phones
    
    @input_error
    def get_birthday(self):
        try:
            date = self.birthday.get_value()
            return date
        except AttributeError:
            return None
    
    @input_error
    def add_phone(self, phone):
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)
        return f"Phone {phone} added for contact {self.name}."

    @input_error
    def edit_contact_phone(self, old_phone, new_phone):
        if not old_phone or not new_phone:
            raise ValueError("Please provide both an old phone and a new phone number.")
        for phone in self.phones:
            if phone.value == old_phone:
                self.phones.remove(phone)
                self.phones.append(Phone(new_phone))
                break
        return f"Phone number {old_phone} changed to {new_phone} for contact {self.name}."

    @input_error
    def delete_contact_phone(self, old_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                self.phones.remove(phone)
                break
        return f"Phone number {old_phone} deleted for contact {self.name}."
    
    @input_error
    def set_birthday(self, date):
        try:
            birthday = Birthday(date)
            self.birthday = birthday
            return f"Birthday for contact {self.name} set to {date}."
        except ValueError as e:
            return f"Invalid birthday: {e}"

        

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    