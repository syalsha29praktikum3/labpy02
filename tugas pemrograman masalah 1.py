def hitung_harga_tiket():
    print("=== Program Pemesanan Tiket Bioskop ===")
    print("1. Reguler (Rp50.000)")
    print("2. VIP (Rp100.000)")
    
    # Input tipe tiket
    while True:
        try:
            tipe_tiket = int(input("\nPilih tipe tiket (1/2): "))
            if tipe_tiket in [1, 2]:
                break
            print("Error: Pilihan tidak valid. Silakan pilih 1 atau 2.")
        except ValueError:
            print("Error: Masukkan angka 1 atau 2.")
    
    # Input status member
    while True:
        member = input("Apakah anda memiliki kartu member? (y/n): ").lower()
        if member in ['y', 'n']:
            break
        print("Error: Masukkan 'y' untuk ya atau 'n' untuk tidak.")
    
    # Menggunakan operator ternary untuk menentukan harga dasar
    harga_dasar = 50000 if tipe_tiket == 1 else 100000
    
    # Menggunakan operator ternary untuk menghitung diskon
    diskon = 0.2 if member == 'y' else 0
    
    # Menghitung harga akhir
    harga_akhir = harga_dasar * (1 - diskon)
    
    # Output hasil
    print("\n=== Detail Pemesanan ===")
    print(f"Tipe Tiket: {'Reguler' if tipe_tiket == 1 else 'VIP'}")
    print(f"Status Member: {'Ya' if member == 'y' else 'Tidak'}")
    print(f"Harga Dasar: Rp{harga_dasar:,.0f}")
    print(f"Diskon: {diskon * 100:.0f}%")
    print(f"Total Bayar: Rp{harga_akhir:,.0f}")

# Menjalankan program
if __name__ == "__main__":
    hitung_harga_tiket()