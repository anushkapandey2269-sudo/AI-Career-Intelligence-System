from fpdf import FPDF

def generate_report(name, email, phone, role, score, match):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="ResumeMind AI Report", ln=True, align="C")

    pdf.set_font("Arial", size=12)
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Email: {email}", ln=True)
    pdf.cell(200, 10, txt=f"Phone: {phone}", ln=True)
    pdf.cell(200, 10, txt=f"Predicted Role: {role}", ln=True)
    pdf.cell(200, 10, txt=f"Resume Score: {score}", ln=True)
    pdf.cell(200, 10, txt=f"Job Match: {match}", ln=True)

    file_name = "resume_report.pdf"
    pdf.output(file_name)

    return file_names