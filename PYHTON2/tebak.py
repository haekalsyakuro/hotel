
def garis():
    print("================")

import random
angka_rahasia = random.randint(1,100)

garis()
print("kami talah memiliki angka, silahkan tebak")
garis()

while True:
    jawaban = int(input("\n masukan angka   :"))
    if jawaban == angka_rahasia:
        print("selamat anda menebak dengan benar")
    else:
        print(
            'tebakan mu terlalu '
            'terkecil'if jawaban < angka_rahasia else 'besar'
        )
