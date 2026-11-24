from flask import Blueprint, jsonify, request

land_bp = Blueprint("land", __name__)

PARCELS = [
 {"id":"BLR-001","land_id":"BLR-001","survey_number":"42/1","taluk":"Yelahanka","hobli":"Yelahanka","village":"Chikkajala","panchayat":"Chikkajala","latitude":13.1074,"longitude":77.6250,"area_acres":18.6,"area_hectares":7.53,"classification":"Government-owned unused land","ownership_category":"State Government","utilization_status":"Unused","source":"Development seed record — official verification required","verification_status":"pending","demo":True,"geometry":[[13.111,77.620],[13.111,77.630],[13.103,77.630],[13.103,77.620]]},
 {"id":"BLR-002","land_id":"BLR-002","survey_number":"88/3","taluk":"Anekal","hobli":"Anekal","village":"Sarjapura","panchayat":"Sarjapura","latitude":12.9086,"longitude":77.7962,"area_acres":12.4,"area_hectares":5.02,"classification":"Barren land","ownership_category":"State Government","utilization_status":"Unused","source":"Development seed record — official verification required","verification_status":"pending","demo":True,"geometry":[[12.912,77.792],[12.912,77.800],[12.905,77.800],[12.905,77.792]]},
 {"id":"BLR-003","land_id":"BLR-003","survey_number":"15/2","taluk":"Bengaluru South","hobli":"Begur","village":"Gottigere","panchayat":"Gottigere","latitude":12.8592,"longitude":77.5760,"area_acres":9.8,"area_hectares":3.97,"classification":"Agricultural land","ownership_category":"Government lease","utilization_status":"Underutilized","source":"Development seed record — official verification required","verification_status":"pending","demo":True,"geometry":[[12.863,77.572],[12.863,77.580],[12.855,77.580],[12.855,77.572]]}
]

@land_bp.get("")
def land_list():
    classification = request.args.get("classification")
    rows = PARCELS
    if classification:
        rows = [r for r in rows if r["classification"] == classification]
    return jsonify({"items":rows,"count":len(rows),"area_acres":sum(r["area_acres"] for r in rows),"demo":True,"source":"Development seed data; not authoritative land ownership data"})

@land_bp.get("/<land_id>")
def land_detail(land_id):
    row = next((r for r in PARCELS if r["land_id"] == land_id), None)
    return jsonify(row) if row else (jsonify({"message":"Land parcel not found"}),404)
