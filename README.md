#  Blog API
<fig>
<img src="https://rockcontent.com/br/wp-content/uploads/sites/2/elementor/thumbs/modelo-de-projeto-p2he6clp7uhmwqd16ikv9jgz30a5liixoon908hej0.png" alt="Uma imagem relacionada ao projeto">
</fig>

## Inicialização
Para executar o projeto siga os seguintes passos:
 - crie um ambiente virtual Python. [Clique
   aqui](https://docs.python.org/3/library/venv.html) caso não saiba
   criar um. 
 - git clone;
 - `pip install -r requirements.txt`;
 - crie um arquivo .env e o edite como na sessão _Variáveis de ambiente_;
 - `python manage.py makemigrations`
 - `python manage.py migrate`;
 - `python manage.py runserver`;

## Variáveis de ambiente

    SECRET_KEY=
    DEBUG=
    DATABASE_NAME=
    DATABASE_USER=
    DATABASE_PASSWORD=
    DATABASE_HOST=
    DATABASE_PORT=

## Banco de dados
O banco de dados padrão é o MySQL. Caso você prefira PostgreSQL, [clique aqui](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-20-04).

##  API URLS

 - http://127.0.0.1:8000/api/list/
 - http://127.0.0.1:8000/users/api/users/
 - http://127.0.0.1:8000/users/api/users/id/	
 - http://127.0.0.1:8000/api/posts/
 - http://127.0.0.1:8000/api/posts/id/
 - http://127.0.0.1:8000/api/comments/
 - http://127.0.0.1:8000/api/comments/id/
