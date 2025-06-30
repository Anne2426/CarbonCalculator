import streamlit as st
import pandas as pd
from generate_pdf import generate_pdf_report

# ✅ Set up page config (title and icon)
st.set_page_config(
    page_title="Carbon Footprint Calculator",
    page_icon="carbon_icon.png"
)

st.title("🌍 Carbon Footprint Calculator")

st.write("Estimate your carbon footprint and get tips to reduce it.")

# --- User Inputs ---
electricity = st.number_input("Monthly Electricity Use (kWh)", min_value=0.0, step=0.1)
fuel = st.number_input("Monthly Fuel Consumption (litres)", min_value=0.0, step=0.1)
waste = st.number_input("Monthly Waste Produced (kg)", min_value=0.0, step=0.1)
travel = st.number_input("Monthly Travel Distance (km)", min_value=0.0, step=0.1)

# --- Emission Factors (per unit) ---
ELECTRICITY_CO2 = 0.85  # kg CO2 per kWh
FUEL_CO2 = 2.31         # kg CO2 per litre
WASTE_CO2 = 0.57        # kg CO2 per kg
TRAVEL_CO2 = 0.21       # kg CO2 per km

# --- Calculate Footprint ---
if st.button("Calculate"):
    total_emissions = (
        electricity * ELECTRICITY_CO2 +
        fuel * FUEL_CO2 +
        waste * WASTE_CO2 +
        travel * TRAVEL_CO2
    )

    st.subheader("📊 Your Estimated Monthly Carbon Footprint:")
    st.success(f"*{total_emissions:.2f} kg CO₂*")

    # --- Green Tips ---
    st.subheader("🌱 Tips to Reduce Your Footprint:")
    st.markdown("- Use energy-efficient appliances")
    st.markdown("- Reduce unnecessary travel")
    st.markdown("- Recycle and compost waste")
    st.markdown("- Consider renewable energy")

    # --- Export to PDF ---
    if st.button("Download PDF Report"):
        pdf_file = generate_pdf_report(electricity, fuel, waste, travel, total_emissions)
        st.download_button(
            label="📄 Download Report",
            data=pdf_file,
            file_name="carbon_footprint_report.pdf",
            mime="application/pdf"
        )