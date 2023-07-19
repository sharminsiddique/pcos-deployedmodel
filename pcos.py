## import the necessary libraries 
import sys 
import numpy as np 
import streamlit as st 
import pandas as pd
from PIL import Image 
import pickle 

## load the trained model 
with open("pcos_model", "rb") as file:
    model = pickle.load(file)

## asking for input from users
def pcos_prediction(input):
    input_array = np.asarray(input)
    input_reshape = input_array.reshape(1,-1)
                                        
    prediction = model.predict(input_reshape)
    print(prediction)

    if(prediction[0]==0):
        return "It is likely you do not have PCOS"
    else:
        return "It is likely you have PCOS"

def main():
    st.set_page_config(page_title = "Predicting likelihood of PCOS", layout= "centered")

    ## add image
    #image = Image.open("pcos_image.jpg")
    #st.image(image, use_column_width = False)

    ## add a page title 
    st.write("Answer some questions about your health markers to obtain a PCOS prediction")

    ## variable input
    follicle_r = st.number_input("Please enter the amount of follicles on your right ovary", min_value = 0, step = 1)
    follicle_l = st.number_input("Please enter the amount of follicles on your left ovary", min_value = 0, step = 1)
    skin = st.number_input("Have you experienced any skin darkening especially at the folds of your skin? Yes|No - (Y = 1), (N = 0)", min_value = 0, step = 1)
    hair_g = st.number_input("Do you experience excessive hair growth (hirsutism)? Yes|No - (Y = 1), (N = 0)", min_value = 0, step = 1)
    weight_g = st.number_input("Have you experienced weight gain? Yes|No - (Y = 1), (N = 0)", min_value = 0, step = 1)
    cycle = st.number_input("Is your menstrual cycle regular or irregular? (R/I) - (R = 2), (I = 4)", min_value = 0, step = 1)
    fast_food = st.number_input("Do you consume fast food? Yes|No - (Y = 1), (N = 0)", min_value = 0, step = 1)
    pimples = st.number_input("Do you have pimples? Yes|No - (Y = 1), (N = 0)", min_value = 0, step = 1)
    hair_loss = st.number_input("Do you experience hair loss? Yes|No - (Y = 1), (N = 0)", min_value = 0, step = 1)
    amh_input = st.number_input("Please enter the amount of AMH (ng/mL) in your blood sample", min_value = 0, step = 1)
    weight_kg = st.number_input("Please enter how much you weigh in kg", min_value = 40, step = 1)
    bmi = st.number_input("Please enter your BMI", min_value = 0, step = 1)
    waist = st.number_input("Please enter the measurement of your waist in inches", min_value = 0, step = 1)
    hip = st.number_input("Please enter the measurement of your hip in inches", min_value = 0, step = 1)
    avg_f_size_l = st.number_input("Please enter the average size of the follicles on your left ovary (mm)", min_value = 0, step = 1)
    endometrium = st.number_input("Please enter the thickness of your endometrium (mm)", min_value = 0, step = 1)
    
    ## log transform amh_input
    log_amh = np.log10(amh_input)

    predict = ""

    ## streamlit button for prediction
    if st.button("Predict"):
        predict = pcos_prediction([follicle_r, follicle_l, skin, hair_g, weight_g, cycle, fast_food, pimples, hair_loss, log_amh, weight_kg, bmi, waist, hip, avg_f_size_l, endometrium])
    st.success(predict)
   
if __name__ == "__main__":
    main()

