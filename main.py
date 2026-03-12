import numpy
import rasterio

dataset1 = rasterio.open("B4-infravermelho.TIF")
dataset2 = rasterio.open("B5-infravermelho.TIF")


print(dataset1.shape)
print(dataset1.dtypes)
print(dataset2.shape)
print(dataset2.dtypes)

matriz_red = dataset1.read().astype('float64')
matriz_infra = dataset2.read().astype('float64')




a = 0
for numero in matriz_red:
    for num in numero:
        print(num)
        a += 1
print(a)
c = float(0.5884556513651658416513513651)

print(c:.2f)
