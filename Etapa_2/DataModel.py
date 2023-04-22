from pydantic import BaseModel
import pandas as pd
import csv
from clean_text import clean_text
from sklearn.pipeline import Pipeline
import joblib
class DataModel(BaseModel):
    review_es: str


def columns(self):
        return ["review_es"]


def use_pipeline(movie):
    filename = 'modelo.joblib'
    df_recent = pd.read_csv('./data/'+movie+'.csv', sep=',', encoding = 'utf-8') # Lectura de los datos recientes
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


