from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class Tarefa(BaseModel):
    id: Optional[int] = None
    titulo: str
# Para simplificar vamos trabalhar com um banco de dados ficticio, apenas uma lista chamada db.
db: List[Tarefa] = []

# Corrija esse endpoint para que ele envie ao template index.html todos os itens no nosso banco de dados db.
@app.get("/")
def ler_tarefas(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "tarefas": db})

# Corrija o endpoint a seguir para que ele seja capaz de adicionar tarefas ao nosso banco de dados. Lembre-se que nosso banco de dados é um simples lista.
@app.get("/tarefas")
def adicionar_tarefa(request: Request, titulo: str = Form(...)):
    nova_tarefa = Tarefa(titulo=titulo)
    nova_tarefa.id = len(db) + 1
    db.append(nova_tarefa)
    return RedirectResponse(url="/", status_code=303)

# Corrija o endpoint a seguir para que ele seja capaz de deletar items do banco de dados.
@app.get("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int, request: Request):
    global db
    db = [tarefa for tarefa in db if nova_tarefa.id != tarefa]
    return RedirectResponse(url="/", status_code=303)

# Corrija o endpoint a seguir para que ele seja capaz de atulizar items do banco de dados.
@app.git("/tarefas/{tarefa_id}")
def atualizar_tarefa(tarefa_id: int, tarefa: Tarefa, request: Request):
    for tarefa, tarefa_existente in enumerate(db):
        if nova_tarefa.id == tarefa_id:
            tarefa_existente.titulo = tarefa.titulo
            db[index] = Tarefa
            return RedirectResponse(url="/", status_code=303)
    raise HTTPException(status_code=404, detail=f"Tarefa com ID {tarefa_id} não encontrada.")
