a = str(input("masukkan nama mahasiswa 1: "))
b = str(input("masukkan nama mahasiswa 2: "))
c = int(input("masukkan nilai mahasiswa 1: "))
d = int(input("masukkan nilai mahasiswa 2: "))

def jumlah_nilai_mahasiswa(nilai1,nilai2):
    total_nilai = nilai1 + nilai2
    return total_nilai

print(a, c)
print(b, d)
print("jumlah nilai:",jumlah_nilai_mahasiswa(c,d))