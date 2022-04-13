#!/bin/bash
hostname > /etc/ssmtp/historial.txt
date >> /etc/ssmtp/historial.txt
uptime >> /etc/ssmtp/historial.txt
uuencode /etc/ssmtp/historial.txt historial.txt > /tmp/out.mail
mail -s "ENCENDIDO GPIO 22" programaembebidauth@gmail.com < /tmp/out.mail
rm -f /tmp/out.mail
echo "Correo Enviado"
