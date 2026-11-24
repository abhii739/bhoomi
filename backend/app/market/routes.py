from flask import Blueprint, jsonify, request

market_bp = Blueprint("market", __name__)

@market_bp.get("/prices")
def prices():
    return jsonify({"items":[],"count":0,"status":"not_configured","source":"AGMARKNET/eNAM integration required","message":"No market prices are claimed as live or measured without an authorized data integration","updated_at":None})

@market_bp.get("/employment")
def employment():
    area = float(request.args.get("area_acres", 10))
    return jsonify({"area_acres":area,"estimated_person_days":round(area*40),"method":"Development estimate: 40 person-days per acre for a representative cultivation cycle","uncertainty":"Indicative only — not measured workforce demand","employment_status":"estimated","demo":True})
