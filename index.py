
from distutils.log import fatal
import streamlit as st;
#from array import array;
import pandas as pd;
import numpy as np;
import pickle;
import sklearn;

#  Local URL: http://localhost:8501
#  Network URL: http://192.168.31.232:8501

#st.title("Lets create")
st.markdown(''' 
# Milk Prediction

:sunglasses:<br>
''', True)
#:sunglasses: for emoji
#<br> is html break

#data = pd.read_csv("milkdata.csv")

#st.dataframe(data, width=500, height=500)



pH = st.slider(label="pH value of Milk", min_value=3.0, max_value=9.0, step=0.1)

col1, col2 = st.columns(2)

with col1:
    temp = st.number_input(label="Fill the temperature of Milk",min_value=30, max_value=90, step=1);
    taste = st.selectbox("Fill the Taste of Milk",("Good","Bad"));
    fat = st.selectbox("Fill the Fat content of Milk",("High","Low"));

with col2:
    color = st.number_input("Fill the colour of Milk",min_value=240, max_value=255, step=1);
    odor = st.selectbox("Fill the Odor of Milk",("Good","Bad"));
    turb = st.selectbox("Fill the Turbidity of Milk",("High","Low"));

if taste == "Good":
    _taste = 1
else:
    _taste = 0;

if fat == "High":
    _fat = 1
else:
    _fat = 0;

if odor == "Good":
    _odor = 1
else:
    _odor = 0;

if turb == "High":
    _turb = 1
else:
    _turb = 0;

inputs = np.array([[pH, temp, _taste, _odor, _fat, _turb, color]])

file = "model.pkl"
fileobj = open(file, 'rb')
model = pickle.load(fileobj)



#with open('model.pkl', 'rb') as f:
#   model = pickle.load(f);

prediction = model.predict(inputs)

if prediction == 0:
    _prediction = "High"

elif prediction == 1:
    _prediction = "Low"

else:
    _prediction = "Medium"

if st.button('Predict'):
    st.write('The Quality of the given milk is', _prediction)


