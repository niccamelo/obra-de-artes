class Lance:
    def __init__(self, id, usuario, valor, comentario, lance_inicial, data, obra_de_arte, ):
        self.id = id
        self.usuario = usuario
        self.valor = valor
        self.comentario = comentario
        self.lance_inicial = lance_inicial
        self.data = data
        self.obra_de_arte = obra_de_arte

    def get_id(self):
        return self.id
        
    def get_usuario(self):
        return self.usuario

    def get_valor(self):
        return self.valor
    
    def get_data(self):
        return self.data
    
    def get_obra_de_arte(self):
        return self.get_obra_de_arte
    
    def get_lance_inicial(self):
        return self.lance_inicial