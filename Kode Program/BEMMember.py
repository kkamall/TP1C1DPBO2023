# Import File:
from Mahasiswa import Mahasiswa

# Kelas Mahasiswa (Child) - Human (Parent)
class BEMMember(Mahasiswa):
    # Atribut Mahasiswa:
    __jabatan = ""
    __program = []
    __innovation = []
    __flagDoingProgram = 0

    # Konstruktor
    def __init__(self, nama, jenis_kelamin, nim, textbooks, laptop, jabatan, program):
        Mahasiswa.__init__(self, nama, jenis_kelamin, nim, textbooks, laptop)
        self.__jabatan = jabatan
        self.__program = program

    # Setter
    def set_jabatan(self, jabatan):
        self.__jabatan = jabatan

    def set_program(self, program):
        self.__program = program

    def set_innovation(self, innovation):
        self.__innovation = innovation

    # Getter
    def get_jabatan(self):
        return self.__jabatan
    
    def get_program(self):
        return self.__program

    def get_innovation(self):
        return self.__innovation
    
    def get_flagDoingProgram(self):
        return self.__flagDoingProgram
    
    # Method lainnya.
    def doing_program(self):
        self.__flagDoingProgram = 1
        return "Kami sedang menjalankan program."

    def planning_innovation(self, innovation):
        self.__innovation = innovation
        return "Kami sedang merencanakan inovasi."

    def working_on_inovasi(self):
        return "Kami sedang menjalankan inovasi."