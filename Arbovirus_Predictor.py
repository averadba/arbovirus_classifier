import streamlit as st
from pycaret.classification import predict_model
from pycaret.classification import load_model
import pandas as pd


# load the PyCaret model
model = load_model('gbc_model_jan2023')

# create a function that makes a prediction using the model
def predict(model, input_data):
    prediction = model.predict(input_data)
    return prediction

# create a function that runs the app
def run_app():
    st.set_page_config(page_title="Arboviral Infection Classification", page_icon=":guardsman:", layout="wide")
    st.title("Arboviral Infection Classification App")

    # create a menu with options for instructions and prediction
    menu = ["Instructions", "Prediction"]
    choice = st.sidebar.selectbox("Read the instructions or go directly to the prediction tab.", menu)

    # show instructions and variable descriptions on the instructions page
    if choice == "Instructions":
        st.subheader("Instructions")
        st.write("This app uses a machine learning model to make predictions on arboviral infections (**Dengue**, **Chikungunya**, and **Zika** virus)\
             with an accuracy of approximately 87% based on clinical data from the individual. Please provide the necessary input in the form on the 'Prediction' page.\
             Please note that this tool is intended to assist the clinician in differentiating between infections, but it should not be used as the sole basis for \
             diagnosis or treatment. The clinician's medical expertise *should always prevail* when making any decisions regarding a patient's care.")

        st.write("The model was trained on the following variables:")
        st.write("- **Sex:** Biological sex of the individual")
        st.write("- **Abdominal Pain**: Presence/absence of abdominal pain [ICD-9 789.0]")
        st.write("- **Anorexia:** Presence/absence of anorexia [ICD-9 307.1]")
        st.write("- **Arthritis:** Presence/absence of arthritis [ICD-9 307.1]")
        st.write("- **Body Aches:** Presence/absence of body aches")
        st.write("- **Chills:** Presence/absence of chills [ICD-9 780.64]")
        st.write("- **Conjunctivitis:** Presence/absence of conjunctivitis [ICD-9 372.0]")
        st.write("- **Convulsion:** Presence/absence of convulsion or coma [ICD-9 780.01]")
        st.write("- **Cough:** Presence/absence of cough [ICD-9 786.2]")
        st.write("- **Diarrhea:** Presence/absence of diarrhea [ICD-9 787.91]")
        st.write("- **Ecchymosis:** Presence/absence of purpura/ecchymosis (hemorrhagic manifestation) [ICD-9 459.89]")
        st.write("- **Effusion:** Presence/absence of pleural or abdominal effusion, a sign of vascular leakage [ICD-9 511.9]")
        st.write("- **Encephalitis:** Presence/absence of encephalitis or mental status changes [ICD-9 323]")
        st.write("- **Eye Pain:** Presence/absence of eye pain")
        st.write("- **Fever:** Presence/absence of fever (abnormal body temperature >38 Celsius) [ICD-9 780.6]")
        st.write("- **Fout:** Fatal outcome (*i.e.* the patient died)")
        st.write("- **Gums Bleeding:** Presence/absence of bleeding gums (hemorrhagic manifestation)")
        st.write("- **Headache:** Presence/absence of headache (cephalalgia) [ICD-9 784.0]")
        st.write("- **Hypotension:** Systolic blood pressure (SBP) < 90 mm Hg for 11 years old and older, and SBP < 70+ (2 x Age in years) for 10 and younger [ICD-9 458]")
        st.write("- **Icteric:** Icteric, jaundice, or yellow skin [ICD-9 782.4]")
        st.write("- **Joint Pain:** Joint pain (arthralgia) [ICD-9 719.4 ]")
        st.write("- **Lethargy:** Lethargy, restlessness, or fatigue [ICD-9 780.7]")
        st.write("- **Liver Enlargement:** Liver enlargement >2cm (Hepatomegaly) [ICD-9 789.1]")
        st.write("- **Mucosal Bleeding:** Presence/absence of mucosal bleeding")
        st.write("- **Nasal Bleeding:** Nasal bleeding, epistaxis, or nosebleed (hemorrhagic manifestation) [ICD-9 784.7]")
        st.write("- **Nasal Congestion:** Nasal congestion [ICD-9 478.19]")
        st.write("- **Nausea or Vomiting:** Nausea or vomiting [ICD-9 787.0]")
        st.write("- **Pallor or Cool Skin:** Pallor or cool skin. [ICD-9 782.61]")
        st.write("- **Persistent Vomiting:** Presence/absence of persistent vomiting")
        st.write("- **Petechiae:** Petechia (hemorrhagic manifestation) [ICD-9 782.7]")
        st.write("- **Platelet:** Platelet count <= 100,000 (thrombocytopenia) [ICD-9 287.3]")
        st.write("- **Pregnancy:** Pregnancy (patient is pregnant) [ICD-9 V22]")
        st.write("- **Prev Fevefr:** Fever 2-7 days")
        st.write("- **Rapid Weak Pulse:** Rapid, weak pulse")
        st.write("- **Rash:** Skin rash [ICD-9 782.1]")
        st.write("- **Sore Throat:** Sore throat (pharyngitis) [ICD-9 462]")
        st.write("- **Stool Blood:** Patient's stool (feces) contained blood (hemorrhagic manifestation) [ICD-9 578.1]")
        st.write("- **Urinalysis:** Positive urinalysis test over 5 RBC/hpf or positive for blood (hemorrhagic manifestation).")
        st.write("- **Urine Blood:** Blood was present in the patient's urine (hematuria) (hemorrhagic manifestation) [ICD-9 599.7]")
        st.write("- **Vaginal Bleeding:** Vaginal bleeding (hemorrhagic manifestation) [ICD-10 N92-N93]")
        st.write("- **Vomit Blood:** Patient's vomit contained blood (hemorrhagic manifestation) (hematemesis) [ICD-9 578.0]")




    # show the form and prediction on the prediction page
    elif choice == "Prediction":
        st.subheader("Prediction")
        input_data = {}
        input_data['SEX'] = st.selectbox('Sex', ('Male','Female'))
        input_data['Abdominal.Pain'] = st.selectbox('Abdominal Pain', ('Unknown','Yes','No'))
        input_data['Anorexia'] = st.selectbox('Anorexia', ('Unknown','Yes','No'))
        input_data['Arthritis'] = st.selectbox('Arthritis', ('Unknown','Yes','No'))
        input_data['Body.Aches'] = st.selectbox('Body Aches', ('Unknown','Yes','No'))
        input_data['Chills'] = st.selectbox('Chills', ('Unknown','Yes','No'))
        input_data['Conjunctivitis'] = st.selectbox('Conjunctivitis', ('Unknown','Yes','No'))
        input_data['Convulsion'] = st.selectbox('Convulsion', ('Unknown','Yes','No'))
        input_data['Cough'] = st.selectbox('Cough', ('Unknown','Yes','No'))
        input_data['Diarrhea'] = st.selectbox('Diarrhea', ('Unknown','Yes','No'))
        input_data['Ecchymosis'] = st.selectbox('Ecchymosis', ('Unknown','Yes','No'))
        input_data['Effusion'] = st.selectbox('Effusion', ('Unknown','Yes','No'))
        input_data['Encephalitis'] = st.selectbox('Encephalitis', ('Unknown','Yes','No'))
        input_data['Eye.Pain'] = st.selectbox('Eye Pain', ('Unknown','Yes','No'))
        input_data['Fever'] = st.selectbox('Fever', ('Unknown','Yes','No'))
        input_data['Fout'] = st.selectbox('Fatal Outcome', ('Unknown','Yes','No'))
        input_data['Gums.Bleeding'] = st.selectbox('Bleeding Gums', ('Unknown','Yes','No'))
        input_data['Headache'] = st.selectbox('Headache', ('Unknown','Yes','No'))
        input_data['Hypotension'] = st.selectbox('Hypotension', ('No','Yes'))
        input_data['Icteric'] = st.selectbox('Icteric', ('Unknown','Yes','No'))
        input_data['Joint.Pain'] = st.selectbox('Joint Pain', ('Unknown','Yes','No'))
        input_data['Lethargy'] = st.selectbox('Lethargy', ('Unknown','Yes','No'))
        input_data['Liver.Enlargement'] = st.selectbox('Liver Enlargement', ('Unknown','Yes','No'))
        input_data['Mucosal.Bleeding'] = st.selectbox('Mucosal Bleeding', ('Unknown','Yes','No'))
        input_data['Nasal.Bleeding'] = st.selectbox('Nasal Bleeding', ('Unknown','Yes','No'))
        input_data['Nasal.Congestion'] = st.selectbox('Nasal Congestion', ('Unknown','Yes','No'))
        input_data['Nauseaorvomiting'] = st.selectbox('Nausea or Vomiting', ('Unknown','Yes','No'))
        input_data['Pallororcoolskin'] = st.selectbox('Pallor or Cool Skin', ('Unknown','Yes','No'))
        input_data['Persistent.Vomiting'] = st.selectbox('Persistent Vomiting', ('Unknown','Yes','No'))
        input_data['Petechiae'] = st.selectbox('Petechiae', ('Unknown','Yes','No'))
        input_data['Platelet'] = st.selectbox('Platelet', ('Unknown','Yes','No'))
        input_data['Pregnancy'] = st.selectbox('Pregnancy', ('Unknown','Yes','No'))
        input_data['Prev.Fever'] = st.selectbox('Previous Fever', ('Unknown','Yes','No'))
        input_data['Rapid.Weak.Pulse'] = st.selectbox('Rapid Weak Pulse', ('Unknown','Yes','No'))
        input_data['Rash'] = st.selectbox('Rash', ('Unknown','Yes','No'))
        input_data['Sore.Throat'] = st.selectbox('Sore Throat', ('Unknown','Yes','No'))
        input_data['Stool.Blood'] = st.selectbox('Blood in Stool', ('Unknown','Yes','No'))
        input_data['Urinalysis'] = st.selectbox('Urinalysis', ('Unknown','Yes','No'))
        input_data['Urine.Blood'] = st.selectbox('Blood in Urine', ('Unknown','Yes','No'))
        input_data['Vaginal.Bleeding'] = st.selectbox('Vaginal Bleeding', ('Unknown','Yes','No'))
        input_data['Vomit.Blood'] = st.selectbox('Blood in Vomit', ('Unknown','Yes','No'))

        
        if st.button('Predict'):
            input_data = pd.DataFrame([input_data])
            st.write(input_data)
            # input_data = pd.DataFrame.from_dict(input_data, orient='index').T
            # prediction = predict_model(model, data=input_data, raw_score=True)
            # st.write("Probabilities for each class:", prediction)
            # st.write("Predicted Class:", prediction.idxmax(axis=1)[0])

            prediction = predict_model(model, input_data, proba=True)
            st.write("Predicted Class:", prediction.idxmax(axis=1)[0])

# if __name__ == '__main__':
run_app()
