# fungsi garis
def garis():
    print("===================================")


tipe_kamar = input("masukan tipe kamar       :")
lama_inap = int(input("masukan lama menginap     :"))

# suoerior deluxe premium
if tipe_kamar == "superior":
    if lama_inap <= 2:
        harga_kamar = 10000*lama_inap
    elif lama_inap <= 4:
        harga_kamar = 90000*lama_inap
    elif lama_inap >= 5:
        harga_kamar = 80000*lama_inap
elif tipe_kamar == "deluxe":
    if lama_inap <= 2:
        harga_kamar = 150000*lama_inap
    elif lama_inap <= 4:
        harga_kamar = 135000*lama_inap
    elif lama_inap >= 5:
        harga_kamar = 120000*lama_inap
elif tipe_kamar == "premium":
    if lama_inap <= 2:
        harga_kamar = 200000*lama_inap
    elif lama_inap <= 4:
        harga_kamar = 180000*lama_inap
    elif lama_inap >= 5:
        harga_kamar = 160000*lama_inap

garis()

print("kamar yang anda pilih     :" , tipe_kamar)
print("lama menginap             :" , lama_inap , "hari")
print("total harga yang dibayar  :  Rp." , harga_kamar ,",00")