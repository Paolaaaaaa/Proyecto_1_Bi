from typing import Optional

from fastapi import FastAPI,Request

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse



app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")# Interface principal
def read_root():
   return {"Hello": "World"}


@app.get("/doc1/",response_class=HTMLResponse)# va a motrar doc1
def doc2(request: Request):
   context ={'request':request}
   return templates.TemplateResponse("doc1.html",context)

@app.get("/doc/",response_class=HTMLResponse) #va a mostrar doc 2 
def doc1(request: Request):
   context ={'request':request}
   return templates.TemplateResponse("doc2.html",context)
   


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}
