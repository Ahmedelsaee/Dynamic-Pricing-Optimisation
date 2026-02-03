# Dynamic Pricing Optimization System

A complete **Machine Learning project** for predicting optimal ride prices using demand, supply, customer behavior, and contextual features.  
The system includes **model training**, **Flask API**, and an interactive **Streamlit web app**.

---

## Project Overview

Dynamic pricing is widely used in ride-hailing platforms to adjust prices based on real-time factors such as demand, supply, location, and time.  
This project predicts the **optimal ride price** using a trained ML regression model and provides an end-to-end deployment pipeline.

---
## Feature Engineering for Dynamic Pricing

- Demand Multiplier: Adjusts price based on rider demand. High demand (above 75th percentile) increases price by 30%, low demand (below 25th percentile) reduces it by 15%.
- Supply Multiplier: Adjusts price based on driver availability. Low supply (below 25th percentile) increases price by 25%, high supply (above 75th percentile) reduces it by 10%.
- Adjusted Price: Final price = Historical_Cost_of_Ride * Demand_Multiplier * Supply_Multiplier, reflecting real-world demand-supply dynamics.

---

### Features:

- Number_of_Riders  
- Number_of_Drivers  
- Location_Category (One-Hot Encoded)  
- Customer_Loyalty_Status  
- Number_of_Past_Rides  
- Average_Ratings  
- Time_of_Booking  
- Vehicle_Type  
- Expected_Ride_Duration  
- Historical_Cost_of_Ride  

---

## Data Preprocessing

- Mapping for ordinal features:
  - Customer_Loyalty_Status
  - Time_of_Booking
  - Vehicle_Type
- One-Hot Encoding for:
  - Location_Category
- Feature alignment using saved `model_features.pkl` to avoid feature mismatch errors.

---

## Tech Stack

- **Python**
- **Pandas & NumPy**
- **Scikit-learn**
- **XGBoost**
- **Joblib** (Model Deployment)
- **Flask** (REST API)
- **Streamlit** (Frontend UI)

---

## Machine Learning Model Details

- **Problem Type:** Regression  
- **Model Used:** XGBoost Regressor  
- **Target:** Adjusted Price
- **Training R^2 Score:** ~ 99.9%
- **Training R^2 Score:** ~ 99.3%
- **Mean Squared Error (MSE):** ~ 288.2
- **Mean Absolute Error (MAE):** ~ 10.1