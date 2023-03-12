# [ TP1C1DPBO2023 ]

## Identitas:
- NIM   : 2102313
- Nama  : Muhammad Kamal Robbani
- Kelas : C1'21

## Janji:
Saya [Muhammad Kamal Robbani] dengan nim 2102313 mengerjakan Tugas Praktikum 1 DPBO dalam mata kuliah [Desain Pemrograman Berorientasi Objek] untuk keberkahan-Nya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

## Spesifikasi Soal:
&nbsp;&nbsp;&nbsp;&nbsp;Rapi (M) is a student as well as the President of BEM in his department. He has some friends with specific positions, such as Alga (M) who became a DPM member, or Najmi (F) and Bulan (M) who are the assistants of Mrs. Rose (F), a programming lecturer. However, there are some regular students, like Afri (M) and Anin (F).

&nbsp;&nbsp;&nbsp;&nbsp;As a happy human being, everyone could do what a human usually does, like eat, drink, and sleep. Meanwhile, Rapi as well as his friends have stuff a student usually has, such as NIM, a few textbooks, and a laptop. Besides, they could do what a student usually does, such as studying, attending classes, and working on assignments.

&nbsp;&nbsp;&nbsp;&nbsp;Fortunately enough, Rapi as a president of BEM, who has an enormous amount of programs and innovations on his mind, can do specific things such as doing a program, planning an innovation, and working on innovation. Meanwhile, Alga whose job is to monitor Rapi's activities will provide appreciation as well as recommendations. He always says “I appreciate your work” to every completed development from Rapi and his team. On the other hand, Najmi and Bulan may help Mrs. Rose in teaching and giving homework. Mrs. Rose herself, as a lecturer, has some stuff for teaching, such as NIP, some whiteboard markers, and a laptop. She also has to fulfill his duties by teaching, giving assignments, and giving scores.

&nbsp;&nbsp;&nbsp;&nbsp;Based on the story above, choose keywords that may be important, then make their design, objects, as well as their relations in OOP!

# Desain Program:
![image](https://user-images.githubusercontent.com/101335350/224519045-95b75e40-643d-4bff-a198-436e0d6fb9d4.png)
- Interaksi:
  - Pengurus DPM tidak bisa memberi masukan dan apresiasi sebelum ketua BEM melaksanakan prokernya.
  - Dosen tidak bisa memberi nilai jika asisten dosen belum memberikan tugas.
- Human:
  - Atribut Ambigu: -
  - Method:
    - get_...() => Mendapatkan value di suatu atribut.
    - set_...() => Memberi value kepada suatu atribut.
    - eat => Memberi info bahwa manusia sedang makan.
    - drink => Memberi info bahwa manusia sedang minum.
    - sleep => Memberi info bahwa manusia sedang tidur.
  - Relasi: -
  - Note:
    - Kelas Human dibangun untuk menghindari atirbut yang redundant dalam class Mahasiswa dan Dosen.
    - Atribut laptop tidak masuk ke dalam kelas Human karena dikhawatirkan akan muncul Child Class baru yang tidak memiliki atribut laptop.
- Mahasiswa:
  - Atribut Ambigu:
    - texbooks => Jumlah textbooks yang dimiliki mahasiswa.
    - laptop => Merek laptop yang dimiliki mahasiswa.
  - Method:
    - get_...() => Mendapatkan value di suatu atribut.
    - set_...() => Memberi value kepada suatu atribut.
    - studying => Memberi info bahwa manusia sedang belajar.
    - attending_class => Memberi info bahwa mahasiswa sedang mengikuti kelas.
    - working_on_assignment => Memberi info bahwa mahasiswa sedang mengerjakan tugas.
  - Relasi:
    - Mahasiswa is a Human, alasan:
      1. Objeknya sama, yaitu manusia.
      2. Atribut dalam kelas Human dapat diakomodir oleh kelas Mahasiswa.
  - Note:
    - Ditambahkan atribut grade untuk menyimpan nilai yang diberikan dari dosen.
    - Beberapa atribut dipindahkan ke class Human untuk menghindari inisialisasi atribut yang sama di kelas sibling-nya.
- Dosen:
  - Atribut Ambigu:
    - whiteboardMarkers => Jumlah spidol yang dimiliki dosen.
    - laptop => Merek laptop yang dimiliki dosen.
    - mahasiswa => Mahasiswa-mahasiswa yang diajar oleh dosen.
  - Method:
    - get_...() => Mendapatkan value di suatu atribut.
    - set_...() => Memberi value kepada suatu atribut.
    - teaching => Memberi info bahwa dosen sedang mengajar.
    - give_assignment => Memberi info bahwa dosen memberikan tugas.
    - give_score => Memberi nilai kepada mahasiswa yang diajar.
  - Relasi:
    - Dosen is a Human, alasan:
      1. Objeknya sama, yaitu manusia.
      2. Atribut dalam kelas Human dapat diakomodir oleh kelas Dosen.
    - Dosen has Mahasiswa, alasan:
      1. Dosen memiliki mahasiswa yang diajar, yaitu mahasiswa yang mengontrak mata kulaih yang diampunya.
  - Note:
    - Ditambahkan atribut mahasiswa untuk menyimpan object mahasiswa yang diajar dosen (atribut komponen).
    - Beberapa atribut dipindahkan ke class Human untuk menghindari inisialisasi atribut yang sama di kelas sibling-nya.
- BEMMember:
  - Atribut Ambigu:
    - flagDoingProgram => Penanda apakah member BEM sudah menjalankan program kerjanya.
  - Method:
    - get_...() => Mendapatkan value di suatu atribut.
    - set_...() => Memberi value kepada suatu atribut.
    - doing_program => Memberi info bahwa member BEM sedang mengerjakan program (setelahnya menjadi sudah).
    - planning_innovation => Memberi info bahwa member BEM sedang merencanakan innovasi dan sekaligus set nilai dari atribut innovation.
    - working_innovation => Memberi info bahwa member BEM sedang mengerjakan inovasi.
  - Relasi:
    - BEMMember is a Mahasiswa:
      1. Objeknya sama, yaitu mahasiswa.
      2. Atribut dalam kelas Mahasiswa dapat diakomodir oleh kelas BEMMember.
  - Note:
    - Method "set_innovation" tidak dibuat karena sudah tercantum dalam method "planning_innovation".
- DPMMember:
  - Atribut Ambigu: -
  - Method:
    - get_...() => Mendapatkan value di suatu atribut.
    - set_...() => Memberi value kepada suatu atribut.
    - give_appreciation => Memberi apresiasi kepada member BEM jika sudah menjalankan program kerjanya.
    - give_recommendation => Memberi rekomendasi terhadap program kerja yang sudah dijalankan member BEM.
  - Relasi:
    - DPMMember is a Mahasiswa, alasan:
      1. Objeknya sama, yaitu mahasiswa.
      2. Atribut dalam kelas Mahasiswa dapat diakomodir oleh kelas DPMMember.
  - Note: -
- DosenAssistant:
  - Atribut Ambigu:
    - flagAssignment => tanda bahwa asisten dosen sudah/belum memberikan tugas kepada mahasiswa.
    - matkul => Mata kuliah yang diajar asisten dosen.
  - Method:
    - get_...() => Mendapatkan value di suatu atribut.
    - set_...() => Memberi value kepada suatu atribut.
    - teaching => Memberi info bahwa asisten dosen sedang mengajar mahasiswa.
    - give_assignment => Memberi info bahwa asisten dosen memberikan tugas dan set nilai atirbut flagAssignment menjadi '1' (True).
  - Relasi:
    - DosenAssistant is a Mahasiswa, alasan:
      1. Objeknya sama, yaitu mahasiswa.
      2. Atribut dalam kelas Mahasiswa dapat diakomodir oleh kelas DosenAssistant.
  - Note:
    - Method "set_flagAssignment" tidak dibuat karena sudah termasuk dalam method "give_assignment" dan harus melalui method tersebut.

## Penjelasan Alur Main (Python)
1. *Import class* yang digunakan.
2. Inisialisasi list yang digunkan untuk menampung objek.
3. Menginstansiasi objek secara hardcode dan memasukannya ke dalam *list of object*.
4. Mengeluarkan *output* dengan struktur sebagai berikut:
  - List Dosen.
    - List Mahasiswa yang Diajar.
  - List Interaksi.
5. End

## Dokumentasi:
![image](https://user-images.githubusercontent.com/101335350/224519791-a19c18cb-13d4-4d98-9d0a-aaaddc7cb033.png)
