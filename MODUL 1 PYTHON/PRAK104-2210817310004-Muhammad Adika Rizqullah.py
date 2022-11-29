a = int(input("Harga sepatu A adalah"))
b = int(input("Harga sepatu B adalah"))
dl = 0.13
hl = a - (a*dl)
d2 = 0.21
h2 = b - (b*d2)

print("Sepatu A mendapat diskon 13% sehingga harganya menjadi", round(hl))
print("Sepatu B mendapa diskon 21% sehingga harganya menjadi", round(h2))