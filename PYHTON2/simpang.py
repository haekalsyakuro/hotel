import statistics
# 1 cari rata rata
data = [90, 84, 88, 87, 83, 71]
reata = statistics.mean(data)

# 2 cari varian
list_varian[]
for bilangan in data:
    list_varian.append(
        (bilagan - rerata)**2
    )
varian = sum(list_varian) / (len(data) - 1)

# 3 hitaung setandar deviasi
simpang_baku = statistics.sqrt(varian)
print(f'data \t \t -> {data}')
print(f'simpangan baku \t -> {simpang_baku}')