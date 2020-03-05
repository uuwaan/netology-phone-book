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
