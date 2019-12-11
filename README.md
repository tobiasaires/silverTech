# Silver Tech Api

  

## Descrição

Um projeto para fazer o pedido de computadores, respeitando alguns critérios de montagem.

  
  

## Tecnologias Usadas

  

- Python

- Django

- Django Rest Framework

- Docker

- Sqlite

  

# Instalação

Primeiro você precisa clonar esse repositório:

  

> git clone https://github.com/tobiasaires/silverTech.git

E depois

> cd silverTech

Caso você possua o Docker e o Docker Composer configurado no seu computador, basta excutar o comando:
> docker-compose up -d --build

Ao término de build dos containers acessar:
> [http://localhost:8000/](http://localhost:8000/)

 Com o venv de sua preferência e ativada:
 >cd silverTech &&  pip install -r requirements.tx

Após a instalação rode as migrations e suba o servidor:
> python manage.py migrate
> python manage.py runserver

Acessar em: [http://localhost:8000/](http://localhost:8000/)

## Testes

### Docker
> docker exec -it silvertech python manage.py test

### venv
> python manage.py test

# Links

## Api

[http://silver-tech.herokuapp.com/api](http://silver-tech.herokuapp.com/api)

## Docs

[http://silver-tech.herokuapp.com/swagger-docs](http://silver-tech.herokuapp.com/swagger-docs)
