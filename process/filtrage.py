from process.send_Mail import send_mail
import time

def filtrage(config, timer):
    # recuperation du fichier avec les adresse mac scanné
    with  open ("donnees/scan.txt","r")as content:
        addr_scan = []
        # creation d'un tableau avec uniquement les adresses mac scanné
        for line in content:
            if line != "/n":
                addr_scan.append(line.split(" ")[0])
    # creation d'un tableau les adresses mac enregistré dans le fichier ini
    addr_ini = config.get_addr_ini()
    # creation d'un tableau les nom des capteur enregistré dans le fichier ini
    name_ini = config.get_addr_to_name_ini()
    # teste pour chaque adresse enregistré
    for i in range(len(addr_ini)):
        print(addr_ini[i])
# teste si l'adresse enregistré est presente dans la liste d'adresse scanné
        if (addr_ini[i] in addr_scan) == True :
            # teste si l'adresse enregistré est presente dans le timer et si le timer pour cette adresse est inferieur a 60 sec
            test1 = addr_ini[i] in timer
            if  test1 == True :
                test2 = time.time() < (timer[addr_ini[i]] + 60)
                if  test2 == True :
                    print("Mouvement de " + addr_ini[i] + " detecté")
                    return timer
            #sinon il reinitialise/crer un timer pour cette adresse et appelle la fonction send mail
            print("Mouvement de " + addr_ini[i] + " detecté , envoie d'un mail d'alerte en cours")
            timer[addr_ini[i]] = time.time()
            send_mail(name_ini[i], config)
            continue
    return timer
