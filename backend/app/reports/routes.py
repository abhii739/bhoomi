from io import BytesIO
from flask import Blueprint, send_file, jsonify, request
from openpyxl import Workbook

reports_bp = Blueprint("reports", __name__)

@reports_bp.post("/excel")
def excel_report():
    data = request.get_json(silent=True) or {}
    wb = Workbook(); ws = wb.active; ws.title = "Land Assessment"
    ws.append(["BhoomiAI Land Assessment","Development export"])
    for key,value in data.items(): ws.append([str(key),str(value)])
    ws.append(["Data limitation","No unverified ownership or measured soil data should be treated as authoritative"])
    bio = BytesIO(); wb.save(bio); bio.seek(0)
    return send_file(bio, as_attachment=True, download_name="bhoomiai-land-assessment.xlsx", mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

@reports_bp.post("/pdf")
def pdf_report():
    data = request.get_json(silent=True) or {}
    try:
        from reportlab.pdfgen import canvas
        bio = BytesIO(); c = canvas.Canvas(bio); c.setTitle("BhoomiAI Land Assessment")
        c.drawString(40,800,"BhoomiAI — Land Assessment Report")
        y=770
        for key,value in data.items():
            c.drawString(40,y,f"{key}: {value}"); y-=22
            if y < 50: c.showPage(); y=800
        c.drawString(40,y,"Data limitation: verify ownership and measured soil conditions with authorized sources.")
        c.save(); bio.seek(0)
        return send_file(bio, as_attachment=True, download_name="bhoomiai-land-assessment.pdf", mimetype="application/pdf")
    except Exception as exc:
        return jsonify({"message":"PDF generation unavailable","detail":str(exc)}),503
