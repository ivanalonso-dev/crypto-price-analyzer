datos = []

for i in range(5):
    cryptoname = input("Enter crypto name: ")
    cryptovalue = float(input("Enter price: "))

    crypto = {  "name" : cryptoname, "price" : cryptovalue }
    datos.append(crypto)

precios = []

for c in datos:
    precios.append(c["price"])

average = sum(precios) / len(precios)
maximun = max(crypto)
minimun = min(crypto)

for c in  datos:
    if c["price"] == maximun:
        max_crypto = c["name"]
    if c["price"] == minimun:
        min_crypto = c["name"]

print("\n--- RESULTS ---")

for c in datos:
    print(f"{c['name']} -> {c['price']}")

print(f"\nAverage price: {average}")
print(f"Highest price: {maximun} ({max_crypto})")
print(f"Lowest price: {minimun} ({min_crypto})")

import json

with open("datos.json", "w") as archivo:
    json.dump(datos, archivo)

with open("datos.json", "r") as archivo:
    datos_leidos = json.load(archivo)