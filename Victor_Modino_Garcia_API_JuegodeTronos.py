import json
from pathlib import Path
import requests
import os

try:

    def menu():

        os.system('cls')
        
        print("Selecciona una opcion:")
        print("\t1 - Nombre de los apodos que tiene Jon Nieve")
        print("\t2 - El blason de una casa, dandome su nombre")
        print("\t3 - Titulos de la casa Stark")
        print("\t4 - Listado de los titulos de Baelor Targaryen")
        print("\t5 - Casas que pertenecen a la region que quieras")
        print("\t6 - Salir")

        opcion=int(input("Selecciona una opcion : "))

        return (opcion)

    def motes_jon():

        api_address="https://anapioficeandfire.com/api/characters/583"
      
        resp = requests.get(api_address)

        if resp.status_code==200:#todo correcto
           
            json_data=json.loads(resp.content)

        print("El nombre de los apodos que tiene Jon Nieve son: %s"%json_data.get('aliases')) 
    
    def casas_poniente_blason():
#para probar: House Arryn of the Eyrie , House Algood , House Lannister of Casterly Rock
        casa=input ("Introduce el nombre de una casa de poniente para saber cual es su blason: ")

        api_address="https://anapioficeandfire.com/api/houses/?name=%s"%casa

        resp = requests.get(api_address)

        if resp.status_code==200:

            json_data=json.loads(resp.content)

            print ("Simbolo del blason de la casa : %s"%json_data[0]['coatOfArms'])
            
    def titulo_Stark():

        api_address="https://anapioficeandfire.com/api/houses/362"
      
        resp = requests.get(api_address)

        if resp.status_code==200:#todo correcto
           
            json_data=json.loads(resp.content)

        print("El nombre los titulos de la casa Stark: %s"%json_data.get('titles')) 

    def Titulos_personales_Baelor_Targaryen():
        
        api_address="https://anapioficeandfire.com/api/characters/161"

        resp = requests.get(api_address)

        if resp.status_code==200:#todo correcto

            json_data=json.loads(resp.content)

        print("Los titulos que posee Baelor Targaryen son: %s"%json_data.get('titles')) 

    def region_casas():
#para probar: Dorne , The Vale , The Reach , The North
        region=input ("Introduce el nombre de una region de poniente para saber las casas pertenecientes a ella: ")

        api_address="https://anapioficeandfire.com/api/houses/?region=%s"%region

        resp = requests.get(api_address)

        if resp.status_code==200:

            json_data=json.loads(resp.content)

            contador=1
            for datos in json_data:

                print ("La casa",datos['name'], "pertenece a la region de",region)
                
                contador+=1
                if contador>50:
                    break
            
            print ("Larga vida al rey de ",region)

    while True:
        opcion=menu()
        if opcion==1:
            motes_jon()
        elif opcion==2:
            casas_poniente_blason()
        elif opcion==3:
            titulo_Stark()
        elif opcion==4:
            Titulos_personales_Baelor_Targaryen()
        elif opcion==5:
            region_casas()
        elif opcion==6:
            break
 
        input("Pulse una tecla para terminar...")

except:
    
    print("Ha ocurrido algun error")