from pydantic import BaseModel
from sklearn.pipeline import Pipeline
from sklearn.pipeline import Pipeline
from joblib import dump
class DataModel(BaseModel):
    review_es: str


def columns(self):
        return ["review_es"]


def generate_pipeLine():

    pipeline = Pipeline(
        [
            ('scaler', StandardScaler()),
            ('model', LinearRegression())
        ]
    )
    pipeline.fit(x_train_m2, y_train_m2)
    dump(pipeline, 'modelo.joblib')



def use_pipeline(movie):
    filename = 'modelo.joblib'
    df_recent = pd.read_csv('./data/'+movie+'.csv', sep=',', encoding = 'utf-8') # Lectura de los datos recientes
    pipeline = joblib.load(filename)
    y_predicted =  pipeline.predict(df_recent)
    return y_predicted

