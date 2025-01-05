from collections import UserDict
import copy
from .errorhandler import input_error
from .birthday import Birthday

class AddressBook(UserDict):
        
    def list_contacts(self):
        if not self.data:
            return "No contacts found."
        return "Contacts:\n" + "\n".join(f"- {record}" for name, record in self.data.items())
    
    def __getstate__(self):
        return copy.deepcopy(self.__dict__)

    def __setstate__(self, state):
        self.__dict__.update(state)
    
    @input_error
    def add_record(self, contact):
        if not contact:
            raise ValueError("No contact provided.")
        
        contact_name = str(contact.get_name())
        if not contact_name:
            raise ValueError("Contact name is empty.")
        
        contact_key = contact_name.casefold()
        
        if contact_key in self.data:
            self.data[contact_key] = contact
            return f"Contact {contact_name} changed!"
        else:
            self.data[contact_key] = contact
            return f"Contact {contact_name} created!"
        

    @input_error
    def find(self, name):
        name = name.casefold()
        for dict_name, record in self.data.items():
            if dict_name == name:
                return record
        raise KeyError("Contact not found.")
    
    @input_error
    def find_phone(self, phone):
        for name, contact in self.data.items():
            for contact_phone in contact.get_phones():
                if phone == contact_phone.get_value():
                    return contact
        return f"Phone number '{phone}' not found in address book."

    
    @input_error
    def edit_phone(self, name, old_phone, new_phone):
        contact = self.find(name)
        contact.edit_contact_phone(old_phone, new_phone)
        self.data[name.casefold()] = contact
        return contact.__str__()
    
    @input_error
    def delete(self, name):
        contact = self.find(name)
        del self.data[name.casefold()]
        return contact
    
    @input_error
    def delete_phone(self, name, old_phone):
        contact = self.find(name)
        return contact.delete_contact_phone(old_phone)
    
    @input_error
    def add_birthday(self, name, date):
        if not name:
            raise ValueError("Name cannot be empty.")
        
        contact = self.find(name)
        if not contact:
            raise KeyError(f"Contact '{name}' not found.")
        
        if not date:
            raise ValueError("Birthday cannot be empty.")
        
        contact.set_birthday(date)
        self.data[name.casefold()] = contact
        return f"Birthday for contact {contact.get_name()} set to {date}."
        

    @input_error
    def show_birthday(self, name):
        if not name:
            raise ValueError("Name cannot be empty.")
        
        contact = self.find(name)
        if not contact:
            raise KeyError(f"Contact '{name}' not found.")
        
        birthday = contact.get_birthday()
        if birthday is None:
            return f"Birthday for contact '{name}' is not set."
        
        return birthday

    @input_error
    def birthdays(self):
        return Birthday.get_upcoming_birthdays(users=self.data)

