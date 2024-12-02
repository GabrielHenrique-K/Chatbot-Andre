import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import RSLPStemmer
import pandas as pd


nltk.download('punkt')
nltk.download('rslp')


dados_usuarios = pd.DataFrame(columns=['Nome', 'Lista Animes', 'Lista Filmes', 'Lista Mangas', 'Lista Jogos'])


chatbot_dados = {
    'animes': {
        'recomendacoes de animes': (
            'Recomendo os seguintes animes:\n'
            '- "Fullmetal Alchemist: Brotherhood": Uma jornada épica de dois irmãos em busca da Pedra Filosofal.\n'
            '- "Attack on Titan": A luta da humanidade contra titãs devoradores.\n'
            '- "Your Name": Uma história emocionante sobre destino e amor.\n'
            '- "Demon Slayer": Tanjiro embarca em uma missão para salvar sua irmã e derrotar demônios poderosos.'
        ),
        'sinopses de animes': 'Claro! Por favor, indique o título do anime que deseja a sinopse.',
        'personagens de animes': (
            'Personagens populares incluem:\n'
            '- Naruto Uzumaki ("Naruto"): Um ninja determinado a se tornar Hokage.\n'
            '- Monkey D. Luffy ("One Piece"): Um pirata aspirante a Rei dos Piratas.\n'
            '- Goku ("Dragon Ball"): Um guerreiro Saiyajin em busca de poder e proteção da Terra.\n'
            '- Mikasa Ackerman ("Attack on Titan"): Uma soldado habilidosa e protetora de Eren Yeager.'
        ),
        'novidades sobre animes': (
            'Últimas notícias:\n'
            '- Nova temporada de "Bleach" anunciada após anos de espera.\n'
            '- "Chainsaw Man" recebe adaptação em anime pelo estúdio MAPPA.\n'
            '- "Jujutsu Kaisen" confirma filme prequela baseado no Volume 0.'
        ),
        'animes por genero': 'Por favor, informe o gênero que você deseja recomendações.',
        'curiosidades de animes': (
            'Você sabia?\n'
            '- "Spirited Away" é o único filme de anime a ganhar um Oscar.\n'
            '- "One Piece" é o mangá mais vendido de todos os tempos.\n'
            '- "Naruto" foi originalmente planejado para ser sobre magia, não ninjas.'
        )
    },
    'filmes': {
        'recomendacoes de filmes': (
            'Sugiro os seguintes filmes:\n'
            '- "A Origem": Um thriller de ficção científica sobre invasão de sonhos.\n'
            '- "Interestelar": Uma exploração espacial em busca de um novo lar para a humanidade.\n'
            '- "Parasita": Uma crítica social sobre desigualdade e classe.\n'
            '- "Spirited Away": Uma aventura fantástica no mundo dos espíritos.'
        ),
        'sinopses de filmes': 'Claro! Por favor, indique o título do filme que deseja a sinopse.',
        'personagens de filmes': (
            'Personagens icônicos incluem:\n'
            '- Harry Potter ("Harry Potter"): O menino que sobreviveu e enfrenta o mal.\n'
            '- Tony Stark ("Homem de Ferro"): Um gênio bilionário que se torna um herói tecnológico.\n'
            '- Ellen Ripley ("Alien"): Uma tenente que enfrenta uma criatura extraterrestre mortal.\n'
            '- Frodo Bolseiro ("O Senhor dos Anéis"): Um hobbit em uma missão para destruir o Anel.'
        ),
        'novidades sobre filmes': (
            'Últimas notícias:\n'
            '- "Duna" recebe aclamação crítica e sucesso de bilheteria.\n'
            '- "Avatar 2" promete revolucionar efeitos especiais novamente.\n'
            '- Marvel anuncia nova fase de filmes com personagens inéditos.'
        ),
        'filmes por genero': 'Por favor, informe o gênero que você deseja recomendações.',
        'curiosidades de filmes': (
            'Você sabia?\n'
            '- "Titanic" foi o primeiro filme a atingir 1 bilhão de dólares em bilheteria.\n'
            '- "O Mágico de Oz" inicialmente não foi um sucesso comercial.\n'
            '- "Psicose" foi o primeiro filme a mostrar um vaso sanitário sendo descarregado.'
        )
    },
    'estudios': {
        'informacoes sobre estudios': (
            'Estúdios renomados:\n'
            '- Studio Ghibli: Conhecido por animações como "Meu Amigo Totoro".\n'
            '- Pixar: Pioneira em animação por computador com filmes como "Toy Story".\n'
            '- Marvel Studios: Revolucionou o gênero de super-heróis com seu universo cinematográfico.\n'
            '- Warner Bros.: Um dos estúdios mais antigos, responsável por "Harry Potter" e "Matrix".'
        ),
        'principais obras': 'Por favor, especifique o estúdio que deseja conhecer as obras.',
        'historias dos estudios': 'Informe o estúdio sobre o qual você deseja saber mais.',
        'proximos lancamentos': (
            'Próximos lançamentos incluem:\n'
            '- "Spider-Man: No Way Home" pela Marvel Studios.\n'
            '- "The Batman" pela DC Films.\n'
            '- Novos projetos de animação pelo Studio Ghibli.'
        ),
        'diretores famosos': (
            'Diretores notáveis:\n'
            '- Hayao Miyazaki: Fundador do Studio Ghibli.\n'
            '- Christopher Nolan: Conhecido por filmes como "A Origem" e "Interestelar".\n'
            '- Steven Spielberg: Diretor de clássicos como "E.T." e "Jurassic Park".\n'
            '- Quentin Tarantino: Reconhecido por seu estilo único em filmes como "Pulp Fiction".'
        ),
        'tecnologias utilizadas': (
            'Inovações tecnológicas:\n'
            '- Pixar utiliza o RenderMan para renderização de gráficos.\n'
            '- Weta Digital, da Nova Zelândia, é líder em efeitos visuais, responsável por "Avatar".\n'
            '- O uso de captura de movimento evoluiu com filmes como "Planeta dos Macacos".'
        )
    },
    'eventos': {
        'eventos de anime e filme': (
            'Principais eventos:\n'
            '- Comic Con: Maior convenção de cultura pop do mundo.\n'
            '- Anime Expo: Evento dedicado a animes e mangás nos EUA.\n'
            '- Tokyo Game Show: Focado em jogos, mas com forte presença de animes.'
        ),
        'datas de convencoes': (
            'Próximas datas:\n'
            '- Comic Con: 22 a 25 de julho.\n'
            '- Anime Friends: 8 a 10 de julho.\n'
            '- Brasil Game Show: 6 a 12 de outubro.'
        ),
        'ingressos e inscricoes': (
            'Informações sobre ingressos:\n'
            '- Comic Con: Disponíveis no site oficial, com opções de pacotes VIP.\n'
            '- Anime Friends: Ingressos promocionais para estudantes e grupos.\n'
            '- BGS: Oferece meia-entrada mediante doação de 1kg de alimento.'
        ),
        'resumos de eventos passados': (
            'Destaques recentes:\n'
            '- Lançamento do trailer de "Matrix Resurrections" na Comic Con.\n'
            '- Painel exclusivo de "The Witcher" com participação do elenco.\n'
            '- Anúncio de novos jogos na E3, incluindo "Elden Ring".'
        ),
        'palestras e workshops': (
            'Atividades disponíveis:\n'
            '- Workshops de desenho com mangakás convidados.\n'
            '- Palestras sobre produção cinematográfica com diretores renomados.\n'
            '- Sessões de perguntas e respostas com atores e dubladores.'
        ),
        'competicoes de cosplay': (
            'Informações sobre concursos:\n'
            '- Premiações para melhores cosplays individuais e em grupo.\n'
            '- Júri composto por especialistas e convidados internacionais.\n'
            '- Inscrições abertas no site oficial do evento.'
        )
    },
    'mangas': {
        'recomendacoes de mangas': (
            'Mangás que você pode gostar:\n'
            '- "Berserk": Uma história sombria de fantasia e sobrevivência.\n'
            '- "Death Note": Um suspense psicológico envolvendo um caderno mortal.\n'
            '- "Vagabond": A jornada de Miyamoto Musashi em busca de ser o espadachim supremo.'
        ),
        'novidades sobre mangas': (
            'Últimas notícias:\n'
            '- "One Piece" atinge a marca de 100 volumes publicados.\n'
            '- Novo mangá de "Bleach" é anunciado pelo autor Tite Kubo.\n'
            '- "Attack on Titan" chega ao fim após 11 anos de publicação.'
        ),
        'autores famosos': (
            'Mangakás notáveis:\n'
            '- Eiichiro Oda: Criador de "One Piece".\n'
            '- Akira Toriyama: Conhecido por "Dragon Ball".\n'
            '- Rumiko Takahashi: Autora de "InuYasha" e "Ranma ½".'
        ),
        'mangas por genero': 'Por favor, informe o gênero que você deseja recomendações.',
        'adaptacoes para anime': (
            'Mangás que ganharam anime:\n'
            '- "Jujutsu Kaisen": Adaptado em 2020 com grande sucesso.\n'
            '- "Demon Slayer": Sua adaptação impulsionou as vendas do mangá.\n'
            '- "The Promised Neverland": Um suspense emocionante.'
        ),
        'curiosidades de mangas': (
            'Você sabia?\n'
            '- "Astro Boy" é considerado o primeiro mangá moderno.\n'
            '- "Sazae-san" é o mangá mais longo da história, iniciado em 1946.\n'
            '- O mangá "Golgo 13" está em publicação contínua desde 1968.'
        )
    },
    'jogos': {
        'jogos baseados em animes': (
            'Jogos recomendados:\n'
            '- "Naruto Shippuden: Ultimate Ninja Storm": Lutas intensas com personagens da série.\n'
            '- "Dragon Ball FighterZ": Um jogo de luta com gráficos impressionantes.\n'
            '- "One Piece: Pirate Warriors": Aventura no mundo de One Piece.'
        ),
        'recomendacoes de jogos': (
            'Sugestões de jogos:\n'
            '- "The Legend of Zelda: Breath of the Wild": Uma jornada épica em mundo aberto.\n'
            '- "God of War": A história de Kratos na mitologia nórdica.\n'
            '- "The Witcher 3: Wild Hunt": Um RPG profundo com narrativa envolvente.'
        ),
        'novidades sobre jogos': (
            'Últimas notícias:\n'
            '- "Elden Ring" tem data de lançamento confirmada.\n'
            '- "Horizon Forbidden West" apresenta novos detalhes de gameplay.\n'
            '- "Final Fantasy XVI" está em desenvolvimento para PS5.'
        ),
        'personagens de jogos': (
            'Personagens marcantes:\n'
            '- Link ("The Legend of Zelda"): O herói silencioso de Hyrule.\n'
            '- Lara Croft ("Tomb Raider"): A icônica arqueóloga aventureira.\n'
            '- Geralt de Rivia ("The Witcher"): Um bruxo caçador de monstros.'
        ),
        'plataformas disponiveis': (
            'Jogos estão disponíveis em diversas plataformas:\n'
            '- PC\n- PlayStation 4 e 5\n- Xbox One e Series X/S\n- Nintendo Switch\n- Mobile (iOS e Android)'
        ),
        'dicas e truques': (
            'Posso fornecer dicas para jogos específicos. Por favor, informe o título do jogo que deseja ajuda.'
        )
    }
}


stemmer = RSLPStemmer()

def processar_texto(texto):
    """
    Tokeniza e aplica stemmização ao texto de entrada.

    Parâmetros:
    texto (str): Texto fornecido pelo usuário.

    Retorna:
    list: Lista de stems das palavras no texto.
    """
    tokens = word_tokenize(texto.lower(), language='portuguese')
    stems = [stemmer.stem(token) for token in tokens if token.isalnum()]
    return stems

def identificar_entidade_intencao(stems):
    """
    Identifica a entidade e a intenção com base nos stems fornecidos.

    Parâmetros:
    stems (list): Lista de stems das palavras do usuário.

    Retorna:
    tuple: Entidade e intenção correspondentes, ou (None, None) se não encontrar.
    """
    best_match = None
    max_matches = 0
    for entidade, intencoes in chatbot_dados.items():
        for intencao in intencoes.keys():
            intencao_tokens = word_tokenize(intencao.lower(), language='portuguese')
            intencao_stems = [stemmer.stem(token) for token in intencao_tokens if token.isalnum()]
            matches = set(stems).intersection(set(intencao_stems))
            if len(matches) > max_matches:
                max_matches = len(matches)
                best_match = (entidade, intencao)
    if best_match and max_matches > 0:
        return best_match
    else:
        return None, None

def cadastrar_usuario():
    """
    Realiza o cadastro do usuário, solicitando informações pessoais.
    """
    nome = input("Por favor, insira seu nome: ")
    lista_animes = input("Digite seus animes favoritos separados por vírgula: ")
    lista_filmes = input("Digite seus filmes favoritos separados por vírgula: ")
    lista_mangas = input("Digite seus mangás favoritos separados por vírgula: ")
    lista_jogos = input("Digite seus jogos favoritos separados por vírgula: ")
    global dados_usuarios
    novo_usuario = pd.DataFrame([{
        'Nome': nome,
        'Lista Animes': [anime.strip() for anime in lista_animes.split(',')],
        'Lista Filmes': [filme.strip() for filme in lista_filmes.split(',')],
        'Lista Mangas': [manga.strip() for manga in lista_mangas.split(',')],
        'Lista Jogos': [jogo.strip() for jogo in lista_jogos.split(',')]
    }])
    dados_usuarios = pd.concat([dados_usuarios, novo_usuario], ignore_index=True)
    print("\nCadastro realizado com sucesso!\n")

def consultar_dados_usuario(nome):
    """
    Consulta e exibe os dados cadastrados de um usuário.

    Parâmetros:
    nome (str): Nome do usuário a ser consultado.
    """
    usuario = dados_usuarios[dados_usuarios['Nome'] == nome]
    if not usuario.empty:
        print(f"\nNome: {usuario.iloc[0]['Nome']}")
        print(f"Animes Favoritos: {', '.join(usuario.iloc[0]['Lista Animes'])}")
        print(f"Filmes Favoritos: {', '.join(usuario.iloc[0]['Lista Filmes'])}")
        print(f"Mangás Favoritos: {', '.join(usuario.iloc[0]['Lista Mangas'])}")
        print(f"Jogos Favoritos: {', '.join(usuario.iloc[0]['Lista Jogos'])}\n")
    else:
        print("\nUsuário não encontrado.\n")

def fornecer_sinopse(entidade, titulo):
    """
    Fornece a sinopse de um anime ou filme específico.

    Parâmetros:
    entidade (str): 'animes' ou 'filmes'.
    titulo (str): Título do anime ou filme.
    """
    sinopses = {
        'animes': {
            'naruto': 'Naruto Uzumaki é um jovem ninja que busca reconhecimento e sonha em se tornar Hokage, o líder de sua vila.',
            'one piece': 'Monkey D. Luffy e sua tripulação de piratas procuram o tesouro supremo conhecido como One Piece para se tornarem o próximo Rei dos Piratas.',
            'attack on titan': 'A humanidade luta pela sobrevivência contra titãs devoradores em um mundo cercado por muralhas gigantes.',
            'death note': 'Light Yagami encontra um caderno que permite matar qualquer pessoa cujo nome seja escrito nele, iniciando um jogo de gato e rato com o detetive L.'
        },
        'filmes': {
            'inception': 'Um ladrão invade os sonhos das pessoas para roubar segredos corporativos, mas é desafiado a plantar uma ideia na mente de um alvo.',
            'parasite': 'Uma família pobre se infiltra na vida de uma família rica, resultando em consequências inesperadas e dramáticas.',
            'interestelar': 'Exploradores espaciais viajam através de um buraco de minhoca em busca de um novo lar para a humanidade.',
            'matrix': 'Um hacker descobre que o mundo real é uma simulação controlada por máquinas e junta-se à rebelião humana.'
        }
    }
    titulo_lower = titulo.lower()
    if titulo_lower in sinopses.get(entidade, {}):
        print(f"\nSinopse de {titulo.title()}:\n{sinopses[entidade][titulo_lower]}\n")
    else:
        print(f"\nDesculpe, não tenho a sinopse de '{titulo}'.\n")

def fornecer_recomendacoes_por_genero(entidade, genero):
    """
    Fornece recomendações de animes, filmes ou mangás por gênero.

    Parâmetros:
    entidade (str): 'animes', 'filmes' ou 'mangas'.
    genero (str): Gênero solicitado pelo usuário.
    """
    recomendacoes = {
        'animes': {
            'acao': ['Naruto', 'Bleach', 'One Punch Man'],
            'romance': ['Your Lie in April', 'Toradora!', 'Clannad'],
            'terror': ['Another', 'Parasyte', 'Tokyo Ghoul']
        },
        'filmes': {
            'acao': ['John Wick', 'Mad Max: Estrada da Fúria', 'Die Hard'],
            'drama': ['Forrest Gump', 'Clube da Luta', 'A Vida é Bela'],
            'ficcao cientifica': ['Blade Runner 2049', 'Ex Machina', 'A Chegada']
        },
        'mangas': {
            'aventura': ['One Piece', 'Fairy Tail', 'Made in Abyss'],
            'drama': ['Orange', 'Goodnight Punpun', 'Nana'],
            'esportes': ['Haikyuu!!', 'Slam Dunk', 'Kuroko no Basket']
        }
    }
    genero_lower = genero.lower()
    if genero_lower in recomendacoes.get(entidade, {}):
        lista = recomendacoes[entidade][genero_lower]
        print(f"\nRecomendações de {entidade} do gênero {genero.title()}:\n- " + "\n- ".join(lista) + "\n")
    else:
        print(f"\nDesculpe, não tenho recomendações para o gênero '{genero}' em {entidade}.\n")

def fornecer_dicas_jogos(titulo):
    """
    Fornece dicas e truques para um jogo específico.

    Parâmetros:
    titulo (str): Título do jogo.
    """
    dicas = {
        'the legend of zelda: breath of the wild': 'Explore todas as torres primeiro para desbloquear o mapa e cozinhe alimentos para aumentar seus atributos.',
        'god of war': 'Use diferentes combinações de runas para variar seus ataques e não se esqueça de explorar para encontrar itens escondidos.',
        'the witcher 3': 'Complete missões secundárias para ganhar experiência e melhorar suas habilidades, e esteja atento às escolhas que afetam a história.'
    }
    titulo_lower = titulo.lower()
    if titulo_lower in dicas:
        print(f"\nDicas para {titulo.title()}:\n{dicas[titulo_lower]}\n")
    else:
        print(f"\nDesculpe, não tenho dicas para '{titulo}'.\n")

def responder_usuario(texto):
    """
    Processa a entrada do usuário e fornece a resposta adequada.

    Parâmetros:
    texto (str): Texto fornecido pelo usuário.
    """
    stems = processar_texto(texto)
    if 'cadastr' in stems:
        cadastrar_usuario()
    elif 'consult' in stems:
        nome = input("Digite o nome do usuário que deseja consultar: ")
        consultar_dados_usuario(nome)
    else:
        entidade, intencao = identificar_entidade_intencao(stems)
        if entidade and intencao:
            if intencao in ['sinopses de animes', 'sinopses de filmes']:
                titulo = input("Por favor, indique o título que deseja a sinopse: ")
                fornecer_sinopse(entidade, titulo)
            elif intencao in ['animes por genero', 'filmes por genero', 'mangas por genero']:
                genero = input(f"Qual gênero de {entidade} você está interessado? ")
                fornecer_recomendacoes_por_genero(entidade, genero)
            elif intencao == 'dicas e truques':
                titulo = input("Para qual jogo você deseja dicas? ")
                fornecer_dicas_jogos(titulo)
            else:
                resposta = chatbot_dados[entidade][intencao]
                print(f"\n{resposta}\n")
        else:
            print("\nDesculpe, não entendi sua solicitação.\n")


def iniciar_chatbot():
    """
    Inicia o loop principal de interação com o usuário.
    """
    print("Olá! Sou o Assistente Otaku. Como posso ajudar?")
    while True:
        texto_usuario = input("Você: ")
        if texto_usuario.lower() in ['sair', 'exit', 'quit']:
            print("\nAté logo! Continue aproveitando seus animes e filmes favoritos!\n")
            break
        responder_usuario(texto_usuario)

iniciar_chatbot()
