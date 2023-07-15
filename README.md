# CondoConta API 
___


<!-- TABLE OF CONTENTS -->

## Table of Contents
___
* [Tabela de Conteúdo](#table-of-contents)
* [Sobre o Projeto](#about-the-project)
  * [Feito com](#done-with)
* [Iniciando](#starting)
  * [Pré Requisitos](#prerequisites)
  * [Configure .env](#configure-env)
  * [Instalação](#installation)
  * [Rode o Projeto](#run-project)
* [Licença](#license)
* [Contato](#contact)
* [Documentação](#docs)


<!-- ABOUT THE PROJECT -->

## About the Project
___
_Este é um simples projeto django REST API que provê informações de extrato, saldo e conta bancaria de um banco._

## Done With
___
- [Django](https://www.djangoproject.com/) - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- [Django Rest Framework](https://www.django-rest-framework.org/) - Django REST framework is a powerful and flexible toolkit for building Web APIs.
- [Django Environ](https://github.com/joke2k/django-environ) - Django Environ allows you to use Twelve-factor methodology to configure your Django application with environment variables.
- [Docker](https://www.docker.com/) - Docker simplifies and accelerates your workflow, while giving developers the freedom to innovate with their choice of tools, application stacks, and deployment environments for each project.
- [Docker Compose](https://docs.docker.com/compose/) - Compose is a tool for defining and running multi-container Docker applications.

<!-- GETTING STARTED -->

## Iniciando
___
_Para o projeto rodar você precisa._

### Pré Requisitos
___
###### docker

- [Official docs](https://docs.docker.com/get-docker/)
- [How to install in Fedora](https://docs.docker.com/engine/install/fedora/)
- [How to install in MacOS](https://docs.docker.com/docker-for-mac/install/)
- [How to install in Windows](https://docs.docker.com/docker-for-windows/install/)

###### docker compose

- [How to install docker compose](https://docs.docker.com/compose/install/)


### Configure .env
___
```sh
$ docker-compose exec service cp core/env.template core/.env
```

_Preencha as informações necessárias do arquivo .env, por exemplo._

### Instalação
___
```sh
$ docker-compose up -d --build # (apenas primeira vez)
$ docker-compose exec service python3 manage.py migrate # (apenas primeira vez)
$ docker-compose exec service python3 manage.py createsuperuser # (apenas primeira vez)
```

### Rode o Projeto
___
```sh
$ docker-compose up -d 
```

<!-- LICENSE -->

## Licença
___
The MIT License (MIT)

Copyright (c) [2023] [Adson Rodrigues](https://github.com/adsonrodrigues)

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

<!-- CONTACT -->

## Contato
___

Adson Rodrigues - [Linkedin](https://www.linkedin.com/in/adsonr/)

## Documentação
__

Todos os endpoints podem ser encontrados em: http://localhost/docs/