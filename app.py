import streamlit as st
import pandas as pd
from warnings import simplefilter

simplefilter(action='ignore', category=FutureWarning)
from PIL import Image
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression


data=pd.read_csv('heart_2020_cleaned.csv')
data['Smoking']=data['Smoking'].map({'Yes':1,'No':0})
data['AlcoholDrinking']=data['AlcoholDrinking'].map({'Yes':1,'No':0})
data['Stroke']=data['Stroke'].map({'Yes':1,'No':0})
data['DiffWalking']=data['DiffWalking'].map({'Yes':1,'No':0})
data['Diabetic']=data['Diabetic'].map({'Yes':1,'No':0})
data['Asthma']=data['Asthma'].map({'Yes':1,'No':0})
data['KidneyDisease']=data['KidneyDisease'].map({'Yes':1,'No':0})
data['SkinCancer']=data['SkinCancer'].map({'Yes':1,'No':0})
data['PhysicalActivity']=data['PhysicalActivity'].map({'Yes':1,'No':0})
data['Sex']=data['Sex'].map({'Male':1,'Female':0})
data['Race']=data['Race'].map({'White':5, 'Black':4, 'Asian':3, 'American Indian/Alaskan Native':2,'Other':1, 'Hispanic':0})
data['GenHealth']=data['GenHealth'].map({'Very good':4, 'Fair':3, 'Good':2, 'Poor':1, 'Excellent':0})
data.replace('80 or older','80-85',inplace=True)
data.replace('80 or older','80-85',inplace=True)

le = LabelEncoder()
data['Sex']=le.fit_transform(data['Sex'])
data['AgeCategory']=le.fit_transform(data['AgeCategory'])
data['Race']=le.fit_transform(data['Race'])
data['Diabetic']=le.fit_transform(data['Diabetic'])
data['GenHealth']=le.fit_transform(data['GenHealth'])


X=data.drop(['HeartDisease'],axis=1)
y=data['HeartDisease']

model=LogisticRegression(random_state=0)
model.fit(X,y)






image=Image.open('heart attack.jpeg')


def main():
    st.title("Heart disease predictions ")

    html_temp = """
    <div style ="background-color:Purple;padding:13px">
    <h1 style ="color:MediumSeaGreen;text-align:center;"> Check the house price prediction the below  ML App </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)


    st.image(image,caption='Check you have heart disease')


    BMI=st.slider("Enter body mass index",12.02,94.85)
    Smoking=st.selectbox("your Smoking status yes=1,or no=0",[1,0])
    AlcoholDrinking=st.selectbox("your alcoholdrinking status yes=1,or no=0",[1,0])
    Stroke=st.selectbox("your Stroke status yes=1,or no=0",[1,0])
    PhysicalHealth=st.slider("Enter PhysicalHealth",0.0,30.0,0.1)
    MentalHealth=st.slider("Enter MentalHealth",0.0,30.0,0.1)
    DiffWalking=st.selectbox("your DiffWalking status yes=1,or no=0",[1,0])
    Sex=st.selectbox("(1=Male,0=Female)",["1","0"])
    AgeCategory=st.selectbox("(55-59,80 or older, 65-69, 75-79, 40-44,70-74,60-64, 50-54, 45-49, 18-24, 35-39,30-34,25-29)",[ 7, 12, 9, 11, 4, 10,8,6,5,0,3,2,1])
    Race=st.selectbox("(White=5, Black=4, Asian=3, American Indian/Alaskan Native=2,Other=1, Hispanic=0)",[5,4,3,2,1,0])
    Diabetic=st.selectbox("your Diabetic status yes=1,or no=0",[1,0])
    PhysicalActivity=st.selectbox("your PhysicalActivity status yes=1,or no=0",[1,0])
    GenHealth=st.selectbox("(Very good=4, Fair=3, Good=2, Poor=1, Excellent=0)",[4,3,2,1,0])
    SleepTime=st.slider("Enter your sleeptime",1.0,24.0,1.0)
    Asthma=st.selectbox("your Asthma status yes=1,or no=0",[1,0])
    KidneyDisease=st.selectbox("your KidneyDiseas status yes=1,or no=0",[1,0])
    SkinCancer=st.selectbox("your SkinCancer status yes=1,or no=0",[1,0])
    

    
    if st.button("Predict"):
        result=model.predict([[BMI, Smoking, AlcoholDrinking, Stroke,
       PhysicalHealth, MentalHealth, DiffWalking, Sex, AgeCategory,
       Race, Diabetic, PhysicalActivity, GenHealth, SleepTime,
       Asthma, KidneyDisease, SkinCancer]])
    
        if (result[0]==0):
            st.success("The preson don't have heart disease")
        else:
            st.warning("The preson have heart disease")
    



if __name__=='__main__':
    main()

