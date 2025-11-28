import numpy as np
import time
class SistemaProducao:
    def __init__(self, matriz):
        self.__matriz = matriz
    
    @property
    def get_matriz(self):
        return self.__matriz
    
    def producao_total(self):
        return np.sum(self.__matriz, axis=1)

    def media_total(self):
        return np.mean(self.__matriz, axis=0)
    
    def fazenda_mais_produtiva(self):
        return np.argmax(self.producao_total())
    
    def mes_mais_produtivo(self):
        return np.argmax(self.media_total())
    
    def normatizacao(self):
        return (self.__matriz-np.min(self.__matriz))/(np.max(self.__matriz)-np.min(self.__matriz))
    
    def filtro_maior_media(self):
        return self.producao_total()[self.producao_total() > (np.mean(self.producao_total()))]
    
    def variacao(self):
        return ((self.__matriz[:, -1] - self.__matriz[:, 0]) / self.__matriz[:, 0]) * 100
    
    def desvio(self):
        desvio = np.std(self.__matriz, axis=1)
        return np.argmin(desvio), desvio[np.argmin(desvio)]