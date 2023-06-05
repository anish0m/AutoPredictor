import numpy as np
import streamlit as st
import joblib

xgb_model = joblib.load('F:/Sixth_Semester/AutoPredictor/xgb_model.pkl')
scaler = joblib.load('F:/Sixth_Semester/AutoPredictor/scaler.pkl')

fuel_type_mapping = {'Petrol': 0, 'Diesel': 1, 'Hybrid': 2, 'Electric': 3, 'Other': 4}

fuel_type_mapping_inverse = {v: k for k, v in fuel_type_mapping.items()}

def car_price_prediction(input_data):
	input_changed = np.array(input_data).reshape(1, -1)

	fuel_type = input_changed[0, 3]
	fuel_type_numeric = fuel_type_mapping.get(fuel_type, -1)

	if fuel_type_numeric == -1:
		return "Invalid fuel type. Please choose from the available options."

	input_changed[0,3] = fuel_type_numeric

	std_input = scaler.transform(input_changed)
	prediction = xgb_model.predict(std_input)

	return "Estimated car price : " + str(prediction[0])

def main():
	st.title('Car price detector by the Ultimate Buds')

	year = st.text_input('Year')
	transmission = st.text_input('Transmission')
	mileage = st.text_input('Mileage')
	fuel_type = st.selectbox('Fuel-type', ('Petrol', 'Diesel', 'Hybrid', 'Electric', 'Other'))
	tax = st.text_input('Tax')
	mpg = st.text_input('MPG')
	enginesize = st.text_input('Engine size')

	pred_price = ""

	if st.button('Check estimated price'):
		fuel_type_numeric = fuel_type_mapping[fuel_type]
		pred_price = car_price_prediction([year, transmission, mileage, fuel_type, tax, mpg, enginesize])

	st.success(pred_price)

if __name__ == '__main__':
	main()