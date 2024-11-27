class Obra_de_arte:
    def __init__(self, id,  categoria_id , artista, titulo, imagem, data, descricao ):
        self.id = id
        self.titulo = titulo
        self.imagem = imagem
        self.data = data
        self.descricao = descricao
        self.categoria_id = categoria_id
        self.artista= artista

    def get_id(self):
        return self.id
    
    def get_titulo(self):
        return self.titulo

    def get_imagem(self):
        return self.imagem
    
    def get_data(self):
        return self.data
    
    def get_descricao(self):
        return self.descricao
    
    def get_categoria_id(self):
        return self.categoria_id
    
    def get_artista(self):
        return self.artista

