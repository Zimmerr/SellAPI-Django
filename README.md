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
+ Apague/comente a variável DATABASES no arquivo `settings.py`, e descomente o seguinte bloco de código:
  + ```
    if 'test' in sys.argv:
      DATABASES = db_sqlite
    else:
      DATABASES = db_postgres
    ```
+ Se as variáveis de ambiente foram preenchidas corretamente, a aplicação deverá rodar normalmente num banco de dados PostgreSQL. Caso queira reverter, apenas inverta a variável DATABASES que está comentada

## Métodos

+ GET `/api/vendedores` - Retorna todos os vendedores
+ GET `/api/vendedores/:vendedor_id` - Retorna o vendedor com o ID especificado
+ POST `/api/vendedores` - Cria um vendedor, requer um payload em json com os dados do vendedor
+ PUT `/api/vendedores/:vendedor_id` - Atualiza o vendedor com o ID especificado, requer um payload em json com os dados do vendedor
+ DELETE `/api/vendedores/:vendedor_id` - Deleta o vendedor com o ID especificado
