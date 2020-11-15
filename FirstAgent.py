import win32com.client
import os
from random import choice
import time
import json

print("-----------------------------------------------------/")
print("                      Data-Base                      /")
print("-----------------------------------------------------/")
print("                                                     /")
print("  Hola! Este programa da la demostracion de como se  /")
print(" verian datos a la forma de entrar, guardarse en una /")
print("                  base de datos.                     /")
print("-----------------------------------------------------/")
time.sleep(7)

Filedata = open("TFDB.txt","a") 

while True: 
    FirstName = ['Carlos', 'Antonio', 'Stiven', 'Yeremi', 'Fernando', 'Cristopher', 'Ed', 'German', 'Fernando', 'Dania', 'Melissa', 'Ariana', 'Emanuel', 'Genesis', 'Andres', 'Jimena', 'Oscar', 'Piedad', 'Leonel', 'Nanit', 'Carolina', 'Juan', 'Ramiro', 'Joe', 'Noe', 'Fabricio', 'Andrea']

    LastName = [' Marroquin', ' Ortega', ' Sandoval', ' Vazquez', ' Jimenez', ' Zetino', ' Garzia', ' Estrada', ' Paz', ' Cruz', ' Manuel', ' Santillana', ' Noble', ' Ronaldo', ' Claus', ' Ladredo', ' Maop', ' Yanes', ' Olivera', ' Lopez', ' Obrador', ' Nieto', ' Trump', ' Biden', ' Fuentes', ' Amelio']

    Rar = choice(FirstName) 

    Rar2 = choice(LastName) 

    datos = { 
        'Nombre': (Rar),
        'Apellido': (Rar2)
    }

    dato_json = json.dumps(datos) 
    qinfo=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
    computer_name = os.getenv('COMPUTERNAME')
    qinfo.FormatName="direct=os:"+computer_name+"\\PRIVATE$\\save-deleted"
    queue=qinfo.Open(2,0)   
    msg=win32com.client.Dispatch("MSMQ.MSMQMessage")
    msg.Label= "Archivos Random"
    msg.Body = (dato_json)
    print("                                  ")
    print("          Holaa amig@!            ")
    print("----------------------------------")
    print("      Entrando en Database...    /")
    print("---------------------------------/")
    print("---------------------------------/")
    print("Dato ingresado: " + Rar + Rar2) 
    print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯/")
    msg.Send(queue)

    Filedata = open("TFDB.txt","a") 

    Filedata.write(dato_json + "\n")

    Filedata.close()

    queue.Close() 

    print("Archivo ingresado con éxito!")
    time.sleep(2)
    print("Wait...")
    print("")
    time.sleep(2)