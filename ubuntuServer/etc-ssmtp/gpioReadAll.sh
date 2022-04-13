#!/bin/bash
uuencode /etc/ssmtp/historial.txt historial.txt > /tmp/out.mail
mail -s "RESUMEN DE GPIO READALL" programaembebidauth@gmail.com < /tmp/out.mail
rm -f /tmp/out.mail
echo "Correo Enviado"
