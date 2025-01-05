import pickle
from internal.addressbook import AddressBook
from internal.record import Record

def load_contacts(filepath="./assistant/storage/phonebook.pkl"):
    """
    Load contacts from a pickle file.

    Args:
        filepath (str): Path to the pickle file.

    Returns:
        AddressBook: An instance of AddressBook with loaded contacts.
    """
    ab = AddressBook()
    try:
        with open(filepath, "rb") as file:
            print("Loading contacts...")
            contacts = pickle.load(file)
            if not isinstance(contacts, AddressBook):
                raise ValueError("Loaded data is not of type AddressBook.")
            return contacts
    except FileNotFoundError:
        print("No contacts found. Please add new contact.")
        return ab
    except (EOFError, ValueError) as e:
        print(f"Error loading contacts: {e}")
        return ab


def record_contacts(contacts, filepath="./assistant/storage/phonebook.pkl"):
    """
    Save contacts to a pickle file.

    Args:
        contacts (AddressBook): The AddressBook instance to save.
        filepath (str): Path to the pickle file.

    Returns:
        None
    """
    try:
        with open(filepath, "wb") as file:
            print("Saving contacts...")
            pickle.dump(contacts, file)
            print("Contacts saved successfully.")
    except Exception as e:
        print(f"Error saving contacts: {e}")