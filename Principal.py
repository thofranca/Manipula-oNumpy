import numpy as np
import Classe as cl
def gerar_matriz_producao(matricula=202513298, fazendas=50, meses=12):
    np.random.seed(matricula)
    matriz = np.zeros((fazendas, meses))
    for fazenda in range(50):
        base = 80 + (matricula % 100) + fazenda * 2
        variacao = np.random.normal(0, 10, 12)
        matriz[fazenda, :] = np.maximum(base + variacao, 20)
    return matriz

arr = cl.SistemaProducao(gerar_matriz_producao())
print(arr.producao_total())
print(arr.media_total())
print(arr.fazenda_mais_produtiva())
print(arr.mes_mais_produtivo())
print(arr.normatizacao())
print(arr.filtro_maior_media())
print(arr.variacao())
print(arr.desvio())





