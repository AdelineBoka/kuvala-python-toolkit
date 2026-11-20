# Kuvala Logistics: flag late shipments

shipment_days = [1, 2, 5, 3, 7, 2, 6, 1]
late_count = 0
for days in shipment_days:
    if days > 4:
        print(f"{days} days: LATE")
        late_count = late_count +1
    elif days == 4:
        print(f"{days} days: at risk")
    else:
        print(f"{days} days: on time")
print(f"Late shipments: {late_count}")
