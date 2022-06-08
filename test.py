from os import listdir
from os.path import isfile, join
import neuralnetwork

mypath = 'C://Users//alena//Desktop//CT_NonCOVID (1)//CT_NonCOVID//'
predictions = []
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
ones = 0
zeros = 0
for file in files:
    prediction = neuralnetwork.predict(mypath + file)
    if prediction[0] == 1:
        ones += 1
    else:
        zeros +=1
    predictions.append(prediction)

print(predictions)
print('zeros', zeros)
print('ones', ones)