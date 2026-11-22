# Kuvala Logistics: all shipments in one list

def shipment_status(days):
    if days > 4:
        return "LATE"
    elif days == 4:
        return "at risk"
    else:
        return "on time"

shipments = [
    {"id": "KV-001", "city": "Krakow", "days": 5, "price": 18.50},
    {"id": "KV-002", "city": "Gdansk", "days": 2, "price": 22.00},
    {"id": "KV-003", "city": "Poznan", "days": 4, "price": 15.75},
    {"id": "KV-004", "city": "Wroclaw", "days": 7, "price": 30.00},
    {"id": "KV-005", "city": "Lodz", "days": 1, "price": 12.25},
]

late_count = 0
on_time_count = 0
total_value = 0
highest_price = 0
highest_id = ""

for s in shipments:
    status = shipment_status(s["days"])
    print(f"{s['id']} to {s['city']}: {s['days']} days, {status}")
    total_value = total_value + s["price"]
    if status == "LATE":
        late_count = late_count + 1
    if status == "on time":
        on_time_count = on_time_count + 1
    if s["price"] > highest_price:
        highest_price = s["price"]
        highest_id = s["id"]

print(f"Late shipments: {late_count}")
print(f"On time shipments: {on_time_count}")
print(f"Total value: {total_value} PLN")
print(f"Most expensive: {highest_id} at {highest_price} PLN")
