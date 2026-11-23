# Kuvala Logistics: read shipments from a file
import csv

def shipment_status(days):
    if days > 4:
        return "LATE"
    elif days == 4:
        return "at risk"
    else:
        return "on time"

shipments = []

with open("shipments.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["days"] = int(row["days"])
        row["price"] = float(row["price"])
        shipments.append(row)

late_count = 0
total_value = 0

for s in shipments:
    status = shipment_status(s["days"])
    print(f"{s['id']} to {s['city']}: {s['days']} days, {status}")
    total_value = total_value + s["price"]
    if status == "LATE":
        late_count = late_count + 1

print(f"Shipments loaded: {len(shipments)}")
print(f"Late shipments: {late_count}")
print(f"Total value: {total_value} PLN")

print("--- Late shipments ---")
for s in shipments:
    if shipment_status(s["days"]) == "LATE":
        print(f"LATE: {s['id']} ({s['city']})")
