from pydantic import BaseModel
import pandas as pd
import csv
from clean_text import clean_text
from sklearn.pipeline import Pipeline
import joblib
import matplotlib.pyplot as plt
import io
import base64


class DataModel(BaseModel):
    review_es: str


def columns(self):
        return ["review_es"]


def use_pipeline():
    filename = 'modelo.joblib'
    df_recent = pd.read_csv('./data/movie.csv', sep=',',encoding='ISO-8859-1') # Lectura de los datos recientes
    pipeline = joblib.load(filename)
    print("reviews")
    df_recent["review_es"]=clean_text(df_recent["review_es"])
    print(df_recent["review_es"])
    y_predicted =  pipeline.predict(df_recent["review_es"])
    return y_predicted



def create_csv_movie( nombre_movie,review):
    id_movie = -1

    with open('./data/movies.txt', 'r') as f:
        id_movie = len(f.readlines())
    f.close()
    
    with open('./data/movies.txt', mode='a') as file:
        file.write("\n "+str(id_movie)+","+nombre_movie)
    file.close()

    with open('./data/'+str(id_movie)+'.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['', 'review_es'])
        writer.writerow(['0', "'" +review +"'"])
    file.close()

def add_review(movie_id,review):

    id_movie = -1

    with open('./data/'+str(movie_id)+'.csv', 'r') as f:
        id_movie = len(f.readlines())
    f.close()
    with open('./data/'+str(movie_id)+'.csv', mode='a') as file:
        file.write("\n"+str(id_movie)+",\""+review+"\"")
    file.close()
    return True


def find_movie (movie_id):
    with open('./data/movies.txt', mode='r') as file:
            contenido = file.read()
            if movie_id in contenido:
                 file.close()

                 return True
            else:
                 file.close()

                 return False

def get_Movie (movie_id):

    with open('./data/movies.txt', mode='r') as file:
            lineas = file.readlines()
            for linea in lineas:
                campos = linea.strip().split(",")
                print(campos[0])
                print(movie_id)

                if campos[0]==movie_id:
                    
                    file.close() 
                    return campos
            file.close()
            return False
    


def render_img(data):
    count_1 = data.count(1)
    count_0 = data.count(0)
    labels = ['Positivos', 'Negativos']
    values = [count_1, count_0]
    plt.bar(labels, values)
    plt.title('Frecuencia de comentarios positivos y negativos en los datos')
    plt.xlabel('Valor')
    plt.ylabel('cantidad')
    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)
    encoded_img = base64.b64encode(img_bytes.read()).decode()
    
    return encoded_img
     
     

