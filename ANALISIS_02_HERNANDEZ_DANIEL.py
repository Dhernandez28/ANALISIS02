"""
Created on Sat Sep 20 16:56:11 2020

@author: DANY  HERNANDEZ

@Description: Programa que optimiza los resultados de una base de datos obteniendo como resultado valores estrategicos para una mejor desición comercial.
 
"""
import os,time,csv
print("***** Bienvenido a Synergy Logistics ******* \n")
time.sleep(2) #congelacion del tiempo en ejecución 
os.system("cls") #limpiar pantalla 
conteo =1 # iniciamos contador en 1 para determinar el limite de las iteraciones en el while


mveces=[]#listas para tener mas ordenados los datos 
mcosto=[]
mcosto2=[]
datos=[]#creamos una lista vacia para manipular datos
#abrimos el archivo csv
with open("synergy_logistics_database.csv","r") as archi_csv:#abrir de manera segura un archivo csv con el formato de lectura
    lectura=csv.reader(archi_csv)#nuestra variable lectura será el atajo para leer nuestro csv
    for lin in lectura:
        datos.append(lin)

def menu():
  print("*********************************************************")
  print("* 1. -Las 10 mejores rutas de importación.              *") #mensaje 
  print("* 2. -Las 10 mejores rutas de exportacion.              *") #mensaje 
  print("* 3. -Medio de trasporte mas demandado.                 *") #mensaje 
  print("* 4. -Salir                                             *")
  print("*********************************************************\n") #mensaje

def base(direccion):
    cont=0
    cont2=0
    rutas_iteradas=[]#guardamos las rutas ya iteradas
    ndrutas=[]#guardamos el formato de nuestra ruta.
    for ruta in datos:
        if ruta[1] == direccion:
            ruta_actual = [ruta[2],ruta[3]] #marcamos cuales seran los indices con los campos que nos interesan
            
            if ruta_actual not in rutas_iteradas:
                for iteracion in datos:#se vuelve a iterar para realizar una comprobacion y concidencias
                    if ruta_actual == [iteracion[2],iteracion[3]]:
                        cont += 1 # empieza el conteo
                        cont2 += int(iteracion[9])

                rutas_iteradas.append(ruta_actual)# al macenams los valores obtenidos en nuestra nueva lista
                ndrutas.append([ruta[4],ruta[5],ruta[2],ruta[3],cont,cont2])#establecemos el formato de nuestra lista
                cont = 0 #reiniciamos el contador.
                cont2= 0
    return ndrutas

def almacenar(variable,l,):
    aux=0
    resulta.sort(reverse=True,key=lambda x:x[l])
    for resultado in resulta:
        año=resultado[0]
        origen=resultado[2]
        destino=resultado[3]
        nume=resultado[4]
        canti=resultado[5]
        if aux < 10:
            variable.append(resultado)
            #print((canti*100)/215691298000)Nota omiti el la consigna 3 porque mi computador se trababa demasiado y eso me atrasó mucho
            print(f"En el año {año} de {origen} a {destino} se generaron  {nume} traslados generando un costo de ${canti}.00 ")
        aux+=1

def base2(direccion,direct,direc,dire):
    cont=0
    cont2=0
    rutas_iteradas=[]#guardamos las rutas ya iteradas
    ndrutas=[]#guardamos el formato de nuestra ruta.
    for ruta in datos:
        if ruta[7] in [direccion,direct,direc,dire]:
            ruta_actual = [ruta[2],ruta[3]] #marcamos cuales seran los indices con los campos que nos interesan
            
            if ruta_actual not in rutas_iteradas:
                for iteracion in datos:#se vuelve a iterar para realizar una comprobacion y concidencias
                    if ruta_actual == [iteracion[2],iteracion[3]]:
                        cont += 1 # empieza el conteo
                        #cont2 += int(iteracion[9])
                        cont2 +=1
                        
        
                rutas_iteradas.append(ruta_actual)# al macenams los valores obtenidos en nuestra nueva lista
                ndrutas.append([ruta[2],ruta[3],ruta[7],cont])#establecemos el formato de nuestra lista
                cont = 0 #reiniciamos el contador.
                cont2= 0
    return ndrutas
#ordenamos conforme al tipo de traslado mas demandado e imprimimos resultado en pantalla
def almacenar2(variable,l):
    resulta.sort(reverse=True,key=lambda x:x[l])
    for resultado in resulta:
        # año=resultado[0]
        origen=resultado[0]
        destino=resultado[1]
        nume=resultado[2]
        canti=resultado[3]
        variable.append(resultado)
        print(f"De {origen} a {destino} se registraron {canti} viajes  por {nume}, en todo el periodo registrado")
           
    






        

while conteo <= 3: # decimos que mientras que el contador no supere esta condicdion 
  usuario = input("User: ")#pedimos datos al usuario
  contraseña = input("Contraseña: ")
  if usuario == "Sistemas" and contraseña == "SISTEMAS": #establecemos variables y evaluamos
    os.system("cls")
    menu()
    while True:
      opc=input("\n Ingrese un numero correspondiente al menú ->  ")
      if opc == '1':
        os.system("cls")
        menu()
        resulta=base('Imports')
        almacenar(mcosto,4)  
      elif opc == '2':
        os.system("cls")
        menu()
        resulta=base('Exports')
        almacenar(mveces,4)
      elif opc == '3':
        os.system("cls")
        menu()
        resulta=base2('Air','Rail','Road','Sea')
        almacenar2(mcosto2,3)  
      elif opc == '4':
        os.system("cls")
        break
      else:
        print("Opción incorrecta")
    conteo = 4 # se asigno al  contador un valor superior para dar salida al bucle
  else: #de lo contrario se visualiza mensaje de intentos fallidos
    print("Acceso Erroneo ")
    print("Intento", conteo ,"Pruebe de nuevo porfavor!")
    time.sleep(2)
    os.system("cls")
    if conteo == 3:
      print("Supero el limite de intentos ")
      print("Consulte a su administrador ")
      time.sleep(2)
      os.system("cls")
      break
    conteo = conteo +1 # cada iteracion se aumenta para validar la condicion establecida

        
        
        
        
        
        
        
        
        
        
        