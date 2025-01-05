from internal.record import Record
from filer.filer import load_contacts, record_contacts

def parse_input(user_input):
    if not user_input:
        print("Please enter a command.")
        return "commands", []
    else: 
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args


def main():
    
    print("Welcome to the assistant bot!")
    ab = load_contacts()
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            record_contacts(ab)
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            new_contact = Record(args[0])
            if len(args) > 1: 
                print(new_contact.add_phone(args[1]))

            print(ab.add_record(new_contact))
        elif command == "change":
            print(ab.edit_phone(args[0], args[1]))
        elif command == "delete":
            print(ab.delete(args[1]))
        elif command == "remove":
            print(ab.delete_phone(args[0], args[1]))
        elif command == "all":
            print(ab.list_contacts())
        elif command == "find":
            print(ab.find(args[0]))
        elif command == "phone":
            print(ab.find_phone(args[0]))
        elif command == "add-birthday":
            print(ab.add_birthday(args[0], args[1]))
        elif command == "show-birthday":
            print(ab.show_birthday(args[0]))
        elif command == "birthdays":
            print(ab.birthdays())
        elif command == "commands":
            print("Available commands: hello, add, change, delete, all, find - for name search, phone - for the phone search, remove, close OR exit")
        else:
            print("Invalid command. If you need help, type 'commands'.")

if __name__ == "__main__":
    main()