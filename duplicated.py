from tkinter.filedialog import askdirectory
from tkinter import Tk
import os, hashlib
from pathlib import Path


Tk().withdraw()
path = askdirectory(title="Selectionner un dossier") #ouvre une fenetre pour selectionner le dossier à examiner
#print(path) retourne le chemin du fichier

file_list = os.listdir(path) #une fois fait, obtenir la liste de tous les fichiers contenus dans ce dossier 
#print(file_list)

unique = dict()
i = 0
print('proccessing...')
for file in file_list:
    #print(file)
    
    file_path = Path(os.path.join(path, file)) #affiche le nom du fichier
    #print(file_path)

    if file_path.is_file(): #si il s'agit d'un fichier
        fileHash = hashlib.md5(open(file_path, 'rb').read()).hexdigest()

        if fileHash not in unique:
            unique[fileHash] = file_path
        else:
            os.remove(file_path)
            print(f'supression avec success du fichier {file}')
            i += 1

    else:
        print(f"operation non reussi. {file} n'est pas un fichier")

print(f"{i} fichiers ont ete surprimés")
print('operation terminée!!')