# Kelas Manusia
class Human():
    # Atribut Manusia:
    __nama = ""
    __jenisKelamin = ""

    # Konstruktor
    def __init__(self, nama, jenisKelamin):
        self.__nama = nama
        self.__jenisKelamin = jenisKelamin

    # Setter
    def set_nama(self, nama):
        self.__nama = nama

    def set_jenis_kelamin(self, jenis_kelamin):
        self.__jenis_kelamin = jenis_kelamin

    # Getter
    def get_nama(self):
        return self.__nama

    def get_jenis_kelamin(self):
        return self.__jenis_kelamin
    
    # Method lainnya.
    def eat(self):
        print("Saya sedang makan.")

    def drink(self):
        print("Saya sedang minum.")
        
    def sleep(self):
        print("Saya sedang tidur.")