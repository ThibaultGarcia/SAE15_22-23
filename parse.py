import time
import requests
from lxml import etree
import datetime

def getDate():
    return str(datetime.date.today()) + "@" + datetime.datetime.now().strftime("%H-%M-%S")

def getParkInfos(name):
    retour=requests.get('https://data.montpellier3m.fr/sites/default/files/ressources/'+name+'.xml')
    getParkInfosFile=open("tempo.xml","w", encoding='utf8')
    #c'est un document intermédiaire qui se verra ré-écrit par-dessus à chaque passage, d'où son ouverture ici
    getParkInfosFile.write(retour.text)
    getParkInfosFile.close()
    return print("= Données récupérées pour "+parkN+" ci-dessous =")

def printParkInfos():
    tree = etree.parse("tempo.xml")
    for item in tree.xpath("Name"):
     print('Nom du parking :',item.text)
     infos.write(item.text+";")
    for item in tree.xpath("Free"):
     free=item.text
     print('Nombre de places libres :',item.text)
     infos.write(item.text+";")
    for item in tree.xpath("Total"):
     total=item.text
     print('Nombre de places totales',item.text)
     infos.write(item.text+"\n")
    for item in tree.xpath("Status"):
     print('Statut d\'ouverture ?',item.text)
    print()
    return free, total
    

def getPercentage(free,total):
    print("Pourcentage de places libres :")
    print((free/total)*100)
    print()

parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_SABL','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']

#mise à zero du fichier infos.txt
infos=open("infos.txt","w", encoding='utf8')
infos.write("")
infos.close()

while True :
    infos=open("./data/data" + getDate() + ".dat","a",encoding="utf-8")
    for parkN in parkings:
        getParkInfos(parkN)
        free,total = printParkInfos()
        getPercentage(int(free),int(total))
    infos.close()
    print("Passage effectué ! "+getDate())
    time.sleep(60)