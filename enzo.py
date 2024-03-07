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
    
db: List[Tarefa] = []

@app.get("/")
def ler_tarefas(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "db": db})

@app.post("/tarefas")
def adicionar_tarefa(request: Request, titulo: str = Form(...)):
    nova_tarefa = Tarefa(titulo=titulo)
    nova_tarefa.id = len(db) + 1
    db.append(nova_tarefa)
    return RedirectResponse(url="/", status_code=303)

@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int, request: Request):
    global db
    db = [tarefa for tarefa in db if tarefa.id != tarefa_id]
    return RedirectResponse(url="/", status_code=303)

@app.put("/tarefas/{tarefa_id}")
def atualizar_tarefa(tarefa_id: int, tarefa: Tarefa, request: Request):
    for index, tarefa_existente in enumerate(db):
        if tarefa.id == tarefa_id:
            tarefa_existente.titulo = tarefa.titulo
            db[index] = tarefa_existente
            return RedirectResponse(url="/", status_code=303)
    raise HTTPException(status_code=404, detail=f"Tarefa com ID {tarefa_id} não encontrada.")
