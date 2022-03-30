#For Loop jest używany do iteracji przez elementy różnych typów zmiennych.
Przyklad = ["1", "2", "Przyklad","4","5"]

for elementy in Przyklad:
  print(elementy)
print("\n")

for elementy in "Przyklad":
  print(elementy)
print("\n")

for elementy in Przyklad:
  print(elementy)
  if elementy == "Przyklad":
    break
print("\n")

for elementy in Przyklad:
  if elementy == "Przyklad":
    break
  print(elementy)
print("\n")

for elementy in Przyklad:
  if elementy == "Przyklad":
    continue
  print(elementy)
print("\n")

for elementy in range(5):
  print(elementy)