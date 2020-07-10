# Backend da aplicação Store Manger

Uma API REST que fornece registro de usuário, autienticação, autorização e CRUD de produtos.

### Instalação
Após clonar o projeto, faça:
- Crie um amibiente virtual `Python 3.7.7`
- Instale as dependências via `pip install -r requirements.txt`
- Execute `python manage.py makamigrations` e `python manage.py migrate`
- Por fim, execute `python manage.py runserver`. A API será servida em http://localhost:8000

### Rotas
|Recurso          |Método|Path                             |
|-----------------|------|---------------------------------|
|Login            |POST  |`/api/v1/rest-auth/login/`       |
|Logout           |POST  |`/api/v1/rest-auth/login/`       |
|Registro         |POST  |`/api/v1/rest-auth/registration/`|
|Criar produto    |POST  |`/products/`                     |
|Listar produto   |GET   |`/products/`                     |
|Atualizar produto|PUT   |`/products/id/`                  |
|Deletar produto  |DELETE|`/products/id/`                  |
