from os import walk
listeFichiers=[]
for (repertoire, sousRepertoires, fichiers) in walk("./data/"):
    listeFichiers.extend(fichiers)
listeFichiers.sort()

for name in listeFichiers:
    fichier=open("./data/"+name,"r")
    readata=fichier.readlines()
    date_heure=name.split(".")
    date_heure=date_heure[0].replace(date_heure[0],date_heure[0][4:])
    for i in range(len(readata)):
        readata[i]=readata[i].split(";")
        readata[i][2]=readata[i][2].replace("\n","")
        #tout ça pour dégager le \n de la fin SUPER
        temp=open("./parkings/"+readata[i][0]+".dat","a")
        temp.write(date_heure+";"+readata[i][0]+";"+readata[i][1]+";"+readata[i][2])
        temp.write("\n")
        temp.close()
        print("Data "+date_heure+" écrite sur son fichier "+readata[i][0]+".dat")