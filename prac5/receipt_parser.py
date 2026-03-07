import re
import json

data = {
    "date": "2026-03-06 13:22",
    "products": [
    {"name": "Milk", "price": 250.00},
    {"name": "Bread", "price": 250.00},
    {"name": "Chocolate", "price": 250.00}
    ],
    "total": 750.00,
    "payment": "Card"
}
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()
print(text)