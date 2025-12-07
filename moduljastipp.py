import os

FILE_NAME = "data_jastip.txt"

def muat_pesanan():
    pesanan_list = []
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, 'r') as file:
                for line in file:
                    data = line.strip().split('|')
                    if len(data) == 4:
                        try:
                            pesanan = {
                                "pelanggan": data[0],
                                "barang": data[1],
                                "harga": float(data[2]),
                                "fee": float(data[3])
                            }
                            pesanan_list.append(pesanan)
                        except ValueError:
                            print(f"Peringatan: Baris data rusak (Non-numerik): {line.strip()}")
        except IOError:
            print(f"Error: Gagal membaca file {FILE_NAME}.")
    return pesanan_list

def simpan_pesanan(pesanan_list):
    try:
        with open(FILE_NAME, 'w') as file:
            for pesanan in pesanan_list:
                line = (f"{pesanan['pelanggan']}|{pesanan['barang']}|"
                        f"{pesanan['harga']}|{pesanan['fee']}\n")
                file.write(line)
        print("\n✅ Data pesanan berhasil disimpan!")
    except IOError:
        print(f"Error: Gagal menulis ke file {FILE_NAME}.")

def tambah_pesanan(pesanan_list):
    print("\n--- Tambah Pesanan Baru ---")
    pelanggan = input("Nama Pelanggan: ").strip()
    barang = input("Nama Barang: ").strip()

    while True:
        try:
            harga = float(input("Harga Barang (Rp): "))
            fee = float(input("Fee Jastip (Rp): "))
            break
        except ValueError:
            print("❌ Input Harga atau Fee harus berupa angka.")

    total_bayar = harga + fee

    pesanan_baru = {
        "pelanggan": pelanggan,
        "barang": barang,
        "harga": harga,
        "fee": fee,
    }

    pesanan_list.append(pesanan_baru)
    print(f"\n✅ Pesanan '{barang}' untuk {pelanggan} ditambahkan!")
    print(f"   Total Bayar: Rp{total_bayar:,.2f}")

def lihat_pesanan(pesanan_list):
    if not pesanan_list:
        print("\nBelum ada pesanan Jastip saat ini.")
        return

    print("\n--- Daftar Pesanan Jastip ---")
    print(f"{'No.':<4} | {'Pelanggan':<20} | {'Barang':<25} | {'Harga (Rp)':>12} | {'Fee (Rp)':>8} | {'Total (Rp)':>12}")
    print("-" * 88)

    total_semua_fee = 0
    total_semua_harga = 0

    for i, pesanan in enumerate(pesanan_list):
        harga = pesanan['harga']
        fee = pesanan['fee']
        total = harga + fee
        total_semua_fee += fee
        total_semua_harga += total

        print(
            f"{i+1:<4} | {pesanan['pelanggan']:<20} | {pesanan['barang']:<25} | "
            f"{harga:>12,.2f} | {fee:>8,.2f} | {total:>12,.2f}"
        )

    print("-" * 88)
    print(f"{'TOTAL KESELURUHAN':<61} | {'':<12} | {total_semua_fee:>8,.2f} | {total_semua_harga:>12,.2f}")
    print("-" * 88)