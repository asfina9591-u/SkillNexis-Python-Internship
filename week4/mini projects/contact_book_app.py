# Contact Book App using Dictionary
contacts = {}

def add_contact(name, number):
    contacts[name] = number

def search_contact(name):
    return contacts.get(name, "Not Found")

def update_contact(name, number):
    if name in contacts:
        contacts[name] = number
        return "Updated"
    return "Not Found"

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        return "Deleted"
    return "Not Found"

# Example usage
add_contact("Asfina", "9876543210")
print(search_contact("Asfina"))
print(update_contact("Asfina", "1234567890"))
print(delete_contact("Asfina"))
