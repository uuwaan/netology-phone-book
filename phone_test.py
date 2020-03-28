import phone

CONTACTS = {
    "john": phone.Contact(
        first_name="John",
        last_name="Smith",
        phone="+71234567809",
        telegram="@johnny",
        email="johnny@smith.com",
    ),
    "mary": phone.Contact(
        first_name="Mary",
        last_name="Sue",
        phone="+75432167890",
        fav=True,
        skype="mary_sue",
        email="mary@heroes.org",
    ),
    "samir": phone.Contact(
        first_name="Samir",
        last_name="Duran",
        phone="+70987654321",
        icq="543123",
        email="s_duran@dominion.gov",
    )
}

book = phone.Book("Друзья")

print("\n=== Добавление контактов ===\n")
for contact in CONTACTS.values():
    print(contact, end="\n\n")
    book.add(contact)

print("\n=== Вывод содержимого книги ===\n")
print(book, end="\n\n")

print("\n=== Вывод избранных контактов ===\n")
for contact in book.all_favs():
    print(contact, end="\n\n")

print("\n=== Поиск контактов по имени и фамилии ===\n")
contact = CONTACTS["samir"]
print("Имя:", contact.first_name, end="\n\n")
found = book.all_contacts(first_name=contact.first_name)
for found_contact in found:
    print(found_contact, end="\n\n")

contact = CONTACTS["mary"]
print("Фамилия:", contact.last_name, end="\n\n")
found = book.all_contacts(last_name=contact.last_name)
for found_contact in found:
    print(found_contact, end="\n\n")

contact = CONTACTS["john"]
print("Имя и фамилия:", contact.first_name, contact.last_name, end="\n\n")
found = book.all_contacts(first_name=contact.first_name,
                          last_name=contact.last_name)
for found_contact in found:
    print(found_contact, end="\n\n")

print("\n=== Удаление по номеру телефона ===\n")
contact = CONTACTS["john"]
print("Номер телефона:", contact.phone)
book.del_by_phone(contact.phone)
print(book, end="\n\n")
