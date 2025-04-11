import streamlit as st
from converter import length_converter, weight_converter


st.set_page_config(page_title="Unit Converter", layout="centered")
st.title("Unit Converter")

conversion_type = st.selectbox("Select conversion type", ["Length", "Weight"])

if conversion_type == "Length":
    units = ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"]
    convert_function = length_converter
else:
    units = ["kilogram", "gram", "milligram", "pound", "ounce"]
    convert_function = weight_converter


col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    value = st.number_input("Enter value", min_value=0.0, format="%.4f")
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)

    if st.button("Convert"):
        result = convert_function(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

st.markdown(
    "<h6 style='text-align: center;'>Made with by <strong>Ammad Ali</strong></h6>",
    unsafe_allow_html=True
)

