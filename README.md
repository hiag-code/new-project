# 🥋 Sistema de Gerenciamento de Campeonato – CBJJ

Este projeto é um sistema completo para gerenciamento de campeonatos de Jiu-Jitsu seguindo normas da **CBJJ/IBJJF**, permitindo o cadastro de atletas, escolas, categorias e resultados de pódio.

---

## 📁 Estrutura do Projeto

```
campeonato/
│
├── app/
│   └── main.py            # Arquivo principal do sistema
│
├── dao/
│   └── sistema_cbjj.py    # Lógica de acesso ao banco e regras de categoria
│
├── db/
│   └── database.py        # Conexão e operações SQL
│
├── model/
│   └── models.py          # Classes: Atleta, Escola, Categoria, Podio
│
├── campeonato.db          # Banco de dados SQLite
└── run.py                 # Script de execução (opcional)
```

---

## 🚀 Como Executar o Projeto

### 1. Criar ambiente virtual
```bash
python -m venv venv
```

### 2. Ativar o ambiente

**Windows**
```bash
venv\Scripts\activate
```

**Linux/Mac**
```bash
source venv/bin/activate
```

### 3. Instalar dependências
```bash
pip install pysqlite3
```

### 4. Iniciar o sistema

Se utilizar o arquivo de execução:
```bash
python run.py
```

Ou diretamente:
```bash
python app/main.py
```

---

## ✔️ Funcionalidades

- Cadastro de atletas  
- Cadastro de escolas  
- Determinação automática de categorias  
- Registro de pódio  
- Lista completa de participantes  
- Banco de dados SQLite  
- Estrutura modular com DAO e Models  

---

## 🧩 Modelos (Model Layer)

- **Categoria** – Nome da categoria  
- **Escola** – Informações completas de academias  
- **Atleta** – Dados pessoais e esportivos  
- **Podio** – Armazena colocação e evento  

---

## 🗄️ Banco de Dados

O sistema utiliza um banco SQLite chamado **campeonato.db**.  
A conexão e criação automática das tabelas são gerenciadas por:

```
db/database.py
```

---

## 🧮 Classificação Segundo a CBJJ

O sistema segue as normas oficiais:

- Categorias por idade  
- Categorias por peso (masculino e feminino)  
- Juvenil, Adulto e Masters  

As regras podem ser expandidas facilmente editando:

```
dao/sistema_cbjj.py
```

---

## 📌 Melhorias Futuras

- Interface gráfica  
- Geração de PDF com resultados  
- Sistema de chaves de luta  
- Exportações CSV/Excel  
- API com FastAPI  

---

## 🤝 Contribuições

Pull Requests são bem-vindos.  
Sugestões podem ser enviadas via Issues.

---

## 📜 Licença

Este projeto é livre para uso pessoal, acadêmico ou esportivo.

---

## Projeto funciona melhor no CMD

