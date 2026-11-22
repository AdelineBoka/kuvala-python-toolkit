# Kuvala Logistics: shipment records

shipment = {
    "id": "KV-001",
    "city": "Krakow",
    "days": 5,
    "delivered": False,
}

print(shipment["id"])
print(shipment["city"])
print(f"{shipment['id']} has been in transit {shipment['days']} days")

shipment["delivered"] = True
print("Delivered:", shipment["delivered"])

shipment["weight_kg"] = 12.5
print(shipment)

shipment2 = {
    "id": "KV-002",
    "city": "Gdansk",
    "days": 2,
    "delivered": True,
}

print(f"{shipment2['id']} to {shipment2['city']}: {shipment2['days']} days")

shipment2["days"] = 6
print(shipment2)
