# Import File:
from Mahasiswa import Mahasiswa
from BEMMember import BEMMember

# Kelas Mahasiswa (Child) - Human (Parent)
class DPMMember(Mahasiswa):
    # Atribut Mahasiswa:
    __jabatan = ""

    # Konstruktor
    def __init__(self, nama, jenis_kelamin, nim, textbooks, laptop, jabatan):
        Mahasiswa.__init__(self, nama, jenis_kelamin, nim, textbooks, laptop)
        self.__jabatan = jabatan

    # Setter
    def set_jabatan(self, jabatan):
        self.__jabatan = jabatan

    # Getter
    def get_jabatan(self):
        return self.__jabatan
    
    # Method lainnya.
    def give_appreciation(self, bemmember):
        if bemmember.get_flagDoingProgram():
            return "Kami mengapresiasi kerja kamu."
        else:
            return "Tolong kerjakan program kalian sesuai dengan interval waktu yang telah diberikan."

    def give_recommendation(self, bemmember):
        if bemmember.get_flagDoingProgram():
            return "Kami memberikan rekomendasi."
        else:
            return "Program belum dikerjakan, kami belum bisa memberikan rekomendasi apapun."