# Import file:
from Mahasiswa import Mahasiswa
from BEMMember import BEMMember
from DPMMember import DPMMember
from DosenAssistant import DosenAssistant
from Dosen import Dosen

# Array of object.
list_mahasiswa = []
list_bemmember = []
list_dpmmember = []
list_dosenassistant = []
list_dosen = []
list_nilai = [90, 88, 60, 78, 95, 80]

# Instansiasi mahasiswa Biasa.
list_mahasiswa.extend([Mahasiswa("Afri", "M", "1000", 2, "Lenovo"), Mahasiswa("Anin", "F", "1001", 5, "Asus")])
list_bemmember.append(BEMMember("Rapi", "M", "1002", 3, "Oppo", "President", ["Belajar Bersama", "Mencoding Bersama"]))
# Instansiasi DPM member.
list_dpmmember.append(DPMMember("Alga", "M", "1003", 7, "Acer", "Ketua Divisi Eval"))
# Instansiasi dosen assistant.
list_dosenassistant.extend([DosenAssistant("Najmi", "F", "1004", 9, "Samsung", "Programming"), DosenAssistant("Bulan", "M", "1005", 8, "Asus", "Programming")])

# Menyatukan BEM member, DPM member, dan dosen assistant ke mahasiswa (menjadi mahasiswa keseluruhan).
list_mahasiswa.extend(list_bemmember)
list_mahasiswa.extend(list_dpmmember)
list_mahasiswa.extend(list_dosenassistant)

# Instansiasi dosen.
list_dosen.append(Dosen("Rose", "F", "2000", 3, "Acer", list_mahasiswa))

# Output list dosen.
print("[ LIST DOSEN ]")
for dosen in list_dosen:
    print(f"# {dosen.get_nip()} - {dosen.get_nama()}")
    
    # Output mahasiswa yang diajar dosen
    print("\t[ LIST MAHASISWA YANG DIAJAR ]")
    for mahasiswa in dosen.get_mahasiswa():
        print(f"\t# {mahasiswa.get_nim()} - {mahasiswa.get_nama()}", end="")
        if isinstance(mahasiswa, DPMMember):
            print(f" - DPM Member ({mahasiswa.get_jabatan()})")
        elif isinstance(mahasiswa, BEMMember):
            print(f" - BEM Member ({mahasiswa.get_jabatan()})")
        elif isinstance(mahasiswa, DosenAssistant):
            print(f" - Dosen Assistant ({mahasiswa.get_matkul()})")
        else:
            print(" - Mahasiswa Biasa")

print("\n[ INTERAKSI ]")
print("-- Pengurus DPM tidak bisa memberi masukan sebelum ketua BEM melaksanakan prokernya --")
print("\t# Anggota BEM belum melaksanakan proker.")
print(f"\t  - {list_dpmmember[0].give_appreciation(list_bemmember[0])}\n\t  - {list_dpmmember[0].give_recommendation(list_bemmember[0])}")
print("\t# Anggota BEM sudah melaksanakan proker.")
print(f"\t  - {list_bemmember[0].doing_program()}\n\t  - {list_dpmmember[0].give_appreciation(list_bemmember[0])}\n\t  - {list_dpmmember[0].give_recommendation(list_bemmember[0])}")
print("-- Dosen tidak bisa memberi nilai jika asisten dosen belum memberikan tugas --")
print("\t# Asisten dosen belum memberika tugas.")
for dosen in list_dosen:
    print(f"\t  # {dosen.get_nip()} - {dosen.get_nama()}")
    for index, mahasiswa in enumerate(dosen.get_mahasiswa()):
        print(f"\t    # {dosen.give_score(list_nilai[index], list_dosenassistant[0], mahasiswa)}")
print("\t# Asisten dosen sudah memberika tugas.")
print(f"\t  - {list_dosenassistant[0].give_assignment()}")
for dosen in list_dosen:
    print(f"\t  # {dosen.get_nip()} - {dosen.get_nama()}")
    for index, mahasiswa in enumerate(dosen.get_mahasiswa()):
        print(f"\t    # {dosen.give_score(list_nilai[index], list_dosenassistant[0], mahasiswa)}")