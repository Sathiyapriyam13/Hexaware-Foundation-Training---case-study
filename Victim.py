class Victim:
    def __init__(self, victim_id, first_name, last_name, gender, phone, address, age):
        self._victim_id = victim_id
        self._first_name = first_name
        self._last_name = last_name
        self._gender = gender
        self._phone = phone
        self._address = address
        self._age = age

    def get_victim_id(self):
        return self._victim_id

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_gender(self):
        return self._gender

    def get_phone(self):
        return self._phone

    def get_address(self):
        return self._address

    def get_age(self):
        return self._age
