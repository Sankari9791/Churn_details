# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 17:27:27 2025

@author: sanka
"""

#import numpy as np
#import pickle
#import streamlit as st

#how we can load this model and how we can use it.
#loaded_model=pickle.load(open("C:/Users/sanka/Desktop/internship_twilearn_ projects/deployment process/trained_model.sav",'rb'))


#create a function for prediction
#def Customer_churn_prediction(input_data):
    
    #predict the loaded model
 #   input_data=(0,0,0,2,0,1,53.85,108.15)

    #convert into numpy array
  #  input_data_as_numpy_array=np.asarray(input_data)
    #reshape the data
   # input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    #prediction=loaded_model.predict(input_data_reshaped)
    #print(prediction)

    #if (prediction[0]==0):
     #  return "The customer has Churned"
    #else:
     #   return "The customer hasn't Churned"
#we need to change return insteadof print and remove parenthesis.copy 
#the same datas loaded pickle and input data predictive details


#nest we move to bulit the part to create web app by streamlit






#def main():    
    
    
    #giving a title for a web page
#    st.title('Customer Churn Prediction Web App')
    
    #create to users getting some input values from users
    
   # SeniorCitizen= st.text_input("category of citizens")
   # Partner=st.text_input("number of partners ")
    #Dependents=st.text_input("number of dependents")
    #tenure=st.text_input("tenure details")
    #Contract=st.text_input("category of citizens")
    #PaperlessBilling=st.text_input("billing details")
    #MonthlyCharges=st.text_input("category of charging")
    #TotalCharges=st.text_input("total amount")
    
    #code for prediction
    #Analysis_of_Customer_churn =' '
    
    #we were doing all the process before that like giving the input data and 
    #make prediction all those things laterly stored in aanlysis of sona data. 
    #that is why er have created the null string which means it has null values in the ' '
    
    
    #whe create the button for prediction
  #  if st.button('Customer Churn'):
   #    Analysis_of_Customer_churn = Customer_churn_prediction([SeniorCitizen,Partner, Dependents,	tenure,	Contract,	PaperlessBilling,	MonthlyCharges,	TotalCharges]) 
    
    
    
    
    
   # if __name__ =='__main__':
    #    main()
    
    
    
    
import streamlit as st
import numpy as np
import pickle

# Load the trained model
loaded_model = pickle.load(open("trained_model.sav", 'rb'))

# Set up Streamlit interface
st.title("Customer Churn Prediction")
st.markdown("This is a customer churn prediction app.")

# Input fields for the user
st.subheader("Enter customer details:")

dependents = st.selectbox("Dependents (0 = No, 1 = Yes)", [0, 1])
contract = st.selectbox("Contract Type (0 = Month-to-month, 1 = One year, 2 = Two year)", [0, 1, 2])
paperless_billing = st.selectbox("Paperless Billing (0 = No, 1 = Yes)", [0, 1])
partner = st.selectbox("Partner (0 = No, 1 = Yes)", [0, 1])
tenure = st.slider("Tenure (Months)", 0, 72, 1)
monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, step=0.01)
total_charges = st.number_input("Total Charges ($)", min_value=0.0, step=0.01)

# Input data as a tuple
input_data = (dependents, contract, paperless_billing, partner, tenure, monthly_charges, total_charges)

# Convert input to numpy array and reshape for prediction
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

# Initialize the prediction variable
prediction =' '


# Predict the churn
if st.button('Predict'):
    prediction = loaded_model.predict(input_data_reshaped)
    
if prediction[0] == 1:
   st.write("The customer has Churned.")
else:
   st.write("The customer hasn't Churned.")
