# Pedir peso y altura para calcular la masa corporal: mc = peso / altura^2.

P = float(input("Digita su peso actual: "))
A = float(input("Digita su Altura actual: "))

mc = P / A**2

print (f"Su masa corporal es de: {mc:.2f}")