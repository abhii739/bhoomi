import pytest
from app import create_app

def test_land_endpoint():
    app=create_app(); app.config["TESTING"]=True
    with app.test_client() as client:
        response=client.get("/api/lands")
        assert response.status_code==200
        assert response.json["demo"] is True

def test_market_is_not_claimed_live():
    app=create_app(); app.config["TESTING"]=True
    with app.test_client() as client:
        response=client.get("/api/market/prices")
        assert response.status_code==200
        assert response.json["status"]=="not_configured"
