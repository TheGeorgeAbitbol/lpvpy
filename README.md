# lpvpy
Librairie python pour aider les utilisateurs du forum _La Passion du Vin_ (LPV) https://www.lapassionduvin.com
dans la gestion des CR de dégustation

### Copyright 2023 Mathias Bouquerel
Veuillez prendre connaissance de la [LICENSE](LICENSE.txt)

## Configuration reguise
[Python 3](https://www.python.org/)

## Tutoriel pour utiliser la fonction de transposition des CR de dégustation
Cette fonction permet de générer les CR par vin à partir des CR par participant suite à une dégustation pour laquelle
les participants ont chacun fait un CR contenant tous les vins, afin de faciliter la remontée des CR sur les fils
des domaines.

Le script `main_example.py` donne un exemple d'utilisation de cette fonction de transposition pour exploiter
les CR stockés dans le sous-dossier `CR-par-auteur`.

Les étapes à suivre sont les suivantes :
1. Créer un dossier `C:/[...]/ma_soiree_lpv`
2. Créer dans ce dossier un fichier texte pour chaque participant qui a été l'auteur d'un CR de la dégustation,
   le nom du fichier étant le nom/pseudo de l'auteur du CR (`George.txt` pour le CR écrit par George)
3. Copier le CR de chaque auteur dans le fichier correspondant
4. Reformater le CR si besoin, en suivant les règles suivantes 
   1. Le CR doit être en texte brut ne contenant aucune balise de formatage, hors image (voir plus bas)
   2. L'encodage du CR doit être `UTF-8`
   3. Chaque CR doit contenir pour chaque vin un paragraphe qui commence par une ligne qui ne contient que le nom du vin
   4. Cette ligne contenant le nom du vin doit commencer par `Vin X`, `X` étant un nombre ou la lettre X
   5. Chaque CR doit contenir un paragraphe pour tous les vins de la dégustation, y compris ceux non commentés
      (il faudra alors retraiter les fichiers générés)
   6. Le texte avant le 1e vin n'est pas pris en compte
   7. Tout texte après le 1e nom de vin est pris en compte : il faut supprimer tout ce qui ne correspond pas
      à un commentaire sur un vin particulier (transition, bilan d'une série, bilan de la dégustation, etc.)
   8. Un seul des CR sera utilisé pour récupérer le nom de tous les vins dans les lignes commençant par `Vin X`
   9. Dans les autres CR les lignes commençant par `Vin X` servent uniquement à séparer les paragraphes
      des différents vins, le contenu de ces lignes n'est pas exploité
   10. Dans le CR exploité pour récupérer le nom des vins, et uniquement dans celui-ci, on peut laisser les balises
       d'insertion des images si elles sont sur la ligne juste au-dessus ou juste en-dessous de celle annonçant
       le titre du vin. L'image sera insérée en tout début du CR du vin correspondant
5. Adapter le script `main_example.py` en remplaçant les valeurs des paramètres
   1. `review_dir_path` : chemin du dossier où les CR par auteur sont stockés, donc `C:/[...]/ma_soiree_lpv`
      (utiliser le double antislash `\\` comme séparateur de dossier sous Windows : `C:\\[...]\\ma_soiree_lpv`)
   2. `author_ref` = nom de l'auteur dont le CR est utilisé pour récupérer les noms des vins et les éventuelles images
   3. `header_file` = chemin d'un fichier texte utilisé pour ajouter un en-tête à tous les CR par vin
      (par exemple pour mettre un lien vers le CR de la dégustation complète)
6. Exécuter le script `main_example.py`
7. Vérifier que les CR par vin ont bien été générés dans le dossier courant, et si besoin supprimer les paragraphes
   correspondant aux auteurs n'ayant pas commenté certains vins
