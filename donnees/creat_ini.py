import configparser
config_file = "list_capt_syst.ini"
cfg = configparser.ConfigParser()
cfg.read(config_file)

adresse_mac = "F2:C8:C2:B3:BA:E0"
choice_name = "toto"

cfg.add_section(adresse_mac)
cfg.set(adresse_mac, 'name', choice_name)
cfg.write(open(config_file, 'w'))
