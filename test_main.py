import pytest
from fastapi.testclient import TestClient
from main import app, calculate_total_stock

client = TestClient(app)

# Unit Test untuk fungsi kalkulasi stok
def test_calculate_total_stock():
    sample_items = [{"quantity": 10}, {"quantity": 20}]
    assert calculate_total_stock(sample_items) == 30

# Integration Test untuk Endpoint API
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["service"] == "TechNova Inventory"

def test_add_and_get_inventory():
    payload = {"id": 1, "name": "Laptop ThinkPad", "quantity": 5, "price": 15000000.0}
    res_post = client.post("/api/v1/inventory", json=payload)
    assert res_post.status_code == 201
    
    res_get = client.get("/api/v1/inventory")
    assert res_get.status_code == 200
    assert res_get.json()["total_items"] == 1