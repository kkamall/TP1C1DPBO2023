# Import File:
from Mahasiswa import Mahasiswa

# Kelas Mahasiswa (Child) - Human (Parent)
class DosenAssistant(Mahasiswa):
    # Atribut Mahasiswa:
    __matkul = ""
    __flagAssignment = 0

    # Konstruktor
    def __init__(self, nama, jenis_kelamin, nim, textbooks, laptop, matkul):
        Mahasiswa.__init__(self, nama, jenis_kelamin, nim, textbooks, laptop)
        self.__matkul = matkul

    # Setter
    def set_matkul(self, matkul):
        self.__matkul = matkul

    # Getter
    def get_matkul(self):
        return self.__matkul
    
    def get_flagAssignment(self):
        return self.__flagAssignment
    
    # Method lainnya.
    def teaching(self):
        return "Saya sedang mengajar."

    def give_assignment(self):
        self.__flagAssignment = 1
        return "Saya memberikan tugas."