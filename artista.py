class Artista:
    def __init__(self, id, nome, foto, biografia ):
        self.id = id
        self.nome = nome
        self.foto = foto
        self.biografia = biografia
        
    def get_id(self):
        return self.id
    
    def get_nome(self):
        return self.nome
        
    def get_foto(self):
        return self.foto

    def get_biografia(self):
        return self.biografia
    