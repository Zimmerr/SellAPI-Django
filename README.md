# Descrição

Uma API REST simples feita em Django

## Como usar localmente

```
git clone https://github.com/Zimmerr/SellAPI-Django
cd SellAPI-Django
pipenv shell
pipenv sync
cd SellAPI
python manage.py runserver
```

O servidor subirá na porta 8000 da sua máquina.

### Como usar o PostgreSQL

Caso queira, é possivel trocar o banco de dados utilizado para o Postgres. Para fazer isso são necessários alguns passos:
+ Vá até a pasta SellAPI
+ Preencha o arquivo `env` com os dados necessários e renomeie-o para `.env`
+ Apague/comente a variável DATABASES no arquivo `settings.py`, e descomente a outra versão dessa mesma váriavel, deixando assim:
  + ```
    # Database
    # https://docs.djangoproject.com/en/3.1/ref/settings/#databases

    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME': BASE_DIR / 'db.sqlite3',
    #     }
    # }

    DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': env('DATABASE_NAME'),
          'USER': env('DATABASE_USER'),
          'PASSWORD': env('DATABASE_PASSWORD'),
          'HOST': env('DATABASE_HOST'),
          'PORT': env('DATABASE_PORT'),
      }
    }
    ```
+ Se as variáveis de ambiente foram preenchidas corretamente, a aplicação deverá rodar normalmente num banco de dados PostgreSQL. Caso queira reverter, apenas inverta a variável DATABASES que está comentada

## Métodos

+ GET `/api/vendedores` - Retorna todos os vendedores
+ GET `/api/vendedores/:vendedor_id` - Retorna o vendedor com o ID especificado
+ POST `/api/vendedores` - Cria um vendedor, requer um payload em json com os dados do vendedor
+ PUT `/api/vendedores/:vendedor_id` - Atualiza o vendedor com o ID especificado, requer um payload em json com os dados do vendedor
+ DELETE `/api/vendedores/:vendedor_id` - Deleta o vendedor com o ID especificado
