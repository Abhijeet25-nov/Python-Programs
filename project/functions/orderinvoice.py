def generate_invoice(customer_name :str ="Guest", *items: str, **charges: float) :
    total=0.0
    invoice_lines = [f"Invoice for {customer_name}:"]
    if items:
        invoice_lines.append("Items:")
        for item in items:
            invoice_lines.append(f"- {item}")
    if charges:
        invoice_lines.append("Charges:")
        for label,amt in charges.items():
            invoice_lines.append(f"{label.capitalize()}: {amt}")
            total += amt
    
    invoice_lines.append(f"Total Amount Due: {total}")
    print("\\n".join(invoice_lines))
        
        
generate_invoice("Abhijeet","Paneer","Dal","Roti", tax=50.0, service=20.0, delivery=15.0)       