# Flask-SPA
Single Page Application avec le Framework Flask

Stack: Python,Flask,Jinja,FlaskForm

/FlaskSPA

=>app.py : "main" du dossier : routage avec les templates et lancement du serveur

=>data.py : contient les données qui seront affichés par le template dashboard.htm

=>form.py :contient la class ContactForm implémenté grace à Flaskform 

/Static

=> style.css : feuille de style de tout les templates 

/Templates

=> about.htm : page "à propos"

=> contact.htm : vue qui affiche le formulaire implémenté avec Flaskform

=> dashboard.htm : vue qui affiche les données implémentés dans data.py

=> error.htm : page affiché en cas d'erreur(401,404,500)

=> home.htm: page d'accueil 

=> layout.htm : squelette de tout les templates htm 


    /includes
  
    =>navbar.htm : barre de navigation 
