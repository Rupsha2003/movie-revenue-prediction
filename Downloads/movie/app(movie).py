import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('trained_model.sav', 'rb'))

# Title
st.title('🎬 Movie Revenue Prediction App')

st.write("""
### Enter Movie Details:
""")

# Input fields (Example features: budget, popularity, runtime)
budget = st.number_input('Movie Budget (in million USD)', min_value=0.0)
popularity = st.slider('Popularity Score', 0.0, 100.0, 50.0)
runtime = st.number_input('Runtime (in minutes)', min_value=30, max_value=300, value=120)

# Button for prediction
if st.button('Predict Revenue'):
    input_data = np.array([[budget, popularity, runtime]])
    prediction = model.predict(input_data)
    
    st.success(f'🎯 Predicted Revenue: ${prediction[0]:,.2f}')
