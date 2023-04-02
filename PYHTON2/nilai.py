def garis():
    print("===================")

# input nilai
a = int(input("nilai A :"))
b = int(input("nilai B :"))
c = int(input("nilai C :"))

# urut gpu yahoooooo
urut = [a,b,c]
asc = sorted(urut)
des = sorted(urut, reverse=True)
# max min rata rata
jumlah = a+b+c
max = max(a,b,c)
min = min(a,b,c)
rata = jumlah / len(urut)
# output
print("urutan Nilai ascending  :", asc)
print("urutan Nilai descending  :", des)
print("nilai max  :", max)
print("nilai min  :", min)
print("nilai rata rata  : ", rata)