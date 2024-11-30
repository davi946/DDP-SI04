import math

def l_kubus(sisi):
    luas = 6 * (sisi ** 2)
    print(f"Luas Kubus 6 x ({sisi} x {sisi}) = {luas}")

def l_balok(panjang, lebar, tinggi):
    luas = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
    print(f"Luas Balok 2 x ({panjang} x {lebar} + {panjang} x {tinggi} + {lebar} x {tinggi}) = {luas}")

def l_tabung(jari, tinggi):
    luas = 2 * 3.14 * jari * (jari + tinggi)
    print(f"Luas Tabung 2 x phi x {jari} x ({jari} + {tinggi}) = {luas}")

def l_kerucut(jari, tinggi):
    luas = 3.14 * jari * (jari + math.sqrt((tinggi ** 2) + (jari ** 2)))
    print(f"Luas Kerucut phi x {jari} x ({jari} + √({tinggi}² + {jari}²)) = {luas}")

def l_bola(jari):
    luas = 4 * 3.14 * (jari ** 2)
    print(f"Luas Bola 4 x phi x ({jari} x {jari}) = {luas}")