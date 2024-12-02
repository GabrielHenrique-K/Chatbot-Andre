# Assistente Geek

O **Assistente Geek** é um chatbot interativo criado para os amantes de animes, filmes, mangás e jogos. Ele permite explorar recomendações, sinopses, curiosidades e muito mais sobre o universo da cultura pop. Além disso, é possível cadastrar e consultar informações de usuários.

## Funcionalidades Principais

### Requisitos
Para rodar o projeto, siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Baixe também os recursos necessários:
   ```python
   nltk.download('punkt')
   nltk.download('rslp')
   ```

4. Execute o arquivo principal:
   ```bash
   python main.py
   ```

### Funções Principais

1. **Cadastro de Usuários**:
   - Permite registrar nome e listas de favoritos (animes, filmes, mangás e jogos).

2. **Consulta de Usuários**:
   - Exibe informações cadastradas de um usuário específico.

3. **Recomendações**:
   - Sugere animes, filmes e mangás com base em categorias ou gêneros.

4. **Sinopses**:
   - Fornece descrições de animes ou filmes informados.

5. **Curiosidades e Novidades**:
   - Descubra fatos interessantes e as últimas notícias do universo geek.

6. **Dicas de Jogos**:
   - Dicas específicas para jogos populares.

7. **Eventos**:
   - Informa sobre convenções e competições relevantes.

### Interação

O chatbot é iniciado com o comando:
```python
iniciar_chatbot()
```

Para sair, utilize os comandos:
- `sair`

### Estrutura de Dados

- **`dados_usuarios`**: Contém informações sobre os usuários em um DataFrame do Pandas.
- **`chatbot_dados`**: Dicionário que armazena as respostas padrão e informações para cada categoria (animes, filmes, jogos, etc.).

### Processamento de Texto

Utiliza o `nltk` para:
- Tokenização: Separar o texto em palavras.
- Stemização: Reduzir palavras à sua raiz para melhor identificação de intenções.

## Exemplo de Uso

1. Cadastro de um novo usuário:
   ```text
   Por favor, insira seu nome: João
   Digite seus animes favoritos separados por vírgula: Naruto, One Piece
   Digite seus filmes favoritos separados por vírgula: Matrix, Inception
   Digite seus mangás favoritos separados por vírgula: Death Note, Berserk
   Digite seus jogos favoritos separados por vírgula: Zelda, God of War
   Cadastro realizado com sucesso!
   ```

2. Consultar dados de um usuário:
   ```text
   Digite o nome do usuário que deseja consultar: João
   Nome: João
   Animes Favoritos: Naruto, One Piece
   Filmes Favoritos: Matrix, Inception
   Mangás Favoritos: Death Note, Berserk
   Jogos Favoritos: Zelda, God of War
   ```

3. Solicitar recomendações:
   ```text
   Você: Recomendção de animes
   Recomendo os seguintes animes:
   - "Fullmetal Alchemist: Brotherhood": Uma jornada épica de dois irmãos em busca da Pedra Filosofal.
   - "Attack on Titan": A luta da humanidade contra titãs devoradores.
   - "Your Name": Uma história emocionante sobre destino e amor.
   - "Demon Slayer": Tanjiro embarca em uma missão para salvar sua irmã e derrotar demônios poderosos.
   ```


