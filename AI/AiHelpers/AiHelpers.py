import sys
#from keras.models import load_model
#from tflite_runtime.interpreter import Interpreter
import tflite_runtime.interpreter as tflite

#model = tflite.Interpreter('AI/tf_liteModel.tflite')

#def classify_image(interpreter, image, top_k=1):
  

def runAiModel(image):
    image=tensor(image)
    #temp = model.(image)
    #modelOutput = temp.index(max(temp))
    #model.set_tensor(image)
   # model.invoke()
    #output_data = model.get_tensor((1,3))
    # print("Inference output is {}".format( label_id))
    model.allocate_tensors()
    model = tflite.Interpreter('AI/tf_liteModel.tflite')

    _, height, width, _ = model.get_input_details()[0]['shape']
#***************************************************************************
    tensor_index = model.get_input_details()[0]['index']
    input_tensor = model.tensor(tensor_index)()[0]
    input_tensor[:, :] = image

   
    model.invoke()
    output_details = model.get_output_details()[0]
    output = np.squeeze(model.get_tensor(output_details['index']))

    scale, zero_point = output_details['quantization']
    output = scale * (output - zero_point)

    ordered = np.argpartition(-output, top_k)
#***********************************************************************
    label_id, prob = [(i, output[i]) for i in ordered[:top_k]][0]
    modelOutput = label_id

    print("Image Shape (", width, ",", height, ")")
    print('ID : ',label_id)
    return modelOutput

'''

from tflite_runtime.interpreter import Interpreter 
from PIL import Image
import numpy as np
import time

data_folder = "/home/pi/TFLite_MobileNet/"

model_path = data_folder + "mobilenet_v1_1.0_224_quant.tflite"
label_path = data_folder + "labels_mobilenet_quant_v1_224.txt"

interpreter = Interpreter(model_path)
print("Model Loaded Successfully.")

interpreter.allocatetensors()
, height, width, _ = interpreter.get_input_details()[0]['shape']
print("Image Shape (", width, ",", height, ")")

# Load an image to be classified.
image = Image.open(data_folder + "test.jpg").convert('RGB').resize((width, height))

# Classify the image.
time1 = time.time()
label_id, prob = classify_image(interpreter, image)
time2 = time.time()
classification_time = np.round(time2-time1, 3)
print("Classificaiton Time =", classification_time, "seconds.")

# Read class labels.
labels = load_labels(label_path)

# Return the classification label of the image.
classification_label = labels[label_id]
print("Image Label is :", classification_label, ", with Accuracy :", np.round(prob*100, 2), "%.")
'''