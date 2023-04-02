# siswa (isinya ada nama dan asal)
# fungsi/operator = taaruf

class siswa:
    nama = None
    asal = None

    def taaruf(self):
        print(f'hallo saya {self.nama} dari {self.asal}')

# kita panggil

juan = siswa()
juan.nama = input("nama saya siapa?")
juan.asal = input("asal saya dari mana?")

# panggil fungsinya
juan.taaruf()
