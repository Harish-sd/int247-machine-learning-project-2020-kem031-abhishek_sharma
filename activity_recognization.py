# -*- coding: utf-8 -*-
"""Activity Recognization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uqf_vdCFqyPPuXcFbXSt4aqns-WDP89T
"""

# Commented out IPython magic to ensure Python compatibility.
#Importing basic libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
# %matplotlib inline

#Importing the models ans preprocessing functions
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

from google.colab import files
uploaded = files.upload()
import io
train_data= pd.read_csv(io.BytesIO(uploaded['train.csv']))

from google.colab import files
uploaded = files.upload()
import io
test_data= pd.read_csv(io.BytesIO(uploaded['test.csv']))

#Dividing the dataset into test and train datasets
y_train=train_data['Activity']
x_train= train_data.drop(columns = ['Activity', 'subject'])

y_test=test_data['Activity']
x_test= test_data.drop(columns = ['Activity', 'subject'])

count_of_each_activity = np.array(y_train.value_counts())

# Identify all the unqiue activities and in sorted order
activities = sorted(y_train.unique())

# Plot a pie chart for different activities
plt.rcParams.update({'figure.figsize': [20, 20], 'font.size': 24})
plt.pie(count_of_each_activity, labels = activities, autopct = '%0.2f')

accuracy_scores = np.zeros(4)

# Support Vector Classifier
from sklearn.svm import SVC
clf = SVC().fit(x_train, y_train)
prediction = clf.predict(x_test)
accuracy_scores[0] = accuracy_score(y_test, prediction)*100
print('Support Vector Classifier accuracy: {}%'.format(accuracy_scores[0]))


# Logistic Regression
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression().fit(x_train, y_train)
prediction = clf.predict(x_test)
accuracy_scores[1] = accuracy_score(y_test, prediction)*100
print('Logistic Regression accuracy: {}%'.format(accuracy_scores[1]))


# K Nearest Neighbors
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier().fit(x_train, y_train)
prediction = clf.predict(x_test)
accuracy_scores[2] = accuracy_score(y_test, prediction)*100
print('K Nearest Neighbors Classifier accuracy: {}%'.format(accuracy_scores[2]))


# Random Forest
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier().fit(x_train, y_train)
prediction = clf.predict(x_test)
accuracy_scores[3] = accuracy_score(y_test, prediction)*100
print('Random Forest Classifier accuracy: {}%'.format(accuracy_scores[3]))


#visualization
colors = cm.rainbow(np.linspace(0, 1, 4))
labels = ['Support Vector Classifier', 'Logsitic Regression', 'K Nearest Neighbors', 'Random Forest']
plt.bar(labels,
        accuracy_scores,
        color = colors)
plt.xlabel('Classifiers')
plt.ylabel('Accuracy')
plt.title('Accuracy of various algorithms')

