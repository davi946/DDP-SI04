class Gempa: 
    #konstruktor inisialisasi atribut 
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi 
        self.skala = skala

    #method penentu skala gempa 
    def dampak(self):
        #statement/logika
        if self.skala < 2:
            print('gempa tidak berasa')
        elif 2 <= self.skala <= 4:
            print('gempa berdampak bangunan')
        elif 4 <= self.skala <= 6:
            print('gempa berdampak bangunan')
        elif self.skala > 6:
            print('gempa berpotensi tsunami')
        
        #menampilkan lokasi dan skala gempa
        print(f'lokasi gempa: {self.lokasi}')
        print(f'skala gempa: {self.skala}')
        