contacts={}
def add_contact():
    name=input("enter the name:")
    number=input("enteer the phone number:")
    contacts[name]=number
    print("contact added successfully!")
    def search_contact():
        name=input("enter the name to search:")
        if name in contacts:
            print(f"phone number of {name}:{contacts[name]}")
        else:
            print("contact not found!")
            def display_contacts():
                print("contacts:")
                for name,number in contacts.items():
                    print(f"{name}:{number}")
                    while True:
                        print("1.add contact")
                        print("2.search contact")
                        print("3.display contacts")
                        print("4.exit")
                        choice=input("enter your choice:")
                        if choice=="1":
                            add_contact()
                        elif choice=="2":
                            search_contact()
                        elif choice=="3":
                            display_contacts()
                        elif choice=="4":
                            print("goodbye!")
                            break
                        else:
                            print("invalid choice.please try again.")
