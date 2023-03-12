# Import File:
from Human import Human
from DosenAssistant import DosenAssistant

# Kelas Mahasiswa (Child) - Human (Parent)
class Dosen(Human):
    # Atribut Mahasiswa:
    __nip = ""
    __whiteboardMarkers = 0
    __laptop = ""
    # Atribut komponen
    __mahasiswa = []

    # Konstruktor
    def __init__(self, nama, jenis_kelamin, nip, whiteboardMarkers, laptop, mahasiswa):
        Human.__init__(self, nama, jenis_kelamin)
        self.__nip = nip
        self.__whiteboardMarkers = whiteboardMarkers
        self.__laptop = laptop
        self.__mahasiswa = mahasiswa

    # Setter
    def set_nip(self, nip):
        self.__nip = nip

    def set_whiteboardMarkers(self, whiteboardMarkers):
        self.__whiteboardMarkers = whiteboardMarkers

    def set_laptop(self, laptop):
        self.__laptop = laptop

    def set_mahasiswa(self, mahasiswa):
        self.__mahasiswa = mahasiswa

    # Getter
    def get_nip(self):
        return self.__nip
    
    def get_whiteboardMarkers(self):
        return self.__whiteboardMarkers

    def get_laptop(self):
        return self.__laptop
    
    def get_mahasiswa(self):
        return self.__mahasiswa
    
    # Method lainnya.
    def teaching(self):
        return "Saya sedang mengajar."

    def give_assignment(self):
        return "Saya sedang memberikan tugas."

    def give_score(self, grade, dosenassistant, mahasiswa):
        if dosenassistant.get_flagAssignment():
            mahasiswa.set_grade(grade)
            return (f"Saya memberikan nilai {grade} kepada {mahasiswa.get_nim()} - {mahasiswa.get_nama()}.")
        else:
            return "Asisten dosen belum memberikan tugas."