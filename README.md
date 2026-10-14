# School Manager

Application Django qui affiche une page d'accueil et la liste des étudiants d'une école.

## Prérequis
- Windows 10 ou 11
- Python 3
- Git
- VS Code

## Installation
1. Cloner le projet : git clone https://github.com/thiawmamediarra1212-del/school_manager.git
2. Entrer dans le dossier : cd school_manager

## Activation du venv
python -m venv venv
venv\Scripts\activate

## Installation de Django
pip install -r requirements.txt

## Lancement du serveur
python manage.py runserver

## URLs disponibles
- http://127.0.0.1:8000/ : page d'accueil
- http://127.0.0.1:8000/students/ : liste des étudiants
- http://127.0.0.1:8000/students/15/ : détail d'un étudiant