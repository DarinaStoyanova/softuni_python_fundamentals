import re
pattern_valid_code = r"@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+"
pattern_group_number = r"\d+"
counter = int(input())

while counter > 0:
    counter -= 1
    barcode = input()
    valid_barcode = re.findall(pattern_valid_code, barcode)
    if valid_barcode:
        product_group = re.findall(pattern_group_number, barcode)
        if not product_group:
            product_group = "00"
        else:
            product_group = "".join(product_group)
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")