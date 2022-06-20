from pyexpat import model
from unittest import result
from pyrsistent import v
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import streamlit.components.v1 as stc
from PIL import Image

model=pickle.load(open('heart_disease_prediction.sav','rb'))

image=Image.open('heart attack.jpeg')




def input_features(BMI, Smoking, AlcoholDrinking, Stroke,
       PhysicalHealth, MentalHealth, DiffWalking, Sex, AgeCategory,
       Race, Diabetic, PhysicalActivity, GenHealth, SleepTime,
       Asthma, KidneyDisease, SkinCancer):
    prediction=model.predict([[BMI, Smoking, AlcoholDrinking, Stroke,
       PhysicalHealth, MentalHealth, DiffWalking, Sex, AgeCategory,
       Race, Diabetic, PhysicalActivity, GenHealth, SleepTime,
       Asthma, KidneyDisease, SkinCancer]])
    if (prediction[0]==0):
        print("The preson don't have heart disease")
    else:
        print("The person have heart disease")
    print(prediction)
    return prediction
   



def main():
    st.title("Heart disease predictions ")

    html_temp = """
    <div style ="background-color:blue;padding:13px">
    <h1 style ="color:black;text-align:center;"> Check you have heart disease prediction using the below  ML App </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)


    st.image(image,caption='Check you have heart disease')


    BMI=st.slider("Enter body mass index",12.02,94.85)
    Smoking=st.selectbox("your Smoking status yes=1,or no=0",["1","0"])
    AlcoholDrinking=st.selectbox("your alcoholdrinking status yes=1,or no=0",["1","0"])
    Stroke=st.selectbox("your Stroke status yes=1,or no=0",["1","0"])
    PhysicalHealth=st.slider("Enter PhysicalHealth",0.0,30.0,0.1)
    MentalHealth=st.slider("Enter MentalHealth",0.0,30.0,0.1)
    DiffWalking=st.selectbox("your DiffWalking status yes=1,or no=0",["1","0"])
    Sex=st.selectbox("(1=Male,0=Female)",["1","0"])
    AgeCategory=st.text_input("Enter your age",18,85,1)
    Race=st.selectbox("(White=5, Black=4, Asian'=3, American Indian/Alaskan Native=2,Other=1, Hispanic=0)",["5","4","3","2","1","0"])
    Diabetic=st.selectbox("your Diabetic status yes=1,or no=0",["1","0"])
    PhysicalActivity=st.selectbox("your PhysicalActivity status yes=1,or no=0",["1","0"])
    GenHealth=st.selectbox("(Very good=4, Fair=3, Good=2, Poor=1, Excellent=0)",["4","3","2","1","0"])
    SleepTime=st.slider("Enter your sleeptime",1.0,24.0,1.0)
    Asthma=st.selectbox("your Asthma status yes=1,or no=0",["1","0"])
    KidneyDisease=st.selectbox("your KidneyDiseas status yes=1,or no=0",["1","0"])
    SkinCancer=st.selectbox("your SkinCancer status yes=1,or no=0",["1","0"])
    
    result= " "
    
    if st.button("Predict"):
        result=input_features(BMI, Smoking, AlcoholDrinking, Stroke,
       PhysicalHealth, MentalHealth, DiffWalking, Sex, AgeCategory,
       Race, Diabetic, PhysicalActivity, GenHealth, SleepTime,
       Asthma, KidneyDisease, SkinCancer)
    
        if (result[0]==0):
            st.warning("The preson don't have heart disease")
        else:
            st.success("The preson have heart disease")
    



if __name__=='__main__':
    main()

