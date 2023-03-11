import streamlit as st

bmi_result = ''
col1, col2, col3 = st.columns(3)


def calculate_bmi():
    """ Calculate the BMI using weight and height user inputs. """

    try:
        if weight_unit == 'Kgrams':
            weight = float(weight_entry)
        elif weight_unit == 'Pounds':
            weight = float(weight_entry) / 2.20462
        elif weight_unit == 'Stones':
            weight = float(weight_entry) * 14 / 2.20462
    except ValueError as e:
        return

    try:
        if height_unit == 'Inches':
            height = float(height_entry) * 2.54
        elif height_unit == 'Centimeters':
            height = float(height_entry)
    except ValueError as e:
        return

    bmi = weight / ((height/100) ** 2)
    msg = ''
    if int(bmi) < 18.5:
        msg = 'Underweight'
    if int(bmi) >= 18.5 and int(bmi) <= 24.9:
        msg = 'Healthy'
    if int(bmi) > 24.9 and int(bmi) <= 29.9:
        msg = 'Overweight'
    if int(bmi) > 29.9 and int(bmi) <= 39.9:
        msg = 'Obese'
    if int(bmi) >= 40:
        msg = 'Severely Obese'

    bmi_result = f'\nYour BMI is: {bmi:.2f}\n\n' + str(msg)

    return bmi_result

with st.columns(3)[1]:
     st.image('bmi2.jpg')

st.subheader('Enter your weight')
weight_entry = st.text_input('Weight')
weight_unit = st.radio('Unit', ('Kgrams', 'Pounds', 'Stones'))

st.subheader('Enter your height')
height_entry = st.text_input('Height')
height_unit = st.radio('Unit', ('Inches', 'Centimeters'))

if st.button('Calculate'):
    bmi_result = calculate_bmi()
    st.write(bmi_result)
