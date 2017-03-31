import configparser
cfg = configparser.ConfigParser()
cfg.read("config.ini")

liste_de_config = ['test', "toto", "jerome", "djaes33@hotmail.com", "Lordunst231280", "True", "F2:C8:C2:B3:BA:E0 Capteur_GP2 ", "F2:C8:C2:B3:BA:AA Capteur_GP1 ", "F4:F4:E4:44:B9:21 Capteur_GP4 "]


cfg.add_section(liste_de_config[0])
cfg.set(liste_de_config[0], 'nom', liste_de_config[1])
cfg.set(liste_de_config[0], 'prenom', liste_de_config[2])
cfg.set(liste_de_config[0], 'adresse mail', liste_de_config[3])
cfg.set(liste_de_config[0], 'mot de passe', liste_de_config[4])
cfg.set(liste_de_config[0], 'scan actif', liste_de_config[5])
cfg.set(liste_de_config[0], 'capteur_1', liste_de_config[6])
cfg.set(liste_de_config[0], 'capteur_2', liste_de_config[7])
cfg.set(liste_de_config[0], 'capteur_3', liste_de_config[8])
cfg.write(open('config.ini','w'))