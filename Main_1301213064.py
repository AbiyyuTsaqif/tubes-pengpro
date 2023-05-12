#=============================A======================================
def buka_file(nama_file):                               #fungsi membaca file dengan parameter nama_file
    buka_file = open(nama_file, "r")                    #membuka file menggunakan read
    posisi = []                                         #membuat list kosong dengan nama posisi
    for baris in buka_file:                             #menggunakan perulangan untuk iterasi setiap baris file.txt
        stripped_line = baris.strip()                   #untuk menyatukan setiap baris menggunakan strip
        list_baru = stripped_line.split()               #untuk membuat list dari setiap baris
        posisi.append(list_baru)                        #menambahkan elemen list posisi dengan list_baru
    buka_file.close()                                   #untuk menutup file
    
    return posisi                                       #mengembalikan list posisi

#=============================B====================================== 
def siapa_menang(board):                                #fungsi menentukan siapa yang menang
    if board[0][0] == board[0][1] == board[0][2]:       #pengkondisian apabila semua tanda baris pertama bernilai sama
        if board[0][0] != '_':                          #pengkondisian apabila isi dari list baris pertama bukan '_'
            return board[0][0]                          #mengembalikan nilai baris 1 kolom 1 karena di awal bernilai sama
#=====untuk seterusnya, maksud dari pengkodisian sama tetapi hanya berbeda di tinjauan nya======
    if board[1][0] == board[1][1] == board[1][2]:       #untuk baris kedua
        if board[1][0] != '_':                        
            return board[1][0]                          #mengembalikan nilai baris 2 kolom 1 karena di awal bernilai sama
    if board[2][0] == board[2][1] == board[2][2]:       #untuk baris ketiga
        if board[2][0] != '_':
            return board[0][0]                          #mengembalikan nilai baris 3 kolom 1 karena di awal bernilai sama
    if board[0][0] == board[1][0] == board[2][0]:       #untuk kolom pertama
        if board[1][0] != '_':
            return board[0][0]                          #mengembalikan nilai baris 1 kolom 1 karena di awal bernilai sama
    if board[0][1] == board[1][1] == board[2][1]:       #untuk kolom kedua
        if board[0][1] != '_':
            return board[0][1]                          #mengembalikan nilai baris 1 kolom 2 karena di awal bernilai sama
    if board[0][2] == board[1][2] == board[2][2]:       #untuk kolom ketiga
        if board[0][2] != '_':
            return board[0][2]                          #mengembalikan nilai baris 1 kolom 3 karena di awal bernilai sama
    if board[0][0] == board[1][1] == board[2][2]:       #untuk diagonal dari kiri ke kanan
        if board[0][0] != '_':
            return board[0][0]                          #mengembalikan nilai baris 1 kolom 1 karena di awal bernilai sama
    if board[0][2] == board[1][1] == board[2][0]:       #untuk diagonal dari kanan ke kiri
        if board[0][2] != '_':
            return board[0][2]                          #mengembalikan nilai baris 1 kolom 3 karena di awal bernilai sama
    else:                                               #jika kondisi pada if tidak memenuhi
        return None                                     #akan mengembalikan 'None' karena tidak ada yang memenuhi kondisi diatas (tidak menang)

#=============================C======================================
def siapa_hampir_menang(board):
    if '_' in board[0][0]:                              #pengkondisian apabila ada '_' di baris 1 kolom 1
        if board[0][1] == board[0][2] != '_':           #pengkondisian apabila ada 2 simbol pada baris satu yang bernilai sama dan bukan merupakan '_'
            if board[0][1] == '0':                      #pengkondisian jika nilai itu '0' karena dalam kasus ini '0' jalan lebih dulu
                return (board[0][1])                    #mengembalikan isi baris 1 kolom 2 
            else:                                       #jika bukan bernilai '0'
                return (board[0][1])                    #mengembalikan isi baris 1 kolom 2
        elif board[1][0] == board[2][0] != '_':         #pengkondisian apabila ada 2 simbol di kolom satu yang bernilai sama dan bukan merupakan '_' 
            if board[1][0] == '0':
                return (board[1][0])                    #jika bernilai '0' maka mengembalikan nilai '0'
            else:
                return (board[1][0])                    #jika bukan bernilai '0' mengembalikan isi baris 1 kolom 2
        elif board[1][1] == board[2][2] != '_':         #pengkondisian apabila ada 2 simbol pada diagonal dari kiri ke kanan yang bernilai sama dan bukan merupakan '_'
            if board[1][1] == '0':                      
                return (board[1][1])                    #jika bernilai '0' maka mengembalikan nilai '0'
            else:
                return (board[1][1])                    #jika bukan bernilai '0' mengembalikan isi baris 2 kolom 2
#=====untuk seterusnya, maksud dari pengkodisian sama tetapi hanya berbeda di tinjauan nya======                                                   
    if '_' in board[0][1]:                              #untuk '_' di baris 1 kolom 2
        if board[0][0] == board[0][2] != '_':           #apabila di baris satu ada yang sama
            if board[0][0] == '0':                      #pengkondisian jika nilai itu '0' karena dalam kasus ini '0' jalan terlebih dahulu
                return (board[0][0])                    #mengembalikan isi baris 1 kolom 1
            else:                                       #jika bukan bernilai '0'
                return (board[0][0])                    #mengembalikan isi baris 1 kolom 1
        elif board[1][1] == board[2][1] != '_':         #apabila di kolom dua ada yang sama
            if board[1][1] == '0':                      #pengkondisian apabila
                return (board[1][1])
            else:
                return (board[1][1])                    #mengembalikan isi baris 2 kolom 2
    if '_' in board[0][2]:                              #untuk '_' di baris 1 kolom 3
        if board[0][0] == board[0][1] != '_':           #apabila di baris satu ada yang sama       
            if board[0][0] == '0':                      
                return (board[0][0])
            else:
                return (board[0][0])                    #mengembalikan isi baris 1 kolom 1
        elif board[1][2] == board[2][2] != '_':         #apabila di kolom ketiga ada yang sama
            if board[1][2] == '0':
                return (board[1][2])
            else:
                return (board[1][2])                    #mengembalikan isi baris 2 kolom 3
        elif board[1][1] == board [2][0] != '_':        #apabila di diagonal dari kanan atas ke kiri bawah ada yang sama
            if board[1][1] == '0':
                return (board[1][1])
            else:
                return (board[1][1])                    #mengembalikan isi baris 2 kolom 2
    if '_' in board[1][0]:                              #untuk '_' di baris 2 kolom 1
        if board[1][1] == board[1][2] != '_':           #apabila di baris kedua ada yang sama
            if board[1][1] == '0':
                return (board[1][1])
            else:
                return (board[1][1])                    #mengembalikan isi baris 2 kolom 2
        elif board[2][0] == board[1][0] != '_':         #apabila di kolom pertama ada yang sama
            if board[2][0] == '0':
                return (board[2][0])
            else:
                return (board[2][0])                    #mengembalikan isi baris 2 kolom 1
    if '_' in board[1][1]:                              #untuk '_' di baris 2 kolom 2
        if board[1][0] == board[1][2] != '_':           #apabila di baris kedua ada yang sama
            if board[1][0] == '0':
                return (board[1][0])
            else:
                return (board[1][0])                    #mengembalikan isi baris 2 kolom 1
        elif board[0][1] == board[2][1] != '_':         #apabila di kolom kedua ada yang sama
            if board[0][1] == '0':
                return (board[0][1])
            else:
                return (board[0][1])                    #mengembalikan isi baris 1 kolom 2
        elif board[0][2] == board[2][0] != '_':         #apabila di diagonal dari kanan atas ke kiri bawah ada yang sama
            if board[0][2] == '0':
                return (board[0][2])
            else:
                return (board[0][2])                    #mengembalikan isi baris 1 kolom 3
        elif board[0][0] == board[2][2] != '_':         #apabila di diagonal dari kiri atas ke kanan bawah ada yang sama
            if board[0][0] == '0':
                return (board[0][0])
            else:
                return (board[0][0])                    #mengembalikan isi baris 1 kolom 1
    if '_' in board[1][2]:                              #untuk '_' di baris 2 kolom 3                              
        if board[1][0] == board[1][1] != '_':           #apabila di baris kedua ada yang sama
            if board[1][0] == '0':
                return (board[1][0])
            else:
                return (board[1][0])                    #mengembalikan isi baris 2 kolom 1
        elif board[0][2] == board[2][2] != '_':         #apabila di kolom ketiga ada yang sama
            if board[0][2] == '0':
                return (board[0][2])
            else:
                return (board[0][2])                    #mengembalikan isi baris 3 kolom 1
    if '_' in board[2][0]:                              #untuk '_' di baris 3 kolom 1
        if board[2][1] == board[2][2] != '_':           #apabila di baris ketiga ada yang sama
            if board[2][1] == '0':
                return (board[2][1])
            else:
                return (board[2][1])                    #mengembalikan isi baris 3 kolom 2
        elif board[0][0] == board[1][0] != '_':         #apabila di kolom pertama ada yang sama
            if board[0][0] == '0':
                return (board[0][0])
            else:
                return (board[0][0])                    #mengembalikan isi baris 1 kolom 1
        elif board[0][2] == board[1][1] != '_':         #apabila di diagonal dari kanan atas ke kiri bawah ada yang sama
            if board[0][2] == '0':
                return (board[0][2])
            else:
                return (board[0][2])                    #mengembalikan isi baris 1 kolom 3
    if '_' in board[2][1]:                              #untuk '_' di baris 3 kolom 2
        if board[2][0] == board[2][2] != '_':           #apabila di baris ketiga ada yang sama
            if board[2][0] == '0':
                return (board[2][0])
            else:
                return (board[2][0])                    #mengembalikan isi baris 3 kolom 1
        elif board[0][1] == board[1][1] != '_':         #apabila di kolom kedua ada yang sama
            if board[0][1] == '0':
                return (board[0][1])
            else:
                return (board[0][1])                    #mengembalikan isi baris 1 kolom 2
    if '_' in board[2][2]:                              #untuk '_' di baris 3 kolom 3
        if board[2][0] == board[2][1] != '_':           #apabila di baris ketiga ada yang sama
            if board[2][0] == '0':
                return (board[2][0])
            else:
                return (board[2][0])                    #mengembalikan isi baris 3 kolom 1f
        elif board[0][2] == board[1][2] != '_':         #apabila di kolom ketiga ada yang sama
            if board[0][2] == '0':
                return (board[0][2])
            else:
                return (board[0][2])                    #mengembalikan isi baris 1 kolom 3
        elif board[1][1] == board[0][0] != '_':         #apabila di diagonal dari kanan atas ke kiri bawah ada yang sama
            if board[1][1] == '0':
                return (board[1][1])
            else:
                return (board[1][1])                    #mengembalikan isi baris 2 kolom 2
    else:
        return(None)                                    #apabila tidak ada kondisi yang terpenuhi maka akan mengembalikan None
    
#=============================MAIN PROGRAM======================================
print("===============SELAAMAT DATANG DI PROGRAM TIC TAC TOE===============")
nama_file = input("Masukkan nama file: ")                                       #menjadikan variabel nama_file sebagai input
print("Menu")                                                                   #membuat menu
print("1. Tampilkan file.txt dalam bentuk list")
print("2. Tampilkan siapa menang")
print("3. Tampilkan siapa hampir menang")
print("4. Tampilkan semua")
inputan = int(input("Silahkan masukkan pilihan anda: "))                        #input angka untuk memilih menu
if inputan == 1:                                                                #pengkondisian apabila inputan bernilai 1
    for i in buka_file(nama_file):                                              #perulangan untuk mengiterasikan list dalam list
        print (i)                                                               #mengeluarkan per-list dengan tujuan membentuk seperti papan permainan tic-tac-toe
elif inputan == 2:                                                              #pengkondisian apabila inputan bernilai 2
    print("pemenangnya adalah: ",siapa_menang(buka_file(nama_file)))            #memanggil fungsi siapa_menang untuk menentukan siapa yang menang
elif inputan == 3:                                                              #pengkondisian apabila inputan bernilai 3
    print(siapa_hampir_menang(buka_file(nama_file)), "hampir menang")           #memanggil fungsi siapa_hampir_menang untuk menentuka
elif inputan == 4:                                                              ##pengkondisian apabila inputan bernilai 4
    for i in buka_file(nama_file):                                              #memanggil semua fungsi di menu 1,2,3                      
        print (i)
    print("pemenangnya adalah: ",siapa_menang(buka_file(nama_file)))
    print(siapa_hampir_menang(buka_file(nama_file)), "hampir menang")