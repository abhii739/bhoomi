from flask import Blueprint, jsonify, request
import os, requests

soil_bp = Blueprint("soil", __name__)

@soil_bp.get("/<land_id>")
def soil_detail(land_id):
    lat = float(request.args.get("lat", 12.9716)); lon = float(request.args.get("lon", 77.5946))
    weather = None
    try:
        base = os.getenv("OPEN_METEO_BASE_URL", "https://api.open-meteo.com/v1")
        r = requests.get(f"{base}/forecast", params={"latitude":lat,"longitude":lon,"current":"temperature_2m,relative_humidity_2m,rain,wind_speed_10m","daily":"temperature_2m_max,temperature_2m_min,precipitation_sum","timezone":"Asia/Kolkata"}, timeout=8)
        r.raise_for_status(); weather = r.json()
        status = "live"
    except Exception as exc:
        weather = {"error":str(exc)}; status = "unavailable"
    return jsonify({"land_id":land_id,"measurements":{"ph":None,"moisture":None,"soil_type":"Not measured","nitrogen":None,"phosphorus":None,"potassium":None,"organic_carbon":None},"is_estimated":True,"source":"No government soil observation is configured","weather":weather,"weather_status":status,"suitability_score":None,"limitations":["Measured soil values are not yet available","Weather is available only when Open-Meteo responds"]})
