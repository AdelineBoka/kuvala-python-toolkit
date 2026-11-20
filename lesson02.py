# Kuvala Logistics: shipment list

shipments = ["KV-001", "KV-002", "KV-003", "KV-004", "KV-005"]

print("Total shipments:", len(shipments))
print("First shipment:", shipments[0])
print("Last shipment:", shipments[-1])

print("--- All shipments ---")
for shipment in shipments:
    print(f"Processing {shipment}")

shipments.append("KV-006")
print("Total shipments:", len(shipments))

delivered_ids =["KV-001", "KV-003", "KV-005"]
for delivered in delivered_ids:
    print(f"{delivered} delivered")
