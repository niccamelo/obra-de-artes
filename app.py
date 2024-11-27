from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
from artista import Artista
from categoria import Categoria
from exibicao import Exibicao
from lance import Lance
from leilao import Leilao 
from obra_de_arte import Obra_de_arte
from datetime import datetime

categoria = Categoria(1, "Quadros")
categoria2 = Categoria(2, "Esculturas")
categoria_list = [categoria, categoria2]

leonardo_20 = Artista(1, "Leonardo da Vinci", "leo.jpg", "Leonardo da Vinci nasceu em Anchiano, uma pequena aldeia toscana perto de Vinci e próxima a Florença, na Itália, no dia 15 de abril de 1452.")
van_gogh =  Artista(2, "Vincent van Gogh", "van.jpg", "Vincent Willem van Gogh (holandês; Zundert, 30 de março de 1853 Auvers-sur-Oise, 29 de julho de 1890) foi um pintor pós-impressionista neerlandês. Considerado uma das figuras mais famosas e influentes da história da arte ocidental, criou mais de dois mil trabalhos ao longo de pouco mais de uma década, incluindo 860 pinturas a óleo, grande parte das quais, concluídas nos seus últimos dois anos de vida.")
sandro = Artista(3, "Sandro Botticelli", "sandro.webp", "Sandro Botticelli (1445-1510) foi um pintor italiano, considerado um dos maiores pintores do Renascimento Artístico na Itália. Entre suas obras estão: “O Nascimento de Vênus”, A Tentação de Cristo e “A Adoração dos Magos")
auguste =  Artista(4, "Auguste Rodin", "auguste.webp", "Auguste Rodin (1840-1917) foi um escultor francês. 'O Pensador', 'O Beijo', 'A Porta do Inferno', são algumas de suas famosas esculturas. Foi um dos artistas mais influentes do século XX.")
thut = Artista(5, "Thutmose", "tut.jpg", "Tutmés I (às vezes lido como Tutmés ou Tutmés I , Thothmes em obras de história mais antigas em grego latinizado; significando    Thoth nasce') foi o terceiro faraó da 18ª Dinastia do Egito .")
michelangelo = Artista(6, "Michelangelo Buonarroti", "michel.webp", "Michelangelo foi um artista italiano, considerado um dos grandes representantes do Renascimento durante o século XVI. Ao longo de sua vida, atuou como escultor, pintor, arquiteto e ainda foi poeta amador, mas a grande paixão de Michelangelo foi mesmo a escultura, por meio da qual parte de seus principais trabalhos foram realizados.")

artista_list = [ leonardo_20, van_gogh, sandro, auguste, thut, michelangelo ]

obra_de_arte_list = [
    Obra_de_arte(1, 1, leonardo_20, "Mona Lisa", "mona-lisa.jpg", 1503, "Este é um dos quadros mais famoso, comentado, reproduzido e valioso da história da arte! Mona Lisa é criação de Leonardo da Vinci, considerado um dos artistas mais completos e conhecidos de toda a humanidade."),
    Obra_de_arte(2, 1, leonardo_20, "Homem Vitruano", "homemvitru.jpg", 1500, "Um desenho encontrado em um dos cadernos do artista. São duas figuras masculinas sobrepostas, com braços e pernas separadas, dentro de um quadrado e um círculo. A obra é baseada em um estudo de proporções de Vitruvius Pollio, um famoso arquiteto da época."),
    Obra_de_arte(3, 1, van_gogh, "Os Girassóis ", "girassois.webp", 1888, "Os Girassóis, do pintor holandês Vincent Van Gogh (1853-1890), são uma série de pinturas icônicas que transmitem a paixão e a visão de mundo do artista. Com cores vibrantes e pinceladas enérgicas, Van Gogh busca capturar a essência da vida na beleza efêmera de seus girassóis."),
    Obra_de_arte(4, 1, sandro, "O Nascimento de Vênus", "nascimento.webp", 1483, "Obra de Sandro Botticelli, O Nascimento de Vênus também é tido como uma das pinturas mais reproduzidas na cultura popular, seja no cinema, em propagandas, na literatura, na música, entre outras manifestações contemporâneas."),
    Obra_de_arte(5, 2, auguste, "O Pensador", "o pensador.webp", 1880, "Essa obra se tornou um símbolo duradouro da busca pelo conhecimento, conquistando um lugar especial no coração da arte e no imaginário coletivo"),
    Obra_de_arte(6, 2, thut, "Busto de Nefertiti", "busto-nefertiti.jpg", 1345, "Em Berlim, no Neues Museum, encontra-se um dos retratos mais incríveis de Nefertiti, a Grande Esposa Real do faraó egípcio Akhenaton. O busto de calcário pintado foi encontrado na oficina de um artista chamado Thutmose. Por muitos anos, esse retrato foi considerado um símbolo de beleza feminina ideal."),
    Obra_de_arte(7, 2, michelangelo, "David", "david.jpg", 1501, "O esplendor diante dos seus olhos! Provavelmente a mais famosa de todas as esculturas famosas. Essa é a melhor definição sobre a escultura de David, feita pelo mestre Michelangelo. Com 4,10 metros de altura e 5 toneladas, a obra-prima, que fica na Galleria dell’Accademia em Florença, é um dos símbolos do Renascimento que você precisa conhecer durante sua viagem. Simplesmente impressionante!")
]


exibicao_list = [
     Exibicao(1, "Quadros", "São Paulo", "12/12/2024", "12/01/2025", 1),
     Exibicao(2, "Estatuas", "São Paulo", "20/12/2024", "11/02/2025", 2),
]


leiloes = [
    {
        "id": 1,
        "obra_id": 1,  
        "lance_inicial": 500000.00,
        "data_inicio": datetime(2024, 10, 1, 10, 0),
        "data_fim": datetime(2024, 10, 7, 20, 0),
        "obra": obra_de_arte_list[1],  
    },
    {
        "id": 2,
        "obra_id": 2,
        "lance_inicial": 1000000.00,
        "data_inicio": datetime(2024, 10, 5, 9, 0),
        "data_fim": datetime(2024, 10, 12, 18, 0),
        "obra": obra_de_arte_list[2],
    },
]


lances = {
    1: [
        {"id": 1, "usuario": "Carlos", "valor": 510000.00, "comentario": "Lance inicial", "data": datetime(2024, 10, 1, 11, 0)},
        {"id": 2,"usuario": "Maria", "valor": 520000.00, "comentario": "Lance interessante", "data": datetime(2024, 10, 1, 12, 30)},
    ],
    2: [
        {"id": 1, "usuario": "João", "valor": 1050000.00, "comentario": "Excelente obra!", "data": datetime(2024, 10, 5, 10, 0)},
    ],
}

@app.route('/')
def home():
    datas_obras = [obra for obra in obra_de_arte_list if obra.get_categoria_id() == 1 ][:3]
    datas_obras2 = [obra for obra in obra_de_arte_list if obra.get_categoria_id() == 2 ][:3]

    artistas = artista_list[:4]
    for obra_de_arte in obra_de_arte_list:
        for artista in artista_list:
            return render_template("index.html", obra_de_arte_list = obra_de_arte_list, obra_de_arte=obra_de_arte, datas_obras = datas_obras, datas_obras2 = datas_obras2, artista_list = artista_list, artistas = artistas )
    
@app.route("/artista/<int:id>")
def artista(id):
    for artista in artista_list:
            if artista.get_id() == id:
                obras_do_artista = []
                for obra in obra_de_arte_list:
                    if obra.get_artista().get_id() == artista.get_id():
                        obras_do_artista.append(obra)
                return render_template("artista.html", artista=artista, obras_do_artista = obras_do_artista)    

@app.route("/obra_de_arte/<int:id>")
def obra_de_arte(id):
    obra = next((obra for obra in obra_de_arte_list if obra.get_id() == id), None) 
    categoria_obra = next((categoria for categoria in categoria_list if categoria.get_id() == obra.get_categoria_id()), None)
    leilao = next((l for l in leiloes if l["id"] == id), None)
    
    if request.method == 'POST':
        usuario = request.form['usuario']
        valor = float(request.form['valor'])
        comentario = request.form['comentario']
        data = datetime.now()

        lances[id].append({"usuario": usuario, "valor": valor, "comentario": comentario, "data": data})

        return redirect(url_for('lance_detail', id=id))

    comentarios_lances = lances.get(id, [])
    for obra_de_arte in obra_de_arte_list:
            if obra_de_arte.get_id() == id:    
                 return render_template("d_obra.html", leilao=leilao, comentarios_lances=comentarios_lances, obra_de_arte_list = obra_de_arte_list,  obra_de_arte=obra, categoria_obra=categoria_obra)    

@app.route("/exibicao/<int:id>")
def exibicao_detail(id):
    exibi_obras = [obra for obra in obra_de_arte_list if obra.get_categoria_id() == 1  ]
    for exibicao in exibicao_list:
            if exibicao.get_id() == id:
                for obra_de_arte in obra_de_arte_list:
                     if obra_de_arte.get_id() == id:
                        return render_template("exibicao_detail.html", exibi_obras = exibi_obras, obra_de_arte_list = obra_de_arte_list, exibicao = exibicao, obra_de_arte=obra_de_arte) 

@app.route('/leilao')
def leilao():
    return render_template('leilao.html', leiloes=leiloes)

@app.route('/leilao/<int:id>')
def leilao_detail(id):
    leilao = next((l for l in leiloes if l["id"] == id), None)
    for lance in lances:
            if not leilao:
                return "Leilão não encontrado", 404
    comentarios_lances = lances.get(id, [])
    return render_template('leilao_detail.html', leilao=leilao, comentarios_lances=comentarios_lances, lance=lance)

@app.route('/exibicao/')
def exibicao():
         return render_template("exibicao.html", exibicao = exibicao, exibicao_list = exibicao_list, obra_de_arte=obra_de_arte)
        


@app.route('/lance/<int:id>', methods=['GET', 'POST'])
def lance_detail(id):
    leilao = next((l for l in leiloes if l["id"] == id), None)
    if not leilao:
        return "Leilão não encontrado", 404
    
    if request.method == 'POST':
        usuario = request.form['usuario']
        valor = float(request.form['valor'])
        comentario = request.form['comentario']
        data = datetime.now()

        # Adiciona o novo lance/comentário
        lances[id].append({"usuario": usuario, "valor": valor, "comentario": comentario, "data": data})

        return redirect(url_for('lance_detail', id=id))

    comentarios_lances = lances.get(id, [])
    return render_template('lance_detail.html', leilao=leilao, comentarios_lances=comentarios_lances)