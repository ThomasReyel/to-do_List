# To-Do List API

API para gerenciamento de tarefas desenvolvida com Django e Django Rest Framework.

## Tecnologias Utilizadas

- Python 3.12
- Django 6.0
- Django Rest Framework
- SQLite

## Instalação e Execução

### 1. Clone o repositório

```
git clone https://github.com/ThomasReyel/to-do_List.git
cd to-do_List
```

### 2. Instale dependências e crie o ambiente virtual (se necessário)
Linux/Mac
```
python -m venv venv
source venv/bin/activate
```
Windows
```
python -m venv venv
venv\Scripts\activate
```

Rest_Framework
```
pip install django djangorestframework
```

### 3. Execulte as migrações
```
python manage.py makemigrations
python manage.py migrate
```

### 4. Popule o banco de dados
```
python manage.py populate_tasks
```

### 5. Execute o servidor
```
python manage.py runserver
```

## Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | /task/ | Lista todas as tarefas com paginação (5 itens por página) |
| GET | /task/?search={termo} | Busca tarefas por título ou descrição |
| GET | /task/{id}/ | Visualiza os detalhes de uma tarefa específica |
| POST | /task/ | Cria uma nova tarefa |
| PUT | /task/{id}/ | Atualiza todos os campos de uma tarefa existente |
| PATCH | /task/{id}/ | Atualiza parcialmente uma tarefa existente |
| DELETE | /task/{id}/ | Remove uma tarefa do sistema |

## Exemplos de Requisições e Respostas

### 1. Listar todas as tarefas (GET)

**Requisição:**
```
GET http://localhost:8000/task/
```

**Resposta (200 OK):**
```json
{
    "count": 15,
    "next": "http://localhost:8000/task/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "Estudar Django",
            "description": "Completar o desafio da API",
            "deadline": "2024-12-31",
            "completion_date": null,
            "state": "nova"
        },
        {
            "id": 2,
            "title": "Fazer exercícios",
            "description": "Correr 5km no parque",
            "deadline": "2024-12-25",
            "completion_date": null,
            "state": "em_andamento"
        }
    ]
}
```

### 2. Buscar tarefas (GET com parâmetro search)

**Requisição:**
```
GET http://localhost:8000/task/?search=django
```

**Resposta (200 OK):**
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "Estudar Django",
            "description": "Completar o desafio da API",
            "deadline": "2024-12-31",
            "completion_date": null,
            "state": "nova"
        },
        {
            "id": 5,
            "title": "Praticar Django Rest Framework",
            "description": "Criar uma API completa",
            "deadline": "2024-12-28",
            "completion_date": null,
            "state": "em_andamento"
        }
    ]
}
```

### 3. Visualizar uma tarefa específica (GET)

**Requisição:**
```
GET http://localhost:8000/task/1/
```

**Resposta (200 OK):**
```json
{
    "id": 1,
    "title": "Estudar Django",
    "description": "Completar o desafio da API",
    "deadline": "2024-12-31",
    "completion_date": null,
    "state": "nova"
}
```

### 4. Criar uma nova tarefa (POST)

**Requisição:**
```
POST http://localhost:8000/task/
Content-Type: application/json
```

**Body:**
```json
{
    "title": "Ler documentação do DRF",
    "description": "Estudar serializers e viewsets",
    "deadline": "2024-12-30",
    "state": "nova"
}
```

**Resposta (201 Created):**
```json
{
    "id": 16,
    "title": "Ler documentação do DRF",
    "description": "Estudar serializers e viewsets",
    "deadline": "2024-12-30",
    "completion_date": null,
    "state": "nova"
}
```

### 5. Atualizar uma tarefa completamente (PUT)

**Requisição:**
```
PUT http://localhost:8000/task/1/
Content-Type: application/json
```

**Body:**
```json
{
    "title": "Estudar Django Avançado",
    "description": "Completar o desafio e enviar no prazo",
    "deadline": "2025-01-15",
    "completion_date": null,
    "state": "em_andamento"
}
```

**Resposta (200 OK):**
```json
{
    "id": 1,
    "title": "Estudar Django Avançado",
    "description": "Completar o desafio e enviar no prazo",
    "deadline": "2025-01-15",
    "completion_date": null,
    "state": "em_andamento"
}
```

### 6. Atualizar parcialmente uma tarefa (PATCH)

**Requisição:**
```
PATCH http://localhost:8000/task/1/
Content-Type: application/json
```

**Body:**
```json
{
    "state": "concluida",
    "completion_date": "2024-12-20"
}
```

**Resposta (200 OK):**
```json
{
    "id": 1,
    "title": "Estudar Django Avançado",
    "description": "Completar o desafio e enviar no prazo",
    "deadline": "2025-01-15",
    "completion_date": "2024-12-20",
    "state": "concluida"
}
```

### 7. Deletar uma tarefa (DELETE)

**Requisição:**
```
DELETE http://localhost:8000/task/1/
```

**Resposta (204 No Content):**
*Corpo da resposta vazio*

---

## Códigos de Resposta

| Status Code | Significado |
|-------------|-------------|
| 200 OK | Requisição bem-sucedida (GET, PUT, PATCH) |
| 201 Created | Tarefa criada com sucesso (POST) |
| 204 No Content | Tarefa deletada com sucesso (DELETE) |
| 400 Bad Request | Dados inválidos enviados |
| 404 Not Found | Tarefa não encontrada |

---

## Campos de Task
| Campo |	Tipo |	Obrigatório |	Descrição |
|-------|------|--------------|-----------|
| title	| String (100) |	Sim |	Título da tarefa |
|description |	String (250)|	Não	| Descrição detalhada|
|deadline	|Date|	Sim|	Data limite para conclusão|
|completion_date|	Date|	Não	|Data em que foi concluída|
|state|	String|	Sim|	Situação da tarefa|
---

Valores permitidos para state:
  - nova
  - em_andamento 
  - concluida
  - cancelada

## Executando os Testes

Para executar a suíte de testes:

```
python manage.py test
```
Os testes verificam:
  - Criação de tarefas
  - Listagem com paginação
  - Busca por título e descrição
  - Atualização de tarefas
  - Deleção de tarefas
  - Validação de campos obrigatórios
