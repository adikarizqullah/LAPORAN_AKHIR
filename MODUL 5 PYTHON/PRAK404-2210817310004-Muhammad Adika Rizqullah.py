from calendar import c
from pickle import TRUE
from re import A
while (TRUE):
 
            print("Pilih program\n")
            print("1.Penjumlahan\n")
            print("2.Pengurangan\n")
            print("3.Perkalian\n")
            print("4.Pembagian\n")
            print("5.Exit\n")
            A=int(input("Masukkan Pilihan : "))
            if A==5: 
               print("Terimakasih,telah menggunakan kalkulator Muhammad Adika Rizqullah") 
            elif A>=5:
                print("Input anda salah,silahkan coba lagi")
            else :
                B=float(input("Masukkan nilai pertama : "))
                C=float(input("Masukkan nilai kedua : "))
            if A==1: 
                print("Hasil penjumlahan antara %.2f dengan %.2f adalah %.2f" %(B, C, B+C)) 
            elif A ==2:
                print("Hasil penjumlahan antara %.2f dengan %.2f adalah %.2f" %(B, C, B-C))
            elif A==3:
                Z = (B*C) 
                print("Hasil penjumlahan antara %.2f dengan %.2f adalah %.2f" %(B, C, B*C))
            elif A==4:
                print("Hasil penjumlahan antara %.2f dengan %.2f adalah %.2f" %(B, C, B/C)) 