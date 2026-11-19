# Kuvala Logistics: daily shipment summary

warehouse = "Krakow Hub"
shipments_today = 42
delivered = 35
price_per_shipment = 18.50

# Math with numbers
pending = shipments_today - delivered
revenue = delivered * price_per_shipment
delivery_rate = delivered / shipments_today * 100

# Strings and f-strings
print(f"Warehouse: {warehouse}")
print(f"Total shipments: {shipments_today}")
print(f"Pending: {pending}")
print(f"Revenue: {revenue} PLN")
print(f"Delivery rate: {delivery_rate:.1f}%")

cancelled=3
cancellation_rate = cancelled / shipments_today * 100
print(f"cancellation rate: {cancellation_rate:.1f}%")
