"""Helper bot module"""

def parse_input(user_input: str) -> tuple:
    """Parse user input and return command and its arguments.

    Args:
        user_input: 
            String that is user input command and its arguments.
    
    Returns:
        Tuple with command name and its arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args: list, contacts: dict) -> str:
    """Adds contact into dictionary.

    Args:
        args:
            List with user name and phone.
        contacts:
            Dictionary with contacts (name and phone).
    
    Returns:
        String with notification that contact is added.

    Raises:
       ValueError: Not enough values to unpack (expected 2, got 0).
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args: list, contacts: dict) -> str:
    """Change contact in dictionary.

    Args:
        args:
            List with user name and phone.
        contacts:
            Dictionary with contacts (name and phone).
    
    Returns:
        String with notification that contact is changed.

    Raises:
       ValueError: Not enough values to unpack (expected 2, got 0).
    """
    name, phone = args
    contacts[name] = phone
    return "Contact changed"

def show_phone(args: list, contacts: dict) -> str:
    """Shows phone number from dictionnary by user name.

    Args:
        args: 
            List containing the user's name.
        contacts:
            Dictionary with contacts (name and phone).
    
    Returns:
        A phone number string.

    Raises:
       KeyError: if no key found on the contacts dictionary.
    """
    name = args[0]
    return contacts[name]

def show_all(contacts: dict) -> None:
    """Shows all contacts from the dictionary.

    Args:
        contacts:
            Dictionary with contacts (name and phone).
    
    Returns:
        None.
    """
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def main():
    """Helper bot logic"""
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        try:
            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone":
                print(show_phone(args, contacts))
            elif command == "all":
                show_all(contacts)
            else:
                print("Invalid command.")
        except Exception:
            print('Invalid input')

if __name__ == "__main__":
    main()
