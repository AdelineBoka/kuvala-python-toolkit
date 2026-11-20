# Kuvala Logistics: reusable functions

def shipment_status(days):
    if days > 4:
        return "LATE"
    elif days == 4:
        return "at risk"
    else:
        return "on time"

def revenue(delivered_count, price):
    return delivered_count * price

print(shipment_status(2))
print(shipment_status(4))
print(shipment_status(9))

total = revenue(35, 18.50)
print(f"Revenue: {total} PLN")

def delivery_rate(delivered,total):
    return delivered / total * 100
rate = delivery_rate(35, 42)
print(f"Delivery rate: {rate:.1f}%")
