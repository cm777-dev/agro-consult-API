# Agro-Consult API

Uma API de consultoria agrícola integrada que fornece recomendações personalizadas para produtores rurais, utilizando dados de múltiplas fontes.

[![RapidAPI](https://img.shields.io/badge/RapidAPI-Live-blue)](https://rapidapi.com/marketplace)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 🌾 Visão Geral

A API integra dados de várias fontes confiáveis:
- ClimAPI: Dados climáticos e previsão do tempo
- Agritec: Informações técnicas sobre culturas e manejo
- SATVeg: Dados de sensoriamento remoto e vegetação

## ✨ Funcionalidades

- 🌡️ Recomendações de plantio baseadas em dados climáticos e características do solo
- 🌦️ Previsão climática personalizada para regiões agrícolas
- 🛰️ Monitoramento de culturas via sensoriamento remoto
- ⚠️ Alertas de condições adversas
- 🌱 Sugestões de manejo baseadas em dados históricos e previsões

## 🛠️ Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/): Framework moderno para APIs em Python
- [Pandas](https://pandas.pydata.org/): Análise e manipulação de dados
- [SQLAlchemy](https://www.sqlalchemy.org/): ORM para banco de dados
- [Pydantic](https://pydantic-docs.helpmanual.io/): Validação de dados
- [PostgreSQL](https://www.postgresql.org/): Banco de dados relacional

## 🚀 Começando

### Pré-requisitos

- Python 3.8+
- PostgreSQL
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/[seu-usuario]/agro-consult-api.git
cd agro-consult-api
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

4. Execute a aplicação:
```bash
uvicorn app.main:app --reload
```

## 📚 Documentação da API

Após iniciar o servidor, acesse:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🔑 Uso via RapidAPI

Esta API está disponível na RapidAPI. Para usar:

1. Crie uma conta na [RapidAPI](https://rapidapi.com)
2. Subscreva à API Agro-Consult
3. Use a chave da API fornecida nos headers das requisições:
```bash
X-RapidAPI-Key: 'sua-chave-aqui'
X-RapidAPI-Host: 'agro-consult.p.rapidapi.com'
```

## 🤝 Contribuindo

1. Faça um Fork do projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📧 Contato

Para suporte ou dúvidas: support@agroconsult.com
