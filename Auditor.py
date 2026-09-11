total_inventory = 0
failed_entries = 0
overstock_limit = 500

print("=== Smart Inventory Auditor ===")
print("Enter stock quantities to add to inventory.")
print("Type 'quit' to stop and see the report.\n")

while True:
    user_input = input("Enter stock quantity: ").strip()

    if user_input.lower() == "quit":
        break

    if not user_input.isdigit():
        print(f"Error: '{user_input}' is not a valid number. Please enter a whole number.\n")
        failed_entries += 1
        continue

    quantity = int(user_input)

    if quantity < 0:
        print("Error: Negative quantities are not allowed.\n")
        failed_entries += 1
        continue
    else:
        total_inventory += quantity
        print(f"Accepted: +{quantity} units. Running total: {total_inventory}\n")

    if total_inventory > overstock_limit:
        print(f"OVERSTOCK ALERT: Inventory total ({total_inventory}) exceeds the "
              f"{overstock_limit}-unit storage capacity!")
        print("Halting intake immediately.\n")
        break

print("=== End of Session Report ===")
print(f"Total Units Processed: {total_inventory}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")
