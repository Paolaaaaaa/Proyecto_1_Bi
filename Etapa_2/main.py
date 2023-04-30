from typing import Optional
import json
from fastapi import FastAPI, HTTPException,Request
from fastapi.responses import RedirectResponse
import matplotlib.pyplot as plt

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, validator
import DataModel as dm
import os
import shutil


app = FastAPI()
templates = Jinja2Templates(directory="templates")


from fastapi import FastAPI, UploadFile, File

app = FastAPI()

app.data = []

@app.post("/upload-csv",response_class=HTMLResponse)
async def upload_csv(file: UploadFile = File(...)):
    file_path = os.path.join("./data", "movie.csv")
    with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    data=dm.use_pipeline().tolist()
    print(dm.use_pipeline())
    img = dm.render_img(data)

    app.data = data

    context = {"request": {"data": data}, "extensions": {},"graph":img}
    
    # renderizar el archivo HTML con los datos
    return templates.TemplateResponse("grafs.html", context=context)


@app.get("/grafs/",response_class=HTMLResponse)# va a motrar grafs
def graf(request: Request):
    context = {"request": request, "data": app.data}
    return templates.TemplateResponse("grafs.html", context=context)

@app.get("/")# Interface principal
def read_root(request: Request):  
   context ={'request':request}
   return templates.TemplateResponse("index.html",context)



@app.get("/doc/",response_class=HTMLResponse) #va a mostrar doc 2 
def doc1(request: Request):
   context ={'request':request}
   return templates.TemplateResponse("doc1.html",context)
   
#

@app.get("/movie/{movie_id}")
def show_moview(movie_id: int, request: Request):

   if(dm.find_movie(str(movie_id))):
       movie_info=dm.get_Movie(str(movie_id))
       print((dm.use_pipeline(str(movie_id))))
       context ={'request':request}

       return templates.TemplateResponse("template_movie.html", {"movie_title": movie_info[1], "movie_img": movie_info[2], "descripcion": movie_info[3], "request":request})
   else:
       context ={'request':request}

       return templates.TemplateResponse("template_error.html", context)
   

@app.get("/index/",response_class=HTMLResponse)
def index(request: Request):
   context ={'request':request}
   return templates.TemplateResponse("index.html",context)
#Crea un nuevo csv y lo adiciona a la lista de peliculas
    
@app.get("/movie/create/{nombre_movie}/{review}")# Para crear un nuevo csv
def read_item(nombre_movie: str, review:str):
      if(dm.find_movie(str(nombre_movie))):
          return dm.add_review(nombre_movie,review)
      else:
          dm.create_csv_movie(str(nombre_movie),review)
      return True
# Para crear un nuevo review
@app.get("/movie/{nombre_movie}/create/{review}")
def read_item(nombre_movie: str, review:str):
      if(dm.find_movie(str(nombre_movie))):
        return dm.add_review(nombre_movie,review)
      else:
        return False
      



