def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command"
    return inner

def input_error_add_contact(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please."
    return inner

@input_error_add_contact
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def all_contacts(args, contacts):
    if not contacts:
        return "Contacts list is empty."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

@input_error
def search(args, contacts):
    name = args[0]
    phone = contacts.get(name)
    if phone:
        return f"{name}: {phone}"
    else:
        return f"Contact {name} not found."

def process_command(command, args, contacts):
    if command == "add":
        return add_contact(args, contacts)
    elif command == "all":
        return all_contacts(args, contacts)
    elif command == "phone":
        return search(args, contacts)
    else:
        return "Invalid command."

def run_bot():
    contacts = {}
    while True:
        command = input("Enter a command: ").strip().lower()
        if command == "exit":
            break
        args = input("Enter the argument for the command: ").strip().split()
        result = process_command(command, args, contacts)
        print(result)

if __name__ == "__main__":
    run_bot()
