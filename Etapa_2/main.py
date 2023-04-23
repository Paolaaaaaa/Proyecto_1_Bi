from typing import Optional

from fastapi import FastAPI,Request

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import DataModel as dm


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
   
#usa el modelo predictivo, todavía no funciona por completo pero ya casi

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
      



