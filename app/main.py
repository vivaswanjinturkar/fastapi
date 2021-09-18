
import numpy as np
import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import json
import uvicorn

class banknote(BaseModel):
    variance:float
    skewness:float
    curtosis:float
    entropy:float

app=FastAPI()

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.get('/')
def get_root():
    
	return {'message': 'Welcome to the API'}

@app.post('/predict')
async def predict(data:banknote):
    data=data.dict()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']
    dp=np.array([variance,skewness,curtosis,entropy]).reshape(1,-1)

    prediction=classifier.predict(dp)
    return str(prediction)

#if __name__ =="__main__":
#    uvicorn.run(app,host="127.0.0.1",port=8000)

    
    