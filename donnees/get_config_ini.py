import configparser

class Get_config_ini:
    def __init__(self):
        self.config =configparser.ConfigParser()
        self.config.read('donnees/config.ini')
    
    
    def get_test(self):
        print (self.config.has_option("djaes","capteur_4"))

    def get_addr_ini(self):
        addr_ini = []
        i=1
        while 1:
            capteur = "capteur_"+str(i)
            if self.config.has_option("djaes",capteur)== False :
                return addr_ini
            X = self.config.get('djaes', capteur)
            addr_ini.append(X.split(" ")[0])
            i+=1

    def get_addr_to_name_ini(self):
        name_ini = []
        i=1
        while 1:
            capteur = "capteur_"+str(i)
            if self.config.has_option("djaes",capteur)== False :
                return name_ini
            X = self.config.get('djaes', capteur)
            name_ini.append(X.split(" ")[1])
            i+=1
        
    def get_actif_ini(self):
        return self.config.get('djaes', 'scan actif')

    def get_adresse_mail_ini(self):
        return self.config.get('djaes', 'adresse mail')

    def get_mdp_ini(self):
        return self.config.get('djaes', 'mot de passe')

