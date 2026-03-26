import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import warnings
warnings.filterwarnings("ignore")
st.set_page_config(
    page_title="Health Assistant AI",
    layout="wide",
    page_icon="🧑‍⚕️"
)

# -------- HEADER --------
st.title("👨‍⚕️🩺 AI Health Assistant")
st.markdown(
"""
This application uses **Machine Learning models** to predict the likelihood of:
- Diabetes
- Heart Disease
- Parkinson's Disease

Enter the patient information and click **Predict**.
"""
)


@st.cache_resource
def load_models():
    diabetes_model = pickle.load(open(r"D:\MLwork\saved_models\diabetes_model.sav","rb"))
    heart_disease_model = pickle.load(open(r"D:\MLwork\saved_models\heart_disease_model.sav","rb"))
    parkinsons_model = pickle.load(open(r"D:\MLwork\saved_models\parkinsons_model.sav","rb"))
    return diabetes_model,heart_disease_model,parkinsons_model

diabetes_model,heart_disease_model,parkinsons_model = load_models()
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3774/3774299.png", width=120)
    selected = option_menu("Muliple Disease",
                            ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                            menu_icon='hospital',
                            icons=["activity","heart","person"],
                            default_index=0)
    
if selected == "Diabetes Prediction":
    st.title("🩺 Diabetes Prediction")
    st.markdown("Enter the patient's medical information to predict diabetes disease risk.")
    with st.form("Diabetes_disease_form"):
        col1,col2,col3 = st.columns(3)
        with col1:
            Pregnancies = st.number_input("Pregnancies",0,20,1)

        with col2:
            Glucose = st.number_input("Glucose Level",0,300,120)

        with col3:
            BloodPressure = st.number_input("Blood Pressure",0,200,70)

        with col1:
            SkinThickness = st.number_input("Skin Thickness",0,100,20)

        with col2:
            Insulin = st.number_input("Insulin",0,900,80)

        with col3:
            BMI = st.number_input("BMI",0.0,70.0,25.0)

        with col1:
            DiabetesPedigreeFunction = st.number_input("Pedigree Function",0.0,3.0,0.5)

        with col2:
            Age = st.number_input("Age",1,120,30)

        submit = st.form_submit_button("🔍 Predict Diabetes")

    if submit:
        with st.spinner("Analyzing patient data..."):
            input_data =  [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                        BMI, DiabetesPedigreeFunction, Age]
        
            diab_prediction = diabetes_model.predict([input_data])
        st.subheader("Prediction Result")
        if diab_prediction[0] == 1:
            st.error("⚠️ The person is diabetic")
        else:
            st.success("✅ The person is not diabetic")
    
if selected == "Heart Disease Prediction":

    st.title("💔 Heart Disease Prediction")
    st.markdown("Enter the patient's medical information to predict heart disease risk.")

    with st.form("heart_disease_form"):

        col1, col2 = st.columns(2)

        with col1:
            age = st.number_input('Age', 1, 120, 40)
            cp = st.number_input('Chest Pain types', 0, 3, 1)
            chol = st.number_input('Serum Cholestoral in mg/dl', 100, 600, 200)
            restecg = st.number_input('Resting Electrocardiographic results', 0, 2, 1)
            exang = st.number_input('Exercise Induced Angina', 0, 1, 0)
            slope = st.number_input('Slope of the peak exercise ST segment', 0, 2, 1)
            thal = st.number_input('thal: 0 = normal , 1 = fixed defect , 2 = reversable defect',0, 2, 1)

        with col2:
            sex = st.number_input('Sex (0 = Female, 1 = Male)', 0, 1, 1)
            trestbps = st.number_input('Resting Blood Pressure', 80, 200, 120)
            fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl (1=True,0=False)', 0, 1, 0)
            thalach = st.number_input('Maximum Heart Rate achieved', 60, 220, 150)
            oldpeak = st.number_input('ST depression induced by exercise', 0.0, 10.0, 1.0)
            ca = st.number_input('Major vessels colored by flourosopy', 0, 4, 0)

        submit = st.form_submit_button("🔍 Heart Disease Test Result")

    if submit:

        user_input = [
            age, sex, cp, trestbps, chol, fbs,
            restecg, thalach, exang, oldpeak,
            slope, ca, thal
        ]

        with st.spinner("Analyzing patient data..."):
            heart_prediction = heart_disease_model.predict([user_input])

        st.subheader("Prediction Result")

        if heart_prediction[0] == 1:
            st.error("⚠️ The person is having heart disease")
        else:
            st.success("✅ The person does not have any heart disease")
    

if selected == "Parkinsons Prediction":

    st.title("🧠 Parkinsons Prediction")
    st.markdown("Enter the patient's voice measurements to predict Parkinson's disease.")

    with st.form("parkinsons_form"):

        col1, col2, col3 = st.columns(3)

        with col1:
            fo = st.number_input('MDVP:Fo(Hz)', min_value=50.0, max_value=300.0, value=120.0, step=0.1)
            Jitter_percent = st.number_input('MDVP:Jitter(%)', min_value=0.0, max_value=1.0, value=0.005, step=0.0001)
            RAP = st.number_input('MDVP:RAP', min_value=0.0, max_value=1.0, value=0.003, step=0.0001)
            Shimmer = st.number_input('MDVP:Shimmer', min_value=0.0, max_value=0.5, value=0.03, step=0.001)
            APQ3 = st.number_input('Shimmer:APQ3', min_value=0.0, max_value=0.5, value=0.02, step=0.001)
            NHR = st.number_input('NHR', min_value=0.0, max_value=1.0, value=0.02, step=0.001)
            spread1 = st.number_input('spread1', min_value=-10.0, max_value=10.0, value=-5.0, step=0.1)
            D2 = st.number_input('D2', min_value=0.0, max_value=10.0, value=2.0, step=0.1)

        with col2:
            fhi = st.number_input('MDVP:Fhi(Hz)', min_value=50.0, max_value=400.0, value=150.0, step=0.1)
            Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', min_value=0.0, max_value=0.01, value=0.0005, step=0.00001)
            PPQ = st.number_input('MDVP:PPQ', min_value=0.0, max_value=1.0, value=0.005, step=0.0001)
            Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', min_value=0.0, max_value=1.0, value=0.3, step=0.01)
            APQ5 = st.number_input('Shimmer:APQ5', min_value=0.0, max_value=0.5, value=0.02, step=0.001)
            HNR = st.number_input('HNR', min_value=0.0, max_value=100.0, value=20.0, step=0.1)
            spread2 = st.number_input('spread2', min_value=-10.0, max_value=10.0, value=0.2, step=0.1)
            PPE = st.number_input('PPE', min_value=0.0, max_value=1.0, value=0.1, step=0.01)

        with col3:
            flo = st.number_input('MDVP:Flo(Hz)', min_value=50.0, max_value=300.0, value=100.0, step=0.1)
            DDP = st.number_input('Jitter:DDP', min_value=0.0, max_value=1.0, value=0.01, step=0.0001)
            APQ = st.number_input('MDVP:APQ', min_value=0.0, max_value=0.5, value=0.03, step=0.001)
            DDA = st.number_input('Shimmer:DDA', min_value=0.0, max_value=0.5, value=0.04, step=0.001)
            RPDE = st.number_input('RPDE', min_value=0.0, max_value=1.0, value=0.5, step=0.01)
            DFA = st.number_input('DFA', min_value=0.0, max_value=1.0, value=0.7, step=0.01)

        submit = st.form_submit_button("🔍 Parkinson's Test Result")

    if submit:

        input_data = [
            fo, fhi, flo, Jitter_percent, Jitter_Abs,
            RAP, PPQ, DDP, Shimmer, Shimmer_dB,
            APQ3, APQ5, APQ, DDA, NHR,
            HNR, RPDE, DFA, spread1, spread2,
            D2, PPE
        ]

        with st.spinner("Analyzing patient data..."):
            park_prediction = parkinsons_model.predict([input_data])

        st.subheader("Prediction Result")

        if park_prediction[0] == 1:
            st.error("⚠️ The person has Parkinson's disease")
        else:
            st.success("✅ The person does not have Parkinson's disease")

