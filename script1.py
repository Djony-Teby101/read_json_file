import json
from time import sleep

def lire_json_fichier(file_path):
    try:
        with open(file_path, 'r') as file:
            data= json.load(file)
        return data
    
    # gérer l'exception si le fichier est pas trouvé.
    except FileNotFoundError:
        print("Erreur: le fichier n'a pas été trouvé ")
        return None
    #gerer l'exception si le fichier est pas encoder json
    except json.JSONDecodeError:
        print("Erreur: probleme de decodage.")



# definir le path
file_path="database.json"

data=lire_json_fichier(file_path)

if data is not None:
    print("les données fournit par le fichier:")
    
    print(data)
   