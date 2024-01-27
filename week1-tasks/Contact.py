import json

def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        contacts = {}
    return contacts

def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=2)

def add_contact(contacts, name, phone, email):
    contacts[name] = {'phone': phone, 'email': email}
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully.")

def search_contact(contacts, name):
    contact = contacts.get(name)
    if contact:
        print(f"Contact Information for '{name}':")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
    else:
        print(f"Contact '{name}' not found.")

def update_contact(contacts, name, phone, email):
    if name in contacts:
        contacts[name]['phone'] = phone
        contacts[name]['email'] = email
        save_contacts(contacts)
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            add_contact(contacts, name, phone, email)

        elif choice == '2':
            name = input("Enter name to search: ")
            search_contact(contacts, name)

        elif choice == '3':
            name = input("Enter name to update: ")
            if name in contacts:
                phone = input("Enter new phone number: ")
                email = input("Enter new email address: ")
                update_contact(contacts, name, phone, email)
            else:
                print(f"Contact '{name}' not found.")

        elif choice == '4':
            print("Exiting Contact Management System.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
