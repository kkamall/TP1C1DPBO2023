# Import File:
from Human import Human

# Kelas Mahasiswa (Child) - Human (Parent)
class Mahasiswa(Human):
    # Atribut Mahasiswa:
    __nim = ""
    __textbooks = 0
    __laptop = ""
    __grade = 0

    # Konstruktor
    def __init__(self, nama, jenis_kelamin, nim, textbooks, laptop):
        Human.__init__(self, nama, jenis_kelamin)
        self.__nim = nim
        self.__textbooks = textbooks
        self.__laptop = laptop

    # Setter
    def set_nim(self, nim):
        self.__nim = nim
    def set_textbooks(self, textbooks):
        self.__textbooks = textbooks

    def set_laptop(self, laptop):
        self.__laptop = laptop

    def set_grade(self, grade):
        self.__grade = grade

    # Getter
    def get_nim(self):
        return self.__nim
    
    def get_textbooks(self):
        return self.__textbooks

    def get_laptop(self):
        return self.__laptop
    
    def get_grade(self):
        return self.__grade
    
    # Method lainnya.
    def studying(self):
        return "Saya sedang belajar."

    def attending_class(self):
        return "Saya sedang menghadiri kelas."

    def working_on_assignment(self):
        return "Saya sedang mengerjakan tugas."