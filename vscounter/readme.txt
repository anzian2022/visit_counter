1 - COPIER PUIS COLLER CETTE APPLICATION (vscounter) A LA RACINE DE VOTRE PROJET
2 - DANS LE FICHIER setting.py DE VOTRE PROJET, AJOUTER 'vscounter' DANS LA PARTIE INSTALLED_APPS
3 - TAPER LES 2 COMMANDES CI-DESSOUS :
    - python manage.py makemigrations
    - python manage.py migrate
    Ces commandes permettent de créer la table dans laquelle va être stocker les différentes adresses IP des visiteurs
4 - POUR EVITER DE FAIRE CETTE ACTION PLUSIEURS FOIS, ALLER DANS LE CODE HTML LE PLUS INCLUS ET CONFIGURER COMME SUIT:
    - INSERER {% load vscounter_tag %} AU DESSUS DU CODE HTML
    - INSERER {% vscounter request as vsc %} POUR RECUPERER LE NOMBRE DE VISITE DANS UNE VARIABLE NOMMEE ICI 'vsc'
    - UTILISER {{vsc}} Là Où VOUS AFFICHER LE NOMBRE DE VISITE

