from gettext import install
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

def set_bg_hack_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://cdn.wallpapersafari.com/64/31/aLP64s.jpg");
             background-size: auto,
             background-size: 150px
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack_url()
img = Image.open("car.png")
new_img=img.resize((750, 250))


st.image(new_img)


html_temp = """
<div style="background-color:rgba(0, 255, 0, 0.3)">
<h1 style="color:white;text-align:center;">  👌Car Price Prediction 👌 </h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)

st.subheader('This is a web app to predict the car price \
        several features that you can see in the sidebar. Please adjust the\
        value of each feature. After that, click on the "Predict Price" button at the bottom to\
        see the prediction of the regressor.')


#sidebar
st.sidebar.image(img, width=250)
#st.sidebar.title("Predict Your Car Prices")
html_temp2 = """
<div style="background-color:rgba(0, 255, 0, 0.3)">
<h1 style="color:white;text-align:center;">  🎲Predict Your Car Prices </h1>
</div><br>"""
st.sidebar.markdown(html_temp2,unsafe_allow_html=True)
st.sidebar.header("Predict your car price according to your car features")

df = pd.read_csv("final_scout_not_dummy.csv")
#make_model
model_list=df["make_model"].unique().tolist()
make_model=st.sidebar.selectbox("Your Model", model_list)
#Gearing_Type
G_Type=df["Gearing_Type"].unique().tolist()
Gearing_Type=st.sidebar.selectbox("Gearing_Type", G_Type)
#Age
age_list=df["age"].unique().tolist()
age=st.sidebar.selectbox("AGE",age_list)
#hp_kW
hp_kW= st.sidebar.slider("Hp_kW:",0.0,max(df["hp_kW"]) ,1.0)
#km
km= st.sidebar.slider("Km",0.0,max(df["km"]) ,100.0)
#Gears
Gears_=df["Gears"].unique().tolist()
Gears= st.sidebar.selectbox("Gears:",Gears_)
st.write(' ')
st.write(' ')

my_dict = {
            "make_model": make_model,
            "Gearing_Type":Gearing_Type,
            "age": age,
            "hp_kW":hp_kW,
            "km":km,
            "Gears":Gears
        }

col1, col2= st.columns(2)
with col1:       
    st.subheader("You selected this model:")
with col2:
      #image:
  if make_model:
    if make_model=="Audi A1":
        img = Image.open("audi-a1.jpg")
        new_img=img.resize((750, 500))
        st.image(new_img)
    elif make_model=="Audi A2":
        img = Image.open("audi-a2.jpg")
        new_img=img.resize((750, 500))
        st.image(new_img)
    elif make_model=="Audi A3":
        img = Image.open("audi-a3.jpg")
        new_img=img.resize((750, 500))
        st.image(new_img)
    elif make_model=="Opel Corsa":
        img = Image.open("opel-corsa.jpg")
        new_img=img.resize((750, 500))
        st.image(new_img)
    elif make_model=="Opel Astra":
        img = Image.open("opel_astra.jpg")
        new_img=img.resize((750, 500))
        st.image(new_img) 
    elif make_model=="Opel Insignia":
        img = Image.open("opel_insignia.png")
        new_img=img.resize((750, 500))
        st.image(new_img) 
    elif make_model=="Renault Clio":
        img = Image.open("Renault_Clio.jpg")
        new_img=img.resize((750, 500))
        st.image(new_img)  
    elif make_model=="Renault Duster":
        img = Image.open("renault_duster.jpg")
        new_img=img.resize((750, 500))
        st.image(new_img)  
    else:
        img = Image.open("renault_espace.jpg")
        new_img=img.resize((750, 500))
        st.image(new_img)




# table
#st.table(df)
# style
th_props = [
  ('font-size', '14px'),
  ('text-align', 'center'),
  ('font-weight', 'bold'),
  ('color', '#6d6d6d'),
  ('background-color', '#f7ffff'),("width", "850px"),
            ("height","80px")
  ]
                               
td_props = [
  ('font-size', '15px')
  ]
                                 
styles = [
  dict(selector="th", props=th_props),
  dict(selector="td", props=td_props)
  ]
df=pd.DataFrame.from_dict([my_dict])

df2=df.style.set_properties(**{'text-align': 'left'}).set_table_styles(styles)

st.table(df2.set_properties(**{'background-color': 'black',
                                        'color': 'lawngreen',
                                        'border-color': 'white'}))

import joblib

filename ="pipe_model.pkl"
model =joblib.load(open(filename, 'rb'))


myButton = st.button("Predict Price")
button_style = """
        <style>
        .stButton > button {
            color: lawngreen;
            background: black;
            width: 700px;
            height: 50px;
            font-size: 25px;
        }
        </style>
        """
st.markdown(button_style, unsafe_allow_html=True)
if myButton:
    pred = model.predict(df)
   
    st.write(round(pred[0], 3))
    st.title('The selling price of this vehicle will be approximately  {}  €.'.format(round(pred[0], 1)))
