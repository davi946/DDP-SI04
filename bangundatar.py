import math 

def l_persegi(sisi):
    luas = sisi*sisi 
    keliling = sisi*sisi*sisi*sisi
    print(f'Luas Persegi{sisi} * {sisi} = {luas}')
    print(f'Keliling Persegi adalah {keliling}')

def persegi_panjang (panjang, lebar):
    luas = panjang*lebar
    print('hasil luas persegi panjang dari', panjang, 'x', lebar, '=', luas) 

def segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    print(f'luas lingkaran adalah 1/2 * {alas} * {tinggi}')

def l_lingkaran(r1, r2):
    luas = 3.14 * r1 * r2
    print('luas lingkaran adalah phi * {r1} * {r2} = {luas}') 