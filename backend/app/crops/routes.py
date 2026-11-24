from flask import Blueprint, jsonify, request

crops_bp = Blueprint("crops", __name__)

CROP_GUIDANCE = {
 "Millet":{"score":82,"duration":90,"yield":"2–3 t/ha (indicative range only)","reason":"Generally drought tolerant and suitable to variable rainfall when local soil and climate validate suitability."},
 "Groundnut":{"score":78,"duration":120,"yield":"1.5–3 t/ha (indicative range only)","reason":"Suitable for well-drained soils; verify pH, nutrients and rainfall before cultivation."},
 "Pigeon pea":{"score":76,"duration":150,"yield":"0.8–1.5 t/ha (indicative range only)","reason":"Potentially suitable as a hardy pulse crop; local growing conditions must be confirmed."},
 "Fodder maize":{"score":73,"duration":75,"yield":"Varies widely by management and irrigation","reason":"Short-duration option subject to verified soil fertility and dependable water availability."}
}

@crops_bp.get("/recommendations")
def recommendations():
    land_id = request.args.get("land_id", "BLR-001")
    rows = [{"crop":name,**data,"limitations":"Illustrative recommendation; no measured soil observation or validated yield model is used"} for name,data in CROP_GUIDANCE.items()]
    return jsonify({"land_id":land_id,"model":"Explainable rule-based development model","confidence":"low","recommendations":rows,"data_status":"Measured soil and official suitability data not available","demo":True})
