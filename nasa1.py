import requests
import csv
import imagejour
import affimage

key_api = '61mk17IxhvvbPJ3i81E8uD58nvYTJcdrtztiKm8H'
url = 'https://api.nasa.gov/planetary/apod'
params = {'api_key': key_api}
response = requests.get(url, params=params)
# print(response.status_code)

results = response.json()
en_tete = []
ligne = []
list = results.keys()
lest = results.values()
with open('nasa2.csv', 'w') as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter=',')
    for keys in list:
        en_tete.append(keys)
    writer.writerow(en_tete)
    for values in lest:
        ligne.append(values)
    writer.writerow(ligne)
word = ["explanation", "title", "url"]
elements = []
for x in word:
    elements.append(results.get(x))
imagejour.importima(elements[-1])
nimage = elements[-1].split('/')[-1]
url_image = "{}".format(nimage)
affimage.affimage(url_image, elements[0], elements[-2])
    # valoris = []
    # for a in en_tete:
    #     valoris.append(results[a])
    # writer.writerow(valoris)