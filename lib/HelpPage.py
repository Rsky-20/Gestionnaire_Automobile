import tkinter as tk
import lib.DataTool as DT

def welcome_page(master):
    """
    [Description]
    Fonction permettant de générer la page "à propos".

    :param master: master se réfaire à la page parent
    :return:
    """

    app = tk.Toplevel(master)
    h = app.winfo_screenheight()
    w = app.winfo_screenwidth()
    screen = str(round(w*0.748)) +"x" + str(round(h*0.91)) + "+" + str(round(w*0.246)) + "+" + str(round(h*0.052))
    app.geometry(screen)
    app.attributes("-toolwindow", 1)# Supprime les boutons Réduire/Agrandir
    app.transient(master)
    app.resizable(False, False)
    app.title("A propos")
    
    para1_help = """Ici se trouve l’ensemble des explications sur l’utilisation de ce logiciel.
Pour commencer, nous allons regarder la maniere dont fonctionne le logiciel. """

    titre1_help = """

Utilisateur : """
    
    paraf_utilisateur = """
            Nous pouvons voir que le premier bouton est le bouton « utilisateur », il sert à rajouter un utilisateur dans le logiciel.
            Pour creer ce nouveau profil utilisateur, il est necessaire de rentrer son nom, son prenom, son age 
            (Attention ! L’utilisateur ne peut pas etre age de moins de 18 ans, age legal pour conduire une voiture en France) 
            et son numero de permis. Il sera egalement possible d’associer un numero de telephone et une adresse mail au compte client. 
            Après avoir rentre toutes ces informations, il faut cliquer sur le bouton « valider ». 
            Une page recapitulant toutes les informations va apparaitre. 
            Il suffit de cliquer sur « ok » si toutes les informations saisies sont correctes.""" 

    titre2_help = """

Reservation : """

    paraf_reservation = """
            Le deuxième bouton « Reservation » sert a creer une reservation.
            Pour se faire il faut choisir le client dans le menu deroulant (toutes ses informations sont associees a son nom). 
            Il faut egalement selectionner le type de voitures voulu par le client et les dates de debut et de fin de la location 
            de la voiture. Chaque fois qu’une information est modifiee, le contenu de l’encadre en dessous l’est aussi. 
            Cela permet de verifier les informations en temps reel. Si le client le souhaite, il peut ou non souscrire a assurance. 
            Une fois toutes les informations remplies, il suffit de cliquer sur « valider » puis sur « ok ». """

    titre3_help = """

Terminer location : """

    paraf_location = """
            Le troisième bouton « Terminer la location » sert à la fin d’une location, lorsque le client ramene la voiture.
            Afin de terminer la location d’une voiture, il suffit de rentrer l’identifiant de la voiture et le nombre de 
            kilomètres parcourus par la voiture. Une fois toutes les informations remplies, il suffit de cliquer sur « valider » 
            puis sur « ok »."""

    
    text = tk.Text(app)
    text.tag_config("Debut", font=('Tahoma', 20))
    text.tag_config("Titre", font=('Tahoma', 20, 'bold', 'underline'), tabs=('3c', '5c', '12c'))
    text.tag_config("Paragraphe", font=('Tahoma', 12, 'italic'))
    
    text.insert(tk.END, para1_help, 'Debut')
    text.insert(tk.END, titre1_help, 'Titre')
    text.insert(tk.END, paraf_utilisateur, 'Paragraphe')
    text.insert(tk.END, titre2_help, 'Titre')
    text.insert(tk.END, paraf_reservation, 'Paragraphe')
    text.insert(tk.END, titre3_help, 'Titre')
    text.insert(tk.END, paraf_location, 'Paragraphe')
    
    text.configure(state='disabled')
    text.place(relx=0, rely=0, relheight=1, relwidth=1)
