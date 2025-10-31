import pandas as pd

dataFile = pd.read_csv("figuras.csv")
print("Procesando Figuras ...\n")


areas = []
perimetros = []

for index, row in dataFile.iterrows():
	print(f"Fila {index}: FIGURA={row['FIGURA']}, Medida1={row['MEDIDA1']}, Medida2={row['MEDIDA2']}")


