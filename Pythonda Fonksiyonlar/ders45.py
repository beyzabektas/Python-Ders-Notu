#Bankamatik Uygulaması

BeyzaHesap = {
    'ad': 'Beyza Bektaş',
    'hesapNo': '1234',
    'bakiye': 5000,
    'ekHesap': 2000
}

NurHesap = {
        'ad': 'Nur Bektaş',
        'hesapNo': '5432',
        'bakiye': 3000,
        'ekHesap': 1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    if hesap['bakiye'] >= miktar:
        hesap['bakiye'] -= miktar
        print('paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if toplam >= miktar:
            ekHesapKullanimi = input('ek hesap kullanılsın mı (e/h)')

            if ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('paranızı alabilirsiniz')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print('üzgünüz bakiye yetersiz.')
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır.Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")

paraCek(BeyzaHesap,2000)
print('********************************')
paraCek(BeyzaHesap,4000)
