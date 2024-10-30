def kalkulator():
    """
    Program kalkulator sederhana yang dapat melakukan operasi dasar aritmatika
    (penjumlahan, pengurangan, perkalian, dan pembagian)
    """
    print("=== Program Kalkulator Sederhana ===")
    print("Operasi yang tersedia:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    
    try:
        # Input dari pengguna
        angka1 = float(input("\nMasukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        operator = input("Masukkan operator (+, -, *, /): ")
        
        # Proses perhitungan berdasarkan operator
        if operator == '+':
            hasil = angka1 + angka2
            print(f"\nHasil: {angka1} + {angka2} = {hasil}")
            
        elif operator == '-':
            hasil = angka1 - angka2
            print(f"\nHasil: {angka1} - {angka2} = {hasil}")
            
        elif operator == '*':
            hasil = angka1 * angka2
            print(f"\nHasil: {angka1} * {angka2} = {hasil}")
            
        elif operator == '/':
            if angka2 == 0:
                print("\nError: Pembagian dengan nol tidak diperbolehkan!")
            else:
                hasil = angka1 / angka2
                print(f"\nHasil: {angka1} / {angka2} = {hasil}")
                
        else:
            print("\nError: Operator tidak valid! Gunakan +, -, *, atau /")
            
    except ValueError:
        print("\nError: Masukkan angka yang valid!")
        
    print("\n=== Program Selesai ===")

# Menjalankan program
if __name__ == "__main__":
  kalkulator()