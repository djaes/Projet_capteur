#!/usr/bin/env python
#-*- coding: utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(nom_objet, config):
    fromaddr = "djaes33@gmail.com"
    toaddr = config.get_adresse_mail_ini()
    mdp = config.get_mdp_ini()
    #attente du test
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Alert system surveillance"
    body = ("Le systeme a detecté un mouvement non autorisé de : "+ nom_objet)
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587) #serveur gmail
    server.starttls()
    server.login(fromaddr, mdp)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    return