import os

znalezienie=False
slowo = 'unittest'
for filename in os.listdir('Pliki'):
    if filename.endswith('.py'):
        with open(os.path.join('Pliki', filename)) as f:
            content = f.read()
            if slowo.lower() in content.lower(): 
                print(slowo, 'zostala znaleziona w pliku:', filename)
                print("\n\nKod w pliku:\n\n"+ content+"\n\nWykonanie tego kodu:\n\n")
                exec(content)
                znalezienie=True 
            f.close() 
if znalezienie==False:
    print(slowo+ ' nie znaleziono') 
  
