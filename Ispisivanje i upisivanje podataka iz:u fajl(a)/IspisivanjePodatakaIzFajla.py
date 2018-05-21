with open('fajlZaIspisivanjePodataka.txt', 'r') as myfile:
    fajl = myfile.read().replace(';', ' ')

print(fajl)