from evaluatedetection import getfeatures, getlabels, displayframe
import matplotlib.pyplot as plt
import shapefeatures
import os
from lxml import etree
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve, auc
from sklearn import ensemble
import numpy as np
import glob
import pickle
import cv2
import sys


DATA_DIR = 'data/'
IMAGE_DIR = DATA_DIR + 'images/'
FEATURES_DIR = DATA_DIR + 'features/'
ANNOTATION_DIR = DATA_DIR + 'annotation/'
RESULTS_DIR = DATA_DIR + 'results/'

featureset = [3,7,11,12,15,17]
num_files = 100
threshold = 0.5
train_set_proportion = .8
test_set_proportion = 1 - train_set_proportion
filters = [[11,'>',1000]]
centiles = [0,25,50,75,100]
size = 40
step = 30
reusefeatures = False
savefeatures = False
reuseclassifier = True
saveclassifier = False
saveresults = True

# Split up image files into training and test sets
imgfilenames = glob.glob(IMAGE_DIR + '*.jpg')

baseimgfilenames = [os.path.basename(imgfilenames[i]) 
                    for i in range(num_files)]                            

train, test = train_test_split(np.arange(num_files),
                               train_size=train_set_proportion,
                               test_size=test_set_proportion,
                               random_state=1)  

trainfiles = [baseimgfilenames[i] for i in train]
testfiles = [baseimgfilenames[i] for i in test]  

Xtest = getfeatures(testfiles, size, step,
                    attributes=featureset,
                    filters=filters,
                    centiles=centiles,
                    loadfromfile=reusefeatures, 
                    savetofile=savefeatures,
                    filename='Xtest.npy') 

ytest = getlabels(testfiles, size, step,
                  loadfromfile=reusefeatures,
                  savetofile=savefeatures,
                  filename='ytest.npy')   

classifier = pickle.load(open(FEATURES_DIR + 'classifier.pkl', 'rb')) 

predictions = classifier.predict_proba(Xtest)[:,1]
for i, img_name in enumerate(testfiles):
	img = (cv2.imread("data/images/{}".format(img_name)))
	output = displayframe(img=img, predictions=predictions[i*850:(i+1)*850], labels=ytest[i*850:(i+1)*850], threshold=threshold, size=size, step=step)
	cv2.imwrite(img_name, output)

precision, recall, thresholds = precision_recall_curve(
                                        ytest, predictions)
    
area = auc(recall, precision)
print("Area under precision-recall curve: %0.2f" % area)
    
fig = plt.figure()
fig.set_size_inches(4,4)
plt.plot(recall, precision)
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.grid(True)
plt.ylim([0.0, 1.0])
plt.xlim([0.0, 1.0])
plt.title('Precision-Recall: AUC=%0.2f' % area)
plt.savefig("precision_recall.pdf")
