class Contact:
    def __init__(self, first_name, last_name, phone, fav=False, **extras):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.fav = fav
        self.extras = extras

    def __str__(self):
        str_items = [
            "Имя: " + self.first_name,
            "Фамилия: " + self.last_name,
            "Телефон: " + self.phone,
            "В Избранных: " + ("да" if self.fav else "нет"),
        ]
        if self.extras:
            str_items.append("Дополнительная информация:")
            str_items.extend((
                "    {0}: {1}".format(key, value)
                for key, value in self.extras.items()
            ))
        return "\n".join(str_items)


class Book:
    def __init__(self, name):
        self.name = name
        self._contacts = []

    def add(self, contact):
        if contact not in self._contacts:
            self._contacts.append(contact)

    def del_by_phone(self, phone):
        self._contacts = [c for c in self._contacts if c.phone != phone]

    def all_favs(self):
        return (c for c in self._contacts if c.fav)

    def all_contacts(self, first_name=None, last_name=None):
        def matches(c):
            first_m = first_name is None or c.first_name == first_name
            secnd_m = last_name is None or c.last_name == last_name
            return first_m and secnd_m
        return (c for c in self._contacts if matches(c))

    def __str__(self):
        str_items = []
        str_items.append("Телефонная книга '{0}':".format(self.name))
        str_items.extend(str(c) for c in self._contacts)
        return "\n\n".join(str_items)
