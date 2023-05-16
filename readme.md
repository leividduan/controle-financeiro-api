# Controle financeiro

## Dependências

Para rodar o projeto é necessário instalar as seguintes dependências.

- pip install fastapi
- pip install uvicorn
- pip install sqlalchemy
- pip install mysqlclient
- pip install cryptography
- pip install bcrypt
- pip install PyJWT python-decouple

Além disso precisa ajustar o caminho do banco de dados dentro do arquivo database.py e adicionar um arquivo .env na raiz do projeto. Dentro do arquivo .env você precisa por uma chave aleatória e um tipo de algoritmo de criptografia. Ex:

- secret=<SUA CHAVE SECRETA>
- algorithm=HS256

## Comandos

- uvicorn main:app --reload
