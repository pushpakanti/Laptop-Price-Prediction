import streamlit as st
import pickle
import numpy as np


#importing model
pipe= pickle.load(open('pipe.pkl','rb'))
df= pickle.load(open('df.pkl', 'rb'))

st.title("Laptop Price Predictor")

#brand
company= st.selectbox('Brand', df['Company'].unique())

#type of laptop
type= st.selectbox('Type', df['TypeName'].unique())

#RAM
ram= st.selectbox('RAM (in GB)',[2,4,8,12,16,24,32,64])

#weight
weight = st.number_input('Weight of the laptop')


#TouchScreen
touchscreen= st.selectbox('Touchscreen', ['Yes','No'])

# Display
hd_display=st.selectbox('HD Display', ['Yes','No'])

#IPS
ips = st.selectbox('IPS', ['Yes', 'No'])

#screen size
screen_size= st.number_input('Screen Size')

#resolution
resolution= st.selectbox('Screen Resolution',['1920x1080',
                 '1366x768','1600x900','3840x2160','3200x1800',
                 '2880x1800','2560x1600','2560x1440','2304x1440'])

# cpu
cpu= st.selectbox('CPU', df['Cpu brand'].unique())

hdd= st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])
ssd= st.selectbox('SSD(in GB)',[0,128,256,512,1024,2048])

gpu= st.selectbox('GPU', df['Gpu brand'].unique())
os= st.selectbox('Operating System', df['os'].unique())

if st.button('Predict Price'):
    # Convert 'Yes'/'No' to 1/0
    touchscreen = 1 if touchscreen == 'Yes' else 0
    hd_display = 1 if hd_display == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0

    # Calculate PPI
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size

    # Create DataFrame for input
    import pandas as pd
    query = pd.DataFrame([{
    'Company': company,
    'TypeName': type,
    'Ram': ram,  # Not 'RAM'
    'Weight': weight,
    'Touchscreen': touchscreen,
    'HD Display': hd_display,
    'Ips': ips,  # Not 'IPS'
    'ppi': ppi,  # Not 'PPI'
    'Cpu brand': cpu,
    'HDD': hdd,
    'SSD': ssd,
    'Gpu brand': gpu,
    'os': os
}])

    # Predict using the pipeline
    predicted_price = np.exp(pipe.predict(query)[0])
    st.title("💰 The predicted price is ₹ " + str(int(predicted_price)))
