from animals import*

class ular (Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ular, jenis_ular):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna_ular
        self.jenis = jenis_ular

    def cetak_ular(self):
        super().cetak()
        print(f'warna ular ini adalah {self.warna} dan jenisnya adalah {self.jenis}')

piton = ular('ular piton', 'tikus', 'air dan darat', 'bertelur', 'coklat', 'darat')
piton.cetak_ular()