import re

n = int(input())
pattern = r"^@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+$"
for barcodes in range(n):
    barcode = input()
    if re.match(pattern, barcode):
        digits = re.findall(r"\d", barcode)
        if digits:
            product_group = "".join(digits)
        else:
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
