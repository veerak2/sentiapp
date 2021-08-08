#!/usr/bin/env python
# coding: utf-8

# In[1]:


import uvicorn
#import wandb
#from typing import List
from pydantic import BaseModel
from fastapi import FastAPI
import tensorflow as tf
import numpy as np

app = FastAPI()


# In[2]:


#best_model = wandb.restore(
#  'model-best.h5', run_path="kavinv/imdb_sentiment_classification/runs/2xllp48u")


# In[3]:


#getting the model
model = tf.keras.models.load_model('Model')


# In[4]:


#import nest_asyncio
#nest_asyncio.apply()
#__import__('IPython').embed()


# In[6]:





# In[ ]:


class Reviews(BaseModel):
    review: str

@app.get('/')
def index():
    return {'message': 'This is IMDb Reviews Classification API!'}

@app.post('/predict')
def predict_review(data: Reviews):
    """ FastAPI 
    Args:
        data (Reviews): json file 
    Returns:
        prediction: probability of review being positive
    """
    data = data.dict()
    review = data['review']
    word_index = tf.keras.datasets.imdb.get_word_index()
    test = []
    for i in review.split():
        test.append(word_index.get(i))
    while len(test) < 500:
        test = [0] + test
    sample_sent = np.stack(test)
    sample_sent = np.expand_dims(sample_sent,axis=0)
    prediction = model.predict(sample_sent)
    return {
        'prediction': prediction.tolist()[0][0]
    }

if __name__ == '__main__':
   uvicorn.run(app, host='127.0.0.1', port=8003)


# In[ ]:




