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

O servidor subirá na porta 8000 da sua máquina

## Métodos

+ GET `/api/vendedores` - Retorna todos os vendedores
+ GET `/api/vendedores/:vendedor_id` - Retorna o vendedor com o ID especificado
+ POST `/api/vendedores` - Cria um vendedor, requer um payload em json com os dados do vendedor
+ PUT `/api/vendedores/:vendedor_id` - Atualiza o vendedor com o ID especificado, requer um payload em json com os dados do vendedor
+ DELETE `/api/vendedores/:vendedor_id` - Deleta o vendedor com o ID especificado
