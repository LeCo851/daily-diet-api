# Daily Diet API

API RESTful desenvolvida em Flask para o controle de dieta diária. Permite o cadastro de usuários e o gerenciamento completo de suas refeições.

## 🚀 Funcionalidades

A API é dividida em dois módulos principais e os dados são protegidos por usuário (um usuário só pode ver e alterar suas próprias refeições).

### Autenticação de Usuários (`/auth`)
*   **Cadastro (`POST /auth/register`)**: Cria um novo usuário informando `username`, `email` e `password`. Possui validação para evitar e-mails e nomes de usuário duplicados.
*   **Login (`POST /auth/login`)**: Autentica o usuário validando o e-mail e a senha criptografada (hash), iniciando uma sessão mantida via cookies no navegador (`Flask-Login`).
*   **Logout (`POST /auth/logout`)**: Encerra de forma segura a sessão ativa do usuário atual.

### Gerenciamento de Refeições (`/meals`)
*Todos os endpoints abaixo exigem que o usuário esteja autenticado (sessão ativa).*

*   **Criar Refeição (`POST /meals/`)**: Adiciona uma nova refeição. Requer `name`, `description` e se está dentro da dieta (`is_on_diet`). Opcionalmente recebe a data/hora (`date_time`), caso não enviada, utilizará o momento atual.
*   **Listar Refeições (`GET /meals/`)**: Retorna uma lista com todas as refeições cadastradas pertencentes ao usuário logado.
*   **Detalhar Refeição (`GET /meals/<id>`)**: Busca os detalhes de uma refeição específica pelo seu ID.
*   **Atualizar Refeição (`PUT /meals/<id>`)**: Atualiza todos os dados de uma refeição existente.
*   **Deletar Refeição (`DELETE /meals/<id>`)**: Remove permanentemente uma refeição do sistema.

### Documentação
*   **Swagger UI (`/apidocs/`)**: A API conta com uma documentação interativa gerada dinamicamente utilizando a biblioteca `Flasgger`.

## 🛠️ Tecnologias Utilizadas

*   **Python 3**
*   **Flask**: Micro-framework web utilizado para construir a API.
*   **Flask-SQLAlchemy**: ORM para comunicação, abstração e modelagem do banco de dados.
*   **Flask-Login**: Gerenciamento de sessões de autenticação do usuário.
*   **Flask-Bcrypt**: Geração de hashes seguros e verificação de senhas.
*   **Marshmallow**: Validação de schemas e serialização/desserialização de dados em JSON.
*   **Flasgger**: Integração do Swagger UI ao Flask a partir de arquivos `.yml`.
*   **Python-dotenv**: Carregamento seguro de variáveis de ambiente.

## ⚙️ Como Executar o Projeto Localmente

Siga os passos abaixo para configurar e rodar o projeto no seu ambiente:

### Pré-requisitos
*   Python 3.x instalado.
*   Gerenciador de pacotes `pip`.

### Passos para Instalação

1.  **Clone o repositório** (se estiver usando git) ou abra a pasta do projeto:
    ```bash
    cd daily-diet-api
    ```

2.  **Crie e ative um ambiente virtual** (recomendado para isolar as dependências):
    ```bash
    # No Windows
    python -m venv venv
    venv\Scripts\activate

    # No Linux/macOS
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências** necessárias:
    *(Nota: Se houver um `requirements.txt`, execute `pip install -r requirements.txt`. Caso contrário, instale manualmente os pacotes principais)*:
    ```bash
    pip install Flask Flask-SQLAlchemy Flask-Login Flask-Bcrypt marshmallow flasgger python-dotenv
    ```

4.  **Configure as variáveis de ambiente**:
    Na raiz do projeto, crie um arquivo chamado `.env` contendo as configurações vitais da aplicação:
    ```env
    SECRET_KEY=sua_chave_secreta_para_sessao_e_cookies
    DATABASE_URL=sqlite:///database.db  # Use SQLite para desenvolvimento local fácil, ou a URL do seu banco PostgreSQL
    ```

5.  **Inicie a aplicação**:
    ```bash
    python run.py
    ```
    > **Dica**: As tabelas do banco de dados serão criadas automaticamente na primeira vez que o servidor for inicializado (graças ao `db.create_all()` no `__init__.py`).

6.  **Acesse no Navegador/Insomnia/Postman**:
    *   A API estará rodando em: `http://127.0.0.1:5000/`
    *   Para ver a documentação interativa, acesse: `http://127.0.0.1:5000/apidocs/`