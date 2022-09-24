import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


html_temp = """
<div style="background-color:#ABBAEA;padding:1.5px">
<h1 style="color:white;text-align:center;"> Car Price Prediction</h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)

#sidebar
st.sidebar.title(" Predict Your Car Prices(in Euros)")
st.sidebar.header("Predict your car price according to your car features")

# select box
#make_model

make_model=st.sidebar.selectbox("Your Model", ["Audi A1","Audi A3","Opel Astra", "Opel Corsa", "Opel Insignia","Renault Clio","Renault Duster","Renault Espace"])
st.write("You selected this model:", make_model)
#image

if make_model[0:2]:
    img = Image.open("audi-logo.png")
    st.image(img, caption="AUDI", width=300)
elif make_model[2:5]:
    img = Image.open("Opel-logo.png")
    st.image(img, caption="OPEL", width=300)
else:
    img = Image.open("renault-logo.png.png")
    st.image(img, caption="RENAULT", width=300)

#Gearing_Type
Gearing_Type=st.sidebar.selectbox("Gearing_Type", ["Automatic","Manual","Semi-automatic"])
st.write("You selected this  Gearing Type:", Gearing_Type)



#AGE
age=st.sidebar.selectbox("AGE", ["3", "2", "1", "0"])
st.write("You selected this age:", age)

#hp_kW
hp_kW= st.sidebar.number_input("hp_kW:",min_value=40, max_value=300)
st.write("You selected this hp_kW:", hp_kW)

#km
km= st.sidebar.number_input("km:",min_value=0, max_value=400000,)
st.write("You selected this km:", km)


my_dict = {
    "make_model": make_model,
    "Gearing_Type":Gearing_Type,
    "Age": age,
    "hp_kW":hp_kW,
    "km":km,
}
df=pd.DataFrame.from_dict([my_dict])
st.table(df)

import pickle
filename = 'my_price_model'
model = pickle.load(open(filename, 'rb'))

df=pd.DataFrame.from_dict([my_dict])
st.table(df)
if st.button("Predict Price"):
    pred = model.predict(df)
    st.write(pred[0])
