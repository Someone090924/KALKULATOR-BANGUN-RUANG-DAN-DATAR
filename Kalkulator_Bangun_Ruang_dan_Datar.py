import time
import os
import math

def clear_terminal():
    # Check the operating system type
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/MacOS
        os.system('clear')

print("____________________________")
print("Kalkulator Bangun v1.0")
print("by : Johar Aja / Someone.py")
print("____________________________")
print("Kalkulator Bangun")
print("a: Bangun Datar ")
print("b: Bangun Ruang ")
pil_bang = input("Pilihan: ")

if pil_bang == "a":
    clear_terminal()
    print("1: Persegi")
    print("2: Segitiga")
    print("3: Lingkaran")
    bangun_datar = input("Pilih bangun datar: ")
    clear_terminal()

    if bangun_datar == "1":
        sisi = float(input("Masukkan panjang sisi persegi: "))
        print("Pilih operasi:")
        print("1: Luas")
        print("2: Keliling")
        opsi = input("Operasi yang dipilih: ")
        clear_terminal()

        if opsi == "1":
            print("Luas persegi =", sisi * sisi)
        elif opsi == "2":
            print("Keliling persegi =", 4 * sisi)
        else:
            print("Operasi tidak valid")

    elif bangun_datar == "2":
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        print("Pilih operasi:")
        print("1: Luas")
        print("2: Keliling")
        opsi = input("Operasi yang dipilih: ")
        clear_terminal()

        if opsi == "1":
            print("Luas segitiga =", 0.5 * alas * tinggi)
        elif opsi == "2":
            print("Keliling segitiga = (belum diimplementasikan)")
        else:
            print("Operasi tidak valid")

    elif bangun_datar == "3":
        jari_jari = float(input("Masukkan jari-jari lingkaran: "))
        print("Pilih operasi:")
        print("1: Luas")
        print("2: Keliling")
        opsi = input("Operasi yang dipilih: ")
        clear_terminal()

        if opsi == "1":
            print("Luas lingkaran =", math.pi * jari_jari ** 2)
        elif opsi == "2":
            print("Keliling lingkaran =", 2 * math.pi * jari_jari)
        else:
            print("Operasi tidak valid")

elif pil_bang == "b":
    clear_terminal()
    print("1: Balok")
    print("2: Tabung")
    print("3: Limas")
    print("4: Bola")
    bangun_ruang = input("Pilih bangun ruang: ")
    clear_terminal()

    if bangun_ruang == "1":
        p = float(input("Masukkan panjang balok: "))
        l = float(input("Masukkan lebar balok: "))
        t = float(input("Masukkan tinggi balok: "))
        print("Pilih operasi:")
        print("1: Volume")
        print("2: Luas Permukaan")
        opsi = input("Operasi yang dipilih: ")
        clear_terminal()

        if opsi == "1":
            print("Volume balok =", p * l * t)
        elif opsi == "2":
            print("Luas permukaan balok =", 2 * (p * l + p * t + l * t))
        else:
            print("Operasi tidak valid")

    elif bangun_ruang == "2":
        r = float(input("Masukkan jari-jari tabung: "))
        t = float(input("Masukkan tinggi tabung: "))
        print("Pilih operasi:")
        print("1: Volume")
        print("2: Luas Permukaan")
        opsi = input("Operasi yang dipilih: ")
        clear_terminal()

        if opsi == "1":
            print("Volume tabung =", math.pi * r ** 2 * t)
        elif opsi == "2":
            print("Luas permukaan tabung =", 2 * math.pi * r * (r + t))
        else:
            print("Operasi tidak valid")

    elif bangun_ruang == "3":
        sisi_alas = float(input("Masukkan panjang sisi alas limas: "))
        tinggi_limas = float(input("Masukkan tinggi limas: "))
        print("Pilih operasi:")
        print("1: Volume")
        print("2: Luas Permukaan")
        opsi = input("Operasi yang dipilih: ")
        clear_terminal()

        if opsi == "1":
            print("Volume limas =", (1/3) * sisi_alas ** 2 * tinggi_limas)
        elif opsi == "2":
            print("Luas permukaan limas = (belum diimplementasikan)")
        else:
            print("Operasi tidak valid")

    elif bangun_ruang == "4":
        jari_jari = float(input("Masukkan jari-jari bola: "))
        print("Pilih operasi:")
        print("1: Volume")
        print("2: Luas Permukaan")
        opsi = input("Operasi yang dipilih: ")
        clear_terminal()

        if opsi == "1":
            print("Volume bola =", (4/3) * math.pi * jari_jari ** 3)
        elif opsi == "2":
            print("Luas permukaan bola =", 4 * math.pi * jari_jari ** 2)
        else:
            print("Operasi tidak valid")

else:
    print("Pilihan tidak valid")
