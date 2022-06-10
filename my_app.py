from gettext import install
import streamlit as st
import pandas as pd
import numpy as np
import sklearn
from PIL import Image
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler
import joblib
def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://i.pinimg.com/236x/1a/42/73/1a4273b139ae69ce2bc974ccc2f4131d.jpg");
             background-size: auto,
             background-size: 150px
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack_url()
img = Image.open("car.png")




html_temp = """
<div style="background-color:rgb(255,0,0, 25%;padding:1.1px">
<h1 style="color:white;text-align:center;">  🎲 Car Price Prediction 🎲 </h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)
st.image(img, width=700)
st.subheader('This is a web app to predict the car price \
        several features that you can see in the sidebar. Please adjust the\
        value of each feature. After that, click on the "Predict Price" button at the bottom to\
        see the prediction of the regressor.')


#sidebar
st.sidebar.image(img, width=250)
#st.sidebar.title("Predict Your Car Prices")
html_temp2 = """
<div style="background-color:rgb(255,0,0, 25%;padding:1.1px">
<h1 style="color:white;text-align:center;">  🎲Predict Your Car Prices </h1>
</div><br>"""
st.sidebar.markdown(html_temp2,unsafe_allow_html=True)
st.sidebar.header("Predict your car price according to your car features")

df = pd.read_csv("final_scout_not_dummy.csv")

model_list=df["make_model"].unique().tolist()

make_model=st.sidebar.selectbox("Your Model", model_list)

#Gearing_Type
G_Type=df["Gearing_Type"].unique().tolist()
Gearing_Type=st.sidebar.selectbox("Gearing_Type", G_Type)


#Age
#age_list=df["age"].unique().tolist()
age=st.sidebar.selectbox("Age", [0.0,1.0,2.0,3.0])



#hp_kW
hp_kW= st.sidebar.number_input("Hp_kW:",min_value=40, max_value=300,value = 100)


#km
km= st.sidebar.number_input("Km:",min_value=0, max_value=400000,value = 10000)

st.write(' ')
st.write(' ')

my_dict = {
    "make_model": make_model,
    "Gearing_Type":Gearing_Type,
    "Age": age,
    "hp_kW":hp_kW,
    "km":km,
}

col1, col2,col3 = st.columns(3)

with col1:
      #image:
  if make_model:
    if make_model in model_list[0:3]:
        img = Image.open("audi-logo.png")
        st.image(img, width=250)
        
    elif make_model in  model_list[3:6]:
        img = Image.open("opel-logo.png")
        st.image(img, width=250)
        
    else:
        img = Image.open("renault-logo.png")
        st.image(img, width=250)
with col2:       
    st.write(" ")



columns_name=['hp_kW', 'km', 'age', 'make_model_Audi A1', 'make_model_Audi A3',
       'make_model_Opel Astra', 'make_model_Opel Corsa',
       'make_model_Opel Insignia', 'make_model_Renault Clio',
       'make_model_Renault Duster', 'make_model_Renault Espace',
       'Gearing_Type_Automatic', 'Gearing_Type_Manual',
       'Gearing_Type_Semi-automatic']

#st.table(df)
st.subheader("You selected this model:")

df=pd.DataFrame.from_dict([my_dict])
st.dataframe(df.style.highlight_max(axis=0))
df = pd.get_dummies(df)
df = df.reindex(columns=columns_name, fill_value=0)



#pipeline = make_pipeline(MinMaxScaler(),lasso_final_model )
#finalized_model = pipeline.fit(X, y)
#joblib.dump(finalized_model, 'price.mod') 
model = joblib.load('price.model')


if st.button("Predict Price"):
    pred = model.predict(df)
    st.write(pred[0])
    st.title('The selling price of this vehicle will be approximately  {}  €.'.format(round(pred[0], 2)))

