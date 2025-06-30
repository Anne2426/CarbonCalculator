from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def create_pdf_report(data, filename="report.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, 800, "MSME Carbon Footprint Report")

    c.setFont("Helvetica", 12)
    c.drawString(50, 760, f"Electricity Used: {data['electricity']} kWh")
    c.drawString(50, 740, f"Diesel Used: {data['diesel']} liters")
    c.drawString(50, 720, f"Travel Distance: {data['distance']} km")
    c.drawString(50, 700, f"Materials Used: {data['material']} kg")
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 660, f"Total Emissions: {data['emissions']} kg CO₂")

    c.setFont("Helvetica", 10)
    c.drawString(50, 620, "Thank you for using the Carbon Footprint Calculator.")
    c.save()