# Pętla While to funkcja zapętlania używana w każdym języku programowania.

i = 1
while i < 6:
  print(i)
  i += 1
i=1
print("\n")

while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
i=1
print("\n")

while i < 6:
  print(i)
  i += 1
else:
  print("Koncowa wartosc i, ktora juz sie nie printuje: "+str(i))
i=1
print("\n")

while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)