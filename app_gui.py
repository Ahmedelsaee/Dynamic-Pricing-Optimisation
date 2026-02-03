import streamlit as st
import requests

st.set_page_config(page_title='Dynamic Pricing Optimisation',layout='centered')
st.title('Dynamic Pricing Optimisation App')
st.write('Enter Details below to predict optimal price')

def reset_form():
    st.session_state.number_of_riders = 0
    st.session_state.number_of_drivers = 0
    st.session_state.location_category = 'Rural'
    st.session_state.customer_loyalty_status = 'Regular'
    st.session_state.number_of_past_rides = 0
    st.session_state.average_ratings = 0.0
    st.session_state.time_of_booking = 'Morning'
    st.session_state.vechile_type = 'Economy'
    st.session_state.expected_ride_duration = 0
    st.session_state.historical_cost_of_ride = 0.0
if 'number_of_riders' not in st.session_state:
    reset_form()

    
with st.form(key='dynamic_pricing_form'):
    number_of_riders=st.number_input('Enter Number Of Riders',min_value=0,value=st.session_state.number_of_riders,step=1)
    number_of_drivers=st.number_input('Enter Number Of Drivers',min_value=0,value=st.session_state.number_of_drivers,step=1)
    location_category=st.selectbox('Select Location Category',['Rural','Suburban','Urban'],index=['Rural','Suburban','Urban'].index(st.session_state.location_category))
    customer_loyalty_status=st.selectbox('Select Customer Loyalty Status',['Regular','Silver','Gold'],index=['Regular','Silver','Gold'].index(st.session_state.customer_loyalty_status))
    number_of_past_rides=st.number_input('Enter Number Of Past Riders',min_value=0,value=st.session_state.number_of_past_rides,step=1)
    average_ratings=st.number_input('Enter Average Rating',min_value=0.0,value=st.session_state.average_ratings,step=0.1,format="%.1f")
    time_of_booking=st.selectbox('Select Time Of Booking',['Morning','Afternoon','Evening','Night'],index=['Morning','Afternoon','Evening','Night'].index(st.session_state.time_of_booking))
    vechile_type=st.selectbox('Select Vehicle Type',['Economy','Premium'],index=['Economy','Premium'].index(st.session_state.vechile_type))
    expected_ride_duration=st.number_input('Enter Expected Ride Duration (in minutes)',min_value=0,value=st.session_state.expected_ride_duration,step=1)
    historical_cost_of_ride=st.number_input('Enter Historical Cost Of Ride',min_value=0.0,value=st.session_state.historical_cost_of_ride,step=0.1,format="%.2f")
    
    col1,col2=st.columns(2)
    submit_button=col1.form_submit_button(label='Predict',use_container_width=True)
    reset_button=col2.form_submit_button(label='Reset',use_container_width=True)

if submit_button:
    input_data={
        "features":{
            "Number_of_Riders":number_of_riders,
            "Number_of_Drivers":number_of_drivers,
            "Location_Category":location_category,
            "Customer_Loyalty_Status":customer_loyalty_status,
            "Number_of_Past_Rides":number_of_past_rides,
            "Average_Ratings":average_ratings,
            "Time_of_Booking":time_of_booking,
            "Vehicle_Type":vechile_type,
            "Expected_Ride_Duration":expected_ride_duration,
            "Historical_Cost_of_Ride":historical_cost_of_ride
        }
    } 

    try:
        response=requests.post('http://127.0.0.1:5000/predict',json=input_data)
        if response.status_code==200:
            result=response.json()
            prediction=result.get('prediction_1',None)
            if prediction is not None:
                st.success(f"The predicted optimal price is: {prediction:.2f}")
            else:
                st.error("Prediction not returned from API")
        else:
            st.error("Error in API request")
    except Exception as e:
        st.error(f"An error occurred: {e}")                