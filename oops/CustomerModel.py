
from Kalkulator import Kalkulator


class CustomerModel(Kalkulator):
    def multiply(self,angka1,angka2):
        if angka1 >5:
            self.nilai = super().sumNilai(angka1,angka2)
        else:
            self.nilai = angka1*angka2
        return self.nilai