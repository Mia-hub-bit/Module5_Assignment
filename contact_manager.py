# contact_manager.py
class DuplicateContactError(Exception):
    def __init__(self, name):
        self.name = name
        super().__init__(f"Error: Contact '{name}' already exists.")

contacts = {}

def add_contact(name, phone):
    if name in contacts:
        raise DuplicateContactError(name)
    contacts[name] = phone
    return True

def find_contact(name):
    return contacts[name] 

def delete_contact(name):
    del contacts[name]
    return True

def main():
    MENU = "\n--- Phonebook ---\n1. Add\n2. Find\n3. Delete\n4. Exit"
    while True:
        print(MENU)
        choice = input("Choice: ").strip()
        
        try:
            if choice == '1':
                name = input("Name: ").strip()
                phone = input("Number: ").strip()
                if name and phone: 
                    add_contact(name, phone)
                    print(f"Added {name}.")

            elif choice == '2':
                name = input("Find Name: ").strip()
                if name: 
                    phone = find_contact(name)
                    print(f"Found: {name} -> {phone}")

            elif choice == '3':
                name = input("Delete Name: ").strip()
                if name: 
                    delete_contact(name)
                    print(f"Deleted {name}.")
            
            elif choice == '4':
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

        except DuplicateContactError as e:
            print(e)
        
        except KeyError:
            print("Contact not found.")
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
