import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
from os import walk
listeFichiers=[]
for (repertoire, sousRepertoires, fichiers) in walk("./parkings/"):
    listeFichiers.extend(fichiers)
listeFichiers.sort()

data=[]
for name in listeFichiers:
    fichier=open("./parkings/" + name, "r")
    date_heure=[]
    named=[]
    vehicle_free=[]
    vehicle_total=[]
    for line in fichier.read().split("\n"):
        if not line.startswith("#") and line != "":
            [date, nom, voiture_free, voiture_total] = line.split(";")
            voiture_free=int(voiture_free)
            voiture_total=int(voiture_total)
            date_heure.append(date)
            named.append(nom)
            vehicle_free.append(voiture_free)
            vehicle_total.append(voiture_total)
    data.append({ "name" : name.replace(".dat", ""), "dates": date_heure, "places_occupees": vehicle_free})

for current in data:
    name=current["name"]
    dates=current["dates"]
    print(dates)
    libre=current["places_occupees"]
    print(libre)
    xpoints = dates #[dt.datetime.strptime(d,'%Y-%m-%d@%H-%M-%S').date() for d in dates]
    ypoints = libre
    plt.plot(xpoints, ypoints)
    plt.plot(xpoints,ypoints, 'o')
    plt.yticks(np.arange(min(ypoints),max(ypoints),step=5))
    plt.title('Places libres dans'+current["name"])
    plt.xlabel("Date et heure")
    plt.ylabel("Places libres",)
    plt.show() 