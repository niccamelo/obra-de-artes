class Leilao:
    def __init__(self, id, obra_de_arte, lance_incial, data_encerramento, termino ):
        self.id = id
        self.obra_de_arte = obra_de_arte
        self.lance_incial = lance_incial
        self.data_encerramento = data_encerramento
        self.termino = termino

    def get_id(self):
        return self.id
    
    def get_imagem(self):
        return self.imagem

    def get_local(self):
        return self.local
    
    def get_lance_incial(self):
        return self.lance_incial
    
    def get_data_encerramento(self):
        return self.data_encerramento
