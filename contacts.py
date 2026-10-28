contacts=[]

def add_contact():
    name = input("Enter the name: ").strip()
    phone = input("Enter the phone number: ").strip().replace(" ", "")

    # Name must not be empty. Hyphens become spaces, then each word must be letters only
    # (so "John Doe" and "Jean-Pierre" are valid, "John2" is not).
    name_ok = bool(name) and all(part.isalpha() for part in name.replace("-", " ").split())
    # Phone is all digits, or starts with "+" followed by digits (e.g. "+3069...").
    phone_ok = phone.isdigit() or (phone.startswith("+") and phone[1:].isdigit())

    if name_ok and phone_ok:
        contacts.append({"name": name, "phone": phone})
        print(f"Contact {name} added successfully")
    else:
        print("Invalid name or phone number")

def search_contact():
    name = input("Enter the name: ")
    for contact in contacts:
        if contact['name'] == name:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
            return
    print("Contact not found")

def view_contacts():
    if not contacts:
        print("No contacts found")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
            
def delete_contacts():
    print("Διαγραφή ολων των επαφών")
    diagrafh = input("Θέλετε να διαγράψετε όλες τις επαφές; (Ν/Ο): ").upper()
    if diagrafh == "Ν":
        contacts.clear()
        print("Όλες οι επαφές διαγράφηκαν")
    else:
        print("Η διαγραφή ακυρώθηκε")

def main():
    while True:
        print("1. Προσθήκη νέας επαφής")
        print("2. Αναζήτηση επαφής")
        print("3. Προβολή όλων των επαφών")
        print("4. Διαγραφή όλων των επαφών")
        print("5. Έξοδος")
        choice = input("Επιλέξτε μια επιλογή: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            view_contacts()
        elif choice == "4":
            delete_contacts()
        elif choice == "5":
            break

if __name__ == "__main__":
    main()