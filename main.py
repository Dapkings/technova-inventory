from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="TechNova Inventory API")

# Mengaktifkan endpoint /metrics untuk Prometheus
Instrumentator().instrument(app).expose(app)

# Database sederhana di memory
inventory_db = []

class Item(BaseModel):
    id: int
    name: str
    quantity: int
    price: float

def calculate_total_stock(items: list) -> int:
    return sum(item["quantity"] for item in items)

@app.get("/")
def read_root():
    return {"status": "online", "service": "TechNova Inventory"}

@app.get("/api/v1/inventory")
def get_inventory():
    return {"data": inventory_db, "total_items": len(inventory_db)}

@app.post("/api/v1/inventory", status_code=201)
def add_item(item: Item):
    item_dict = item.model_dump()
    inventory_db.append(item_dict)
    return item_dict