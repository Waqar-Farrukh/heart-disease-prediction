from pathlib import Path
import json
import pickle
import pandas as pd
import streamlit as st

folder = Path(__file__).parent
st.set_page_config(page_title='Heart Disease Prediction', layout='centered')

@st.cache_resource
def load_files():
    with open(folder / 'heart_disease_model.pkl', 'rb') as file:
        model = pickle.load(file)
    with open(folder / 'results.json') as file:
        results = json.load(file)
    return model, results

model, results = load_files()
st.title('Heart Disease Prediction')
st.caption(f"Test accuracy: {results['accuracy']:.2%}")
pain_types = {'Typical angina': 1, 'Atypical angina': 2,
              'Non-anginal pain': 3, 'Asymptomatic': 4}
with st.form('heart'):
    age = st.number_input('Age in years', min_value=1, max_value=120, value=63)
    cp = st.selectbox('Chest pain type', list(pain_types))
    thalach = st.number_input('Maximum heart rate achieved', min_value=1, max_value=250, value=150)
    exang = st.selectbox('Exercise-induced angina', ['No', 'Yes'])
    submitted = st.form_submit_button('Predict heart disease')

if submitted:
    user_input = pd.DataFrame({'age': [float(age)], 'cp': [float(pain_types[cp])],
                               'thalach': [float(thalach)], 'exang': [float(exang == 'Yes')]})
    prediction = int(model.predict(user_input)[0])
    if prediction == 1:
        st.info('Model predicts: heart disease present')
    else:
        st.success('Model predicts: heart disease absent')

st.caption('Educational model prediction. It is not a medical diagnosis.')
