import streamlit as st
from pycaret.classification import predict_model
from pycaret.classification import load_model


# load the PyCaret model
model = load_model(gbc_model_jan2023.pkl)

# create a function that makes a prediction using the model
def predict(model, input_data):
    prediction = model.predict(input_data)
    return prediction

# create a function that runs the app
def run_app():
    st.set_page_config(page_title="PyCaret Model App", page_icon=":guardsman:", layout="wide")
    st.title("PyCaret Model App")

    # create a menu with options for instructions and prediction
    menu = ["Homepage", "Prediction"]
    choice = st.sidebar.selectbox("Select an option", menu)

    # show instructions and variable descriptions on the instructions page
    if choice == "Homepage":
        st.subheader("Instructions")
        st.write("This app uses a PyCaret model to make predictions. Please provide the necessary input in the form on the 'Prediction' page.")
        st.write("The model was trained on the following variables:")
        st.write("- variable 1: description")
        st.write("- variable 2: description")
        st.write("- variable 3: description")

    # show the form and prediction on the prediction page
    elif choice == "Prediction":
        st.subheader("Prediction")
        input_data = {}
        input_data['variable1'] = st.number_input('Variable 1')
        input_data['variable2'] = st.number_input('Variable 2')
        input_data['variable3'] = st.number_input('Variable 3')
        if st.button('Predict'):
            prediction = predict(model, input_data)
            st.success('The Prediction is : {}'.format(prediction))

if __name__ == '__main__':
    run_app()
