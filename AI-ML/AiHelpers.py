#from tensorflow import keras
import sys
from keras.models import load_model

#model = keras.models.load_model("")
model = load_model('../../AI-ML/ourAiModel/')

def runAiModel(image):

    temp = model.predict(image)
    modelOutput = temp.index(max(temp))
    return modelOutput