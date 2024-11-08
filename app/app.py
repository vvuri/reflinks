import uvicorn
from fastapi import FastAPI
from ml.iris.model import IrisModel, IrisSpecies

app = FastAPI()
model_iris = IrisModel()


@app.get('/')
def index():
    return {'message': 'Hello, stranger'}


@app.get('/{name}')
def get_name(name: str):
    return {'message': f'Hello, {name}'}


@app.post('/predict_iris')
def predict_species(iris: IrisSpecies):
    data = iris.dict()
    prediction, probability = model_iris.predict_species(
        data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']
    )
    return {
        'prediction': prediction,
        'probability': probability
    }


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
