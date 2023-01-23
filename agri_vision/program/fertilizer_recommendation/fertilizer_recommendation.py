import numpy as np
import pandas as pd

data=pd.read_csv("C:/Users/SANTHOSH/Downloads/agrothon/signup.html/fertilizer/ferti.csv")
# from sklearn.preprocessing import LabelEncoder
# mod=LabelEncoder()
# data['Soil Type']=mod.fit_transform(data['Soil Type'])
#
# data['Crop Type'].unique()
#
# data['Crop Type']=mod.fit_transform(data['Crop Type'])
# data['Fertilizer Name'].unique()
#
# data['Fertilizer Name']=data['Fertilizer Name'].replace({'Urea':1,'DAP':2,'14-35-14':3,'28-28':4,'17-17-17':5,'20-20':6,'10-26-26':7})
#
print(data)

x=data.drop(['Fertilizer Name'],axis=1)
#
y=data['Fertilizer Name']
#
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
from sklearn.linear_model import LogisticRegression
#
model=LogisticRegression()
model.fit(x_train,y_train)
#
model.score(x_test,y_test)
