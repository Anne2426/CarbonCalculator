import streamlit as st
from generate_pdf import create_pdf_report
import os

def calculate_emissions(electricity_kwh, diesel_liters, distance_km, material_kg):
    factors = {
        'electricity': 0.82,
        'diesel': 2.68,
        'transport': 0.12,
        'material': 1.5
    }
    return round(
        electricity_kwh * factors['electricity']
        + diesel_liters * factors['diesel']
        + distance_km * factors['transport']
        + material_kg * factors['material'], 2
    )

st.set_page_config(page_title="Carbon Footprint Calculator", layout="centered")
st.title("🌿Carbon Footprint Calculator")

electricity = st.number_input("Electricity Used (kWh)", min_value=0.0)
diesel = st.number_input("Diesel Used (liters)", min_value=0.0)
distance = st.number_input("Travel Distance (km)", min_value=0.0)
material = st.number_input("Materials Used (kg)", min_value=0.0)

if st.button("Calculate CO₂ Emissions"):
    emissions = calculate_emissions(electricity, diesel, distance, material)
    st.success(f"🌍 Estimated Carbon Emissions: {emissions} kg CO₂")

    data = {
        'electricity': electricity,
        'diesel': diesel,
        'distance': distance,
        'material': material,
        'emissions': emissions
    }

    pdf_filename = "report.pdf"
    create_pdf_report(data, pdf_filename)

    with open(pdf_filename, "rb") as file:
        st.download_button(
            label="📄 Download PDF Report",
            data=file,
            file_name="Carbon_Footprint_Report.pdf",
            mime="application/pdf"
        )

    os.remove(pdf_filename)