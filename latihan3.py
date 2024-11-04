saldo = 1000000

while True:
    print(f"\nSaldo saat ini: Rp{saldo}")
    print("1. Tarik Tunai")
    print("2. Keluar")
    pilihan = int(input("Pilih menu (1/2): "))

    if pilihan == 1:
        jumlah = int(input("Masukkan jumlah penarikan: Rp"))
        if jumlah <= saldo:
            saldo -= jumlah
            print(f"Penarikan berhasil. Sisa saldo Anda: Rp{saldo}")
        else:
            print("Saldo Anda tidak mencukupi!")
    elif pilihan == 2:
        print("Terima kasih telah menggunakan layanan ATM!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
