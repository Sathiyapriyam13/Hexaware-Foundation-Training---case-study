# entity/Status.py

class Status:
    def __init__(self, status_id=None, status_name=None):
        self.__status_id = status_id
        self.__status_name = status_name

    def get_status_id(self):
        return self.__status_id

    def get_status_name(self):
        return self.__status_name

    def set_status_id(self, status_id):
        self.__status_id = status_id

    def set_status_name(self, status_name):
        self.__status_name = status_name
