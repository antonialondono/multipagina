import streamlit as st
from PIL import Image


st.title('Pagina Inicio')
st.write('Hola! Acá te contaré un poco sobre mi 3 series favoritas de cuando era más pequeña')

image = Image.open('series.jpg')

st.image(image)

