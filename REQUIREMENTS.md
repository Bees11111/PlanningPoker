# Exigences du Projet

Ce document liste les exigences logicielles nécessaires pour exécuter le projet "Planning Poker".

## Environnement

- Anaconda

## Modules Python

Les modules suivants doivent être installés dans l'environnement Python pour assurer le bon fonctionnement du projet :

- `tkinter`: Bibliothèque pour l'interface graphique. Trouvable sur Anaconda sous `tk`
- `sys`: Module système. Utilisé pour quitter des menus. Integré à Python
- `svglib`: Bibliothèque pour la manipulation des fichiers SVG. `conda install -c conda-forge svglib`
- `reportlab`: Bibliothèque pour la création de documents. Utilisé pour les cartes. Trouvable sur Anaconda sous `reportlab`
- `json`: Module pour la manipulation de fichiers JSON. Trouvable sur Anaconda sous `json5`

## Installation avec terminal sans utiliser l'interface Anaconda

1. Installer Anaconda en utilisant la version la plus récente disponible sur le site officiel.

2. Créer un environnement virtuel à l'aide de la commande suivante :
   `conda create --name planning_poker_env python=3.8`

3. Activer l'environnement virtuel :
   `conda activate planning_poker_env`
   
4. Installer les modules requis :
   `conda install -c conda-forge tk`
   `conda install -c conda-forge svglib`
   `conda install -c conda-forge reportlab`