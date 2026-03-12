import numpy as np
import rasterio
import matplotlib.pyplot as plt

#Seleção das imagens
dataset1 = rasterio.open("B4-infravermelho.TIF")
dataset2 = rasterio.open("B5-infravermelho.TIF")


"""
#Printando os o tamanho e tipo de dado
print(dataset1.shape)
print(dataset1.dtypes)
print(dataset2.shape)
print(dataset2.dtypes)
"""

#Lendo os pixels e mudando o tipo de inteiro para float
matriz_red = dataset1.read().astype('float64')
matriz_infra = dataset2.read().astype('float64')


#Calculando o NDVI que é: matriz_infra+matriz_red/matriz_infra-matriz_red
soma = matriz_infra+matriz_red
subtracao = matriz_infra-matriz_red
NDVI = np.divide(subtracao, soma, where=soma!=0)#Só irá dividir onde for diferente de 0

#Adequando o resultado a minha condição. Resultado anterior [-1,1]. Novo resultado [0,1]
NDVI += 1
NDVI /= 2
NDVI[NDVI==0.5000]=0
#print(NDVI)

print(NDVI)
#Criação do arquivo novo com os valores do NDVI
metadados = dataset1.profile.copy()
metadados['dtype'] = 'uint16' #O uso do uint16 ocasiona a perca dos decimais e portanto de informações, mas para subir tudo no github precisei usa-lo. Para corrigir é só trocar o 'uint16' por 'float32' ou 'float64'(Ocupa mais espaço)

resultado_vegetacao = 'resultado_vegetacao.TIF'
with rasterio.open(resultado_vegetacao, 'w', **metadados) as dst:
    dst.write(NDVI[0], 1)

#Visualização do arquivo novo com o NDVI
plt.imshow(NDVI[0], cmap='RdYlBu')
plt.show()