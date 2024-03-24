import streamlit as st
import pickle

st.title('Iris Data Prediction')

sepal_length = st.number_input('Enter sepal length : ')
sepal_width = st.number_input('Enter sepal width : ')
petal_length = st.number_input('Enter petal length : ')
petal_width = st.number_input('Enter petal width : ')

a = st.selectbox('Select the operation : ', ('Description of data', 'Prediction'))

if st.button('Execute??'):
    if a=='Description of data':
        st.write('Development in progress!! will be back soon')
    else:
        with open('Jeffry_model.jeffry', 'rb') as models:
            main_model = pickle.load(models)

        datas = [[sepal_length,sepal_width, petal_length, petal_width]]

        predicted = main_model.predict(datas)
        st.error('Problem!!!')
        st.write(f'My models predictions is {predicted}')

