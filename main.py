import moduljastipp as jastip

def tampilkan_menu():
    print("\n===============================")
    print("🛒 PROGRAM JASA TITIP (JASTIP) 🛍️ 2")
    print("===============================")
    print("1. Tambah Pesanan Baru")
    print("2. Lihat Semua Pesanan")
    print("3. Simpan & Keluar")
    print("4. Keluar Tanpa Menyimpan")
    print("-------------------------------")

def main():
    pesanan_list = jastip.muat_pesanan()
    print("💡 Program Jastip dimulai. Data lama telah dimuat.")

    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan (1-4): ").strip()

        if pilihan == '1':
            jastip.tambah_pesanan(pesanan_list)

        elif pilihan == '2':
            jastip.lihat_pesanan(pesanan_list)

        elif pilihan == '3':
            jastip.simpan_pesanan(pesanan_list)
            print("\nTerima kasih! Program Jastip selesai.")
            break

        elif pilihan == '4':
            print("\n⚠️ Keluar tanpa menyimpan perubahan.")
            break

        else:
            print("❌ Pilihan tidak valid. Silakan masukkan angka 1 sampai 4.")

if __name__ == "__main__":
    main()