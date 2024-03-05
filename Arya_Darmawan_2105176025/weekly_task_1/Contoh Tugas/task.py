class Mahasiswa:
    def __init__(self, nama, kelas, prodi, fakultas, tempat_tinggal, asal):
        self.nama = nama
        self.kelas = kelas
        self.prodi = prodi
        self.fakultas = fakultas
        self.tempat_tinggal = tempat_tinggal
        self.asal = asal

# Membuat objek mahasiswa
mahasiswa1 = Mahasiswa("Arya Darmawan", "Pendikom A 21", "Pendidikan Komputer", "FKIP", "Jalan Bung Tomo, Samarinda Seberang", "Samarinda")

# Menampilkan nilai atribut objek mahasiswa
print("Nilai atribut mahasiswa1:")
print("Nama:", mahasiswa1.nama)
print("Kelas:", mahasiswa1.kelas)
print("Program Studi:", mahasiswa1.prodi)
print("Fakultas:", mahasiswa1.fakultas)
print("Tempat Tinggal:", mahasiswa1.tempat_tinggal)
print("Asal:", mahasiswa1.asal)


