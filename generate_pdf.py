# generate_pdf.py
from fpdf import FPDF
import io

def create_pdf(electricity, fuel, travel, waste, carbon_score):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="Carbon Footprint Report", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt=f"Electricity usage: {electricity} kWh", ln=True)
    pdf.cell(200, 10, txt=f"Fuel consumption: {fuel} litres", ln=True)
    pdf.cell(200, 10, txt=f"Travel distance: {travel} km", ln=True)
    pdf.cell(200, 10, txt=f"Waste generated: {waste} kg", ln=True)
    pdf.ln(5)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt=f"Total Carbon Score: {carbon_score} tons CO₂", ln=True)
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt="Tips to reduce your carbon footprint:\n"
                              "- Switch to energy-efficient appliances.\n"
                              "- Reduce car usage.\n"
                              "- Recycle waste.\n"
                              "- Use public transport.\n"
                              "- Eat more plant-based foods.")

    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    return pdf_output.getvalue()