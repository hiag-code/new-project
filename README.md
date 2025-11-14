# Sistema de Gerenciamento de Campeonato CBJJ

Projeto simples para cadastro de atletas, escolas e categorias seguindo regras básicas da CBJJ.

## Como executar

1. Crie um ambiente virtual:
```
python -m venv venv
```

2. Ative o ambiente:
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

3. Execute o sistema:
```
python app/main.py
```

## Estrutura do projeto

```
app/        # Arquivo principal
dao/        # Regras e acesso ao banco
db/         # Configuração do banco SQLite
model/      # Classes do sistema
```

## Banco de dados

Usa SQLite (arquivo campeonato.db).
