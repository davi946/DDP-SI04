from animals import*

class Burung(Animal):
    def __init__(self, nama, manakan, hidup, berkembang_biak, jenis_Bulu, bunyi):
        super(). __init__(nama, manakan, hidup, berkembang_biak)
        self.jenis_Bulu = jenis_Bulu
        self.bunyi = bunyi

    def cetak_burung(self):
        super() .cetak()
        print(f'hewan ini berbulu {self.jenis_Bulu} dan hewan ini berbunyi {self.bunyi}')

beo = Burung ('Burung beo', 'biji-bijian', 'udara', 'bertelur', 'blue and orange', 'kamu jelek')
beo.cetak_burung() 

