class Exibicao:
    def __init__(self, id, nome, local, data_inicio , data_fim, obra_de_arte):
        self.id = id
        self.nome = nome
        self.local = local
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.obra_de_arte = obra_de_arte
        
    def get_id(self):
        return self.id
    
    def get_nome(self):
        return self.nome

    def get_local(self):
        return self.local
    
    def get_data_inicio(self):
        return self.data_inicio
    
    def get_obra_de_arte(self):
        return self.obra_de_arte
    
    def get_data_fim(self):
        return self.data_fim