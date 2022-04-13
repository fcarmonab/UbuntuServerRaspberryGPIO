from Tkinter import *
import ttk
import tkFont
import tkMessageBox
import os
import time
import subprocess
import ScrolledText

v0 = Tk()
v0.title("EXAMEN TERCER PARCIAL")
v0.geometry("600x600+0+0")

formato = tkFont.Font(family="Helvetica", size=12)
label = Label(v0, text="Desarrollado en Equipo",font=formato).place(x=190, y=10)


img_on = PhotoImage(file="on.gif")
img_off = PhotoImage(file="off.gif")



def limpiar():
              horaInicial.set("")
              minInicial.set("")
              horaFinal.set("")
              minFinal.set("")

def salida():
             v0.destroy()

def registrar0():
                print "REGISTRADO"
                hi=horaInicial.get()
                mi=minInicial.get()
                hf=horaFinal.get()
                mf=minFinal.get()
                tab=" "
                dia="*"
                mes="*"
                ano="*"
                usuario="root"
                path1='sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/on0"'
                path2='sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/off0"'
                path3="sudo /./etc/ssmtp/correo0on.sh"
                path4="sudo /./etc/ssmtp/correo0off.sh"

                #Asignar permisos de escritura y ejecucion

                os.system("sudo chmod -R 777 /etc/cron.d/tarea1")
                os.system("sudo chmod -R 777 /etc/cron.d/tarea2")
                os.system("sudo chmod -R 777 /etc/cron.d/tarea7")
                os.system("sudo chmod -R 777 /etc/cron.d/tarea8")

                #cadena
                cadena=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path1))
                cadena2=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path2))
                cadena3=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path3))
                cadena4=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path4))
                
                # aperturar archivo

                pf=open("/etc/cron.d/tarea1","w")
                pf.write(cadena)
                pf.write("\n")
                pf.close()

                pf=open("/etc/cron.d/tarea7","w")
                pf.write(cadena3)
                pf.write("\n")
                pf.close()
                time.sleep(0.1)
                
                pf=open("/etc/cron.d/tarea2","w")
                pf.write(cadena2)
                pf.write("\n")
                pf.close()
                
                pf=open("/etc/cron.d/tarea8","w")
                pf.write(cadena4)
                pf.write("\n")
                pf.close()
                time.sleep(0.1)

                #Revertir permiso
                os.system("sudo chmod -R 755 /etc/cron.d/tarea1")
                os.system("sudo chmod -R 755 /etc/cron.d/tarea2")
                os.system("sudo chmod -R 755 /etc/cron.d/tarea7")
                os.system("sudo chmod -R 755 /etc/cron.d/tarea8")

                #Reiniciar servicios
                os.system("sudo /etc/init.d/cron restart")
                limpiar()
                tkMessageBox.showinfo("save",message="Tiempos registrado")

          
                
def registrar2():
                print "REGISTRADO"
                hi=horaInicial.get()
                mi=minInicial.get()
                hf=horaFinal.get()
                mf=minFinal.get()
                tab=" "
                dia="*"
                mes="*"
                ano="*"
                usuario="root"
                path1='sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/on2"'
                path2='sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/off2"'
                path3="sudo /./etc/ssmtp/correo2on.sh"
                path4="sudo /./etc/ssmtp/correo2off.sh"


                #Asignar permisos de escritura y ejecucion

                os.system("sudo chmod -R 777 /etc/cron.d/tarea3")
                os.system("sudo chmod -R 777 /etc/cron.d/tarea4")
                os.system("sudo chmod -R 777 /etc/cron.d/tarea9")
                os.system("sudo chmod -R 777 /etc/cron.d/tarea10")

                #cadena
                cadena=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path1))
                cadena2=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path2))
                cadena3=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path3))
                cadena4=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path4))

                # aperturar archivo

                pf=open("/etc/cron.d/tarea3","w")
                pf.write(cadena)
                pf.write("\n")
                pf.close()

                pf=open("/etc/cron.d/tarea9","w")
                pf.write(cadena3)
                pf.write("\n")
                pf.close()
                time.sleep(0.1)
                
                pf=open("/etc/cron.d/tarea4","w")
                pf.write(cadena2)
                pf.write("\n")
                pf.close()                              

                pf=open("/etc/cron.d/tarea10","w")
                pf.write(cadena4)
                pf.write("\n")
                pf.close()
                time.sleep(0.1)


                #Revertir permiso
                os.system("sudo chmod -R 755 /etc/cron.d/tarea3")
                os.system("sudo chmod -R 755 /etc/cron.d/tarea4")
                os.system("sudo chmod -R 755 /etc/cron.d/tarea9")
                os.system("sudo chmod -R 755 /etc/cron.d/tarea10")

                #Reiniciar servicios
                os.system("sudo /etc/init.d/cron restart")
                limpiar()
                tkMessageBox.showinfo("save",message="Tiempos registrado")

                     

def registrar22():
                print "REGISTRADO"
                hi=horaInicial.get()
                mi=minInicial.get()
                hf=horaFinal.get()
                mf=minFinal.get()
                tab=" "
                dia="*"
                mes="*"
                ano="*"
                usuario="root"
                path1='sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/on22"'
                path2='sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/off22"'
                path3="sudo /./etc/ssmtp/correo22on.sh"
                path4="sudo /./etc/ssmtp/correo22off.sh"

                #Asignar permisos de escritura y ejecucion

                os.system("sudo chmod -R 777 /etc/cron.d/tarea5")
                os.system("sudo chmod -R 777 /etc/cron.d/tarea6")
                os.system("sudo chmod -R 777 /etc/cron.d/tarea11")
                os.system("sudo chmod -R 777 /etc/cron.d/tarea12")

                #cadena
                cadena=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path1))
                cadena2=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path2))
                cadena3=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path3))
                cadena4=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path4))

                # aperturar archivo

                pf=open("/etc/cron.d/tarea5","w")
                pf.write(cadena)
                pf.write("\n")
                pf.close()

                pf=open("/etc/cron.d/tarea11","w")
                pf.write(cadena3)
                pf.write("\n")
                pf.close()    
                time.sleep(0.1)            
                
                pf=open("/etc/cron.d/tarea6","w")
                pf.write(cadena2)
                pf.write("\n")
                pf.close()

                pf=open("/etc/cron.d/tarea12","w")
                pf.write(cadena4)
                pf.write("\n")
                pf.close()
                time.sleep(0.1)


                #Revertir permiso
                os.system("sudo chmod -R 755 /etc/cron.d/tarea5")
                os.system("sudo chmod -R 755 /etc/cron.d/tarea6")
                os.system("sudo chmod -R 755 /etc/cron.d/tarea11")
                os.system("sudo chmod -R 755 /etc/cron.d/tarea12")

                #Reiniciar servicios
                os.system("sudo /etc/init.d/cron restart")
                limpiar()
                tkMessageBox.showinfo("save",message="Tiempos registrado")
                
              

def abrirVentana0():
                     ventana0 = Toplevel(v0)
                     ventana0.geometry("600x600+0+0")
                     titulo0 = Label(ventana0, text="OPCION GPIO-0")
                     label = Label(ventana0, text="SE ENCUENTRA EN GPIO-0",font=formato).place(x=165, y=10)
                     
                     global horaInicial
                     global minInicial
                     global horaFinal
                     global minFinal
                     
                     def lecturaOn ():
                                      os.system('sudo /./home/fcarmona/lectura0on.sh > /home/fcarmona/gpio0.txt')
                                      pf=open("/home/fcarmona/gpio0.txt","r")
                                      for linea in pf:
                                                      campo=linea.split("\n")
                                                      campof=campo[0]
                                                      if (campof=="1"):
                                                                       
                                                                       imagenOn=Button(ventana0,image=img_on).place(x=320, y=102)
                                                                       text1= tkFont.Font(family="Arial",size ="20")
                                                                       label1 =Label(ventana0,text="1",font=text1).place(x=300,y=50)
                                                                       ventana0.after(1000,lecturaOn)
                                                      if (campof=="0"):
                                                                       text1= tkFont.Font(family="Arial",size ="20")
                                                                       imagenOn=Button(ventana0,image=img_off).place(x=320, y=102)
                                                                       label1 = Label(ventana0,text="0",font=text1).place(x=300,y=50)
                                                                       ventana0.after(1000,lecturaOn)
                     lecturaOn()

                     def on():
                              os.system('sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/on0.sh"')
                              os.system('sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/on0"')
                              os.system("sudo /./etc/ssmtp/correo0on.sh")

                     def off():
                               os.system('sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/off0.sh"')
                               os.system('sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/off0"')
                               os.system("sudo /./etc/ssmtp/correo0off.sh")

                     def salida():
                                  ventana0.destroy()
                                  ventana0.update()
                     
                                
                     btn_on0 = Button(ventana0,text="ENCENDER                         ", command=on).place(x=50, y=50)
                     btn_off0 = Button(ventana0,text="APAGAR                             ", command=off).place(x=50, y=110)
                     btn_retorno = Button(ventana0, text="RETORNO MENU PRINCIPAL", command=salida).place(x=50, y=180)
                     
                     minInicial=StringVar()
                     horaInicial=StringVar()
                     minFinal=StringVar()
                     horaFinal=StringVar()

                     label_horaInicial =Label(ventana0, text="Hora Inicial").place(x=10,y=250)
                     txt_horaInicial = Entry(ventana0, textvariable=horaInicial, width=20).place(x=130, y=250)

                     label_minInicial =Label(ventana0, text="Minuto Inicial").place(x=10,y=280)
                     txt_minInicial = Entry(ventana0, textvariable=minInicial, width=20).place(x=130, y=280)

                     label_horaFinal =Label(ventana0, text="Hora Final").place(x=10,y=310)
                     txt_horaFinal = Entry(ventana0, textvariable=horaFinal, width=20).place(x=130, y=310)

                     label_minFinal =Label(ventana0, text="Minuto Final").place(x=10,y=340)
                     txt_minFinal = Entry(ventana0, textvariable=minFinal, width=20).place(x=130, y=340)
                     
                     btn_guardar=Button(ventana0,text="GUARDAR", command=registrar0).place(x=150,y=385)

def abrirVentana2():
                     ventana2 = Toplevel(v0)
                     ventana2.geometry("600x600+0+0")
                     titulo2 = Label(ventana2, text="OPCION GPIO-2")
                     label = Label(ventana2, text="SE ENCUENTRA EN GPIO-2",font=formato).place(x=165, y=10)
                     global horaInicial
                     global minInicial
                     global horaFinal
                     global minFinal   
                     
                     def lecturaOn ():
                                      os.system('sudo /./home/fcarmona/lectura2on.sh > /home/fcarmona/gpio2.txt')
                                      pf=open("/home/fcarmona/gpio2.txt","r")
                                      for linea in pf:
                                                      campo=linea.split("\n")
                                                      campof=campo[0]
                                                      if (campof=="1"):
                                                                       
                                                                       imagenOn=Button(ventana2,image=img_on).place(x=320, y=102)
                                                                       text1= tkFont.Font(family="Arial",size ="20")
                                                                       label1 = Label(ventana2,text="1",font=text1).place(x=300,y=50)
                                                                       ventana2.after(1000,lecturaOn)
                                                      if (campof=="0"):
                                                                       text1= tkFont.Font(family="Arial",size ="20")
                                                                       imagenOn=Button(ventana2,image=img_off).place(x=320, y=102)
                                                                       label1 = Label(ventana2,text="0",font=text1).place(x=300,y=50)
                                                                       ventana2.after(1000,lecturaOn)
                     lecturaOn()

                     def on():
                              os.system('sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/on2.sh"')
                              os.system('sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/on2"')
                              os.system("sudo /./etc/ssmtp/correo2on.sh")
                              
                     def off():
                               os.system('sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/off2.sh"')
                               os.system('sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/off2"')
                               os.system("sudo /./etc/ssmtp/correo2off.sh")
                     def salida():
                                  ventana2.destroy()
                                  ventana2.update()
                     
                                
                     btn_on2 = Button(ventana2,text="ENCENDER                         ", command=on).place(x=50, y=50)
                     btn_off2 = Button(ventana2,text="APAGAR                             ", command=off).place(x=50, y=110)
                     btn_retorno = Button(ventana2, text="RETORNO MENU PRINCIPAL", command=salida).place(x=50, y=180)

                     minInicial=StringVar()
                     horaInicial=StringVar()
                     minFinal=StringVar()
                     horaFinal=StringVar()

                     label_horaInicial =Label(ventana2, text="Hora Inicial").place(x=10,y=250)
                     txt_horaInicial = Entry(ventana2, textvariable=horaInicial, width=20).place(x=130, y=250)

                     label_minInicial =Label(ventana2, text="Minuto Inicial").place(x=10,y=280)
                     txt_minInicial = Entry(ventana2, textvariable=minInicial, width=20).place(x=130, y=280)

                     label_horaFinal =Label(ventana2, text="Hora Final").place(x=10,y=310)
                     txt_horaFinal = Entry(ventana2, textvariable=horaFinal, width=20).place(x=130, y=310)

                     label_minFinal =Label(ventana2, text="Minuto Final").place(x=10,y=340)
                     txt_minFinal = Entry(ventana2, textvariable=minFinal, width=20).place(x=130, y=340)
                     
                     btn_guardar=Button(ventana2,text="GUARDAR", command=registrar2).place(x=150,y=385)


def abrirVentana22():
                     ventana22 = Toplevel(v0)
                     ventana22.geometry("600x600+0+0")
                     titulo22 = Label(ventana22, text="OPCION GPIO-22")
                     label = Label(ventana22, text="SE ENCUENTRA EN GPIO-22",font=formato).place(x=165, y=10)
                     global horaInicial
                     global minInicial
                     global horaFinal
                     global minFinal  
                     
                     def lecturaOn ():
                                      os.system('sudo /./home/fcarmona/lectura22on.sh > /home/fcarmona/gpio22.txt')
                                      pf=open("/home/fcarmona/gpio22.txt","r")
                                      for linea in pf:
                                                      campo=linea.split("\n")
                                                      campof=campo[0]
                                                      if (campof=="1"):
                                                                       
                                                                       imagenOn=Button(ventana22,image=img_on).place(x=320, y=102)
                                                                       text1= tkFont.Font(family="Arial",size ="20")
                                                                       label1 = Label(ventana22,text="1",font=text1).place(x=300,y=50)
                                                                       ventana22.after(1000,lecturaOn)
                                                      if (campof=="0"):
                                                                       text1= tkFont.Font(family="Arial",size ="20")
                                                                       imagenOn=Button(ventana22,image=img_off).place(x=320, y=102)
                                                                       label1 = Label(ventana22,text="0",font=text1).place(x=300,y=50)
                                                                       ventana22.after(1000,lecturaOn)
                     lecturaOn()

                     def on():
                              os.system('sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/on22.sh"')
                              os.system('sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/on22"')
                              os.system("sudo /./etc/ssmtp/correo22on.sh")

                     def off():
                               os.system('sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/off22.sh"')
                               os.system('sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo /./home/uth/off22"')
                               os.system("sudo /./etc/ssmtp/correo22off.sh")

                     def salida():
                                  ventana22.destroy()
                                  ventana22.update()
                     
                                
                     btn_on22 = Button(ventana22,text="ENCENDER                         ", command=on).place(x=50, y=50)
                     btn_off22 = Button(ventana22,text="APAGAR                             ", command=off).place(x=50, y=110)
                     btn_retorno = Button(ventana22, text="RETORNO MENU PRINCIPAL", command=salida).place(x=50, y=180)

                     minInicial=StringVar()
                     horaInicial=StringVar()
                     minFinal=StringVar()
                     horaFinal=StringVar()

                     label_horaInicial =Label(ventana22, text="Hora Inicial").place(x=10,y=250)
                     txt_horaInicial = Entry(ventana22, textvariable=horaInicial, width=20).place(x=130, y=250)

                     label_minInicial =Label(ventana22, text="Minuto Inicial").place(x=10,y=280)
                     txt_minInicial = Entry(ventana22, textvariable=minInicial, width=20).place(x=130, y=280)

                     label_horaFinal =Label(ventana22, text="Hora Final").place(x=10,y=310)
                     txt_horaFinal = Entry(ventana22, textvariable=horaFinal, width=20).place(x=130, y=310)

                     label_minFinal =Label(ventana22, text="Minuto Final").place(x=10,y=340)
                     txt_minFinal = Entry(ventana22, textvariable=minFinal, width=20).place(x=130, y=340)
                     
                     btn_guardar=Button(ventana22,text="GUARDAR", command=registrar22).place(x=150,y=385)

                     
def reporte():
              os.system('sshpass -p "fcarmona" ssh -l "uth" 192.168.0.27 "sudo gpio readall" > /etc/ssmtp/historial.txt')              
              os.system("sudo /./etc/ssmtp/gpioReadAll.sh")
             

#Botones

btn_gpio17 = Button(v0,text="OPCION GPIO-0       ", command=abrirVentana0).place(x=50, y=50)
 
btn_gpio27 = Button(v0,text="OPCION GPIO-2       ", command=abrirVentana2).place(x=50, y=120)

btn_gpio21 = Button(v0,text="OPCION GPIO-22      ", command=abrirVentana22).place(x=50, y=190)

btn_gpio21 = Button(v0,text="RESUMEN DE GPIO  ", command=reporte).place(x=50, y=260)

btn_salida = Button(v0,text="SALIDA                   ", command=salida).place(x=50, y=330)




v0.mainloop()
