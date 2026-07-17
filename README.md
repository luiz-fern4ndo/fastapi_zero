# fastapi_zero

### Comentáiio do projeto vou adicionar mais tarde

## Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/) - Framework web
- [UV](https://docs.astral.sh/uv/) - Gerenciador de pacotes e ambiente virtual
- [Uvicorn](https://www.uvicorn.org/) - Servidor ASGI

## Pré requisito
 - Python 3.10+
 - UV (instalado globalmente)

 ## Instalação

 ### 1. Instale o UV (caso não tenha)

 ```bash
 # macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Ou via pip
pip install uv
```
### 2. Clone o repositório
```bash
git clone https://github.com/seu-usuario/fastapi_zero.git
cd fastapi_zero
```  

### 3. Inicialize o ambiente com UV
```bash
# Inicializa o projeto UV (cria pyproject.toml)
uv init

# Cria e ativa o ambiente virtual
uv venv

# Ative o ambiente virtual
# Linux/Mac:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate
```  

### 4. Instale as dependências
```bash
 # Instala as dependências do pyproject.toml
uv sync

# Ou instale manualmente
uv add fastapi uvicorn
```

## Executando o Projeto

### Modo Desenvolvimento
```bash
uv run uvicorn main:app --reload
```

Acesse: http://172.0.0.1:8000


### Documentação Interativa

    Swagger UI: http://172.0.0.1:8000/docs

    ReDoc: http://172.0.0.1:8000/redoc


### Modo Produção
```bash
uv run uvicorn main:app --host 0.0.0.0 --port 8000
```

## Estrutura do Projeto
```plaintext
.
├── main.py              # Ponto de entrada da aplicação
├── pyproject.toml       # Configuração do projeto e dependências
├── uv.lock             # Lockfile das dependências
└── .venv/              # Ambiente virtual
```

## Comando Úteis
```plaintext
Comando	               Descrição

uv add <pacote>	       Adiciona uma nova dependência
uv remove <pacote>	   Remove uma dependência
uv sync	               Sincroniza dependências com o lockfile
uv run <comando>	   Executa comando no ambiente virtual
uv tree	               Mostra árvore de dependências
```


### Contribuindo 
    Fork o projeto

    Crie uma branch (git checkout -b feature/nova-feature)

    Commit suas mudanças (git commit -m 'Adiciona nova feature')

    Push para a branch (git push origin feature/nova-feature)

    Abra um Pull Request


### Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.