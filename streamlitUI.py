import streamlit as st
import numpy as np
import pickle


with open('logistic_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

def predict_property_damage(features):
    return model.predict([features])

def main():
    st.title("Austin Bicycle Accident Property Damage High-Low Prediction")
    
    
    st.write("""
        Based on about 2,500 bike crash records from Austin, this program uses a logistic regression model to predict the level of property damage caused by traffic accidents, and predict whether the property damage will be higher than $1,000.
    """)
    
    
    st.image('bikepic.jpg', caption='Image Caption')

    st.title("Top factors associated with bike crashes in Austin")
    
    st.write("""
        According to the comparison between EDA and the three models, among the 12 features, "Traffic Control Type" and "Speed Limit" are the two main causes of bicycle accidents.
    """)
    
    st.image('trafficControl.png', caption='Distribution of the number of accidents by traffic control type')

    
    st.image('speedLimit.png', caption='Distribution of the number of accidents by speed Limit')

    st.title("Logistic regression model prediction, accuracy 73%")
    
    
    active_school_zone_flag = st.selectbox('Active School Zone Flag', options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    at_intersection_flag = st.selectbox('At Intersection Flag', options=[0, 1], format_func=lambda x: "False" if x == 0 else "True")
    construction_zone_flag = st.selectbox('Construction Zone Flag', options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    crash_severity = st.selectbox('Crash Severity', options=range(5), format_func=lambda x: ["Incapacitating Injury", "Killed", "Non-Incapacitating Injury", "Not Injured", "Possible Injury"][x])
    intersection_related = st.selectbox('Intersection Related', options=range(5), format_func=lambda x: ["Driveway Access", "Intersection", "Intersection Related", "Non Intersection", "Not Reported"][x])
    roadway_part = st.selectbox('Roadway Part', options=range(4), format_func=lambda x: ["Entrance/On Ramp", "Main/Proper Lane", "Other (Explain In Narrative)", "Service/Frontage Road"][x])
    surface_condition = st.selectbox('Surface Condition', options=range(7), format_func=lambda x: ["Dry", "Ice", "Other (Explain In Narrative)", "Sand, Mud, Dirt", "Standing Water", "Unknown", "Wet"][x])
    traffic_control_type = st.selectbox('Traffic Control Type', options=range(16), format_func=lambda x: ["Bike Lane", "Center Stripe/Divider", "Crosswalk", "Flagman", "Flashing Red Light", "Flashing Yellow Light", "Marked Lanes", "No Passing Zone", "Officer", "Other (Explain In Narrative)", "Signal Light", "Signal Light With Red Light Running Camera", "Stop Sign", "Warning Sign", "Yield Sign", "no data"][x])
    person_helmet = st.selectbox('Person Helmet', options=range(5), format_func=lambda x: ["Not Worn", "Unknown If Worn", "Worn, Damaged", "Worn, Not Damaged", "Worn, Unk Damage"][x])
    crash_total_injury_count = st.number_input('Crash Total Injury Count', min_value=0, value=0, step=1)
    speed_limit = st.number_input('Speed Limit', min_value=0, value=0, step=1)

   
    
    
    if st.button('Predict'):
        features = [active_school_zone_flag, at_intersection_flag, construction_zone_flag, crash_severity, crash_total_injury_count, intersection_related, roadway_part, speed_limit, surface_condition, traffic_control_type, person_helmet]
        prediction = predict_property_damage(features)
        result = "Greater chance of property damage exceeding $1,000" if prediction[0] == 1 else "Greater chance of property damage less than $1,000"
        
        
        st.markdown(f"<h3 style='color: black;font-size: 24px'>Prediction:</h3>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='color: black;font-size: 24px'>$1000 Damage to Any One Person's Property:</h3>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='color: red;font-size: 30px'>{result}</h3>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
    