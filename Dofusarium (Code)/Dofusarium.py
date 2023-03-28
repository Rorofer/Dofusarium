import os
from datetime import datetime
from Dragodindes import afficher_all_DD_console



def achat_date_prix():
    print("\n" + "-" * 40 + "\n")
    nom_item = ""
    while nom_item == "" or nom_item is None:
        nom_item = input("Nom de l'article (au minimum un caractère) : ")
        if nom_item == "":
            print("Aucun caractère entré.")

        qte_items = -1
        while qte_items is None or qte_items <= 0 :
            try:
                qte_items = float(input("Entrez le nombre d'items achetés (entrez un nombre supérieur à 0) : "))
            except ValueError:
                print("Veuillez entrer un nombre.")

    prix_items = -1
    while prix_items is None or prix_items <= 0:
        try:
            prix_items = float(input("Prix du lot d'articles (entrez un nombre supérieur à 0): "))
        except ValueError:
            print("Veuillez entrer un nombre.")
    
    prix_unité = (prix_items/qte_items)
    
    with open("achats_dates.txt", "a") as f:
        date_obj = datetime.today()
        day = date_obj.day
        month = date_obj.month
        year = date_obj.year
        date_achat = f"{day:02d}/{month:02d}/{year}"
        f.write("\n"+"-" * 40 + "\n")
        if qte_items == 1 :
            f.write(f"Item : {nom_item}\n"+f"Quantité d'items : {qte_items}\n"+f"Prix des items : {prix_items}\n"+f"Date d'achat : {date_achat}")
        else :
            f.write(f"Item : {nom_item}\n"+f"Quantité d'items : {qte_items}\n"+f"Prix des items : {prix_items}\n"+f"Prix d'un item : {prix_unité}\n"+f"Date d'achat : {date_achat}")
    print("Date d'achat mise à la date du jour ({})",date_obj)
    



def calculer_rentabilite():
    print("\n" + "-" * 40 + "\n")

    nom_item = ""
    while(nom_item =="" or nom_item == None):
        try:
            nom_item = input("Nom de l'item (au minimum un caractère) : ")
            if nom_item == "":
                print("Aucun caractère entré.")
        except ValueError:
            print("Entrez un nom d'item")

    nb_ressources = 0
    while (nb_ressources == None or nb_ressources <= 0):
        try:
            nb_ressources = int(input("Nombre de ressources utilisées : "))
            if nb_ressources <= 0:
                print("Veuillez entrer une valeur supérieure à 0.")
                nb_ressources = 0
        except ValueError:
            print("Veuillez entrer un nombre.")
    ressources = {}
    for i in range(nb_ressources):
        
        nom_ressource = ""
        while(nom_ressource =="" or nom_ressource == None):
            try:
                nom_ressource = input("Nom de la ressource {} : ".format(i+1))
                if nom_ressource== "":
                    print("Aucun caractère entré.")
            except ValueError:
                print("Entrez un nom de ressource")

        prix_unitaire = None
        while prix_unitaire is None or prix_unitaire < 0:
            try:
                prix_unitaire = float(input("Prix unitaire de la ressource : "))
                if prix_unitaire < 0:
                    print("Veuillez entrer une valeur supérieure ou égale à 0.")
                    prix_unitaire = None
            except ValueError:
                print("Veuillez entrer un nombre.")
        quantite_utilisee = 0
        while quantite_utilisee is None or quantite_utilisee <= 0:
            try:
                quantite_utilisee = int(input("Quantité utilisée de la ressource : "))
                if quantite_utilisee <= 0:
                    print("Veuillez entrer une valeur supérieure à 0.")
            except ValueError:
                print("Veuillez entrer un nombre supérieur à 0.")
        ressources[nom_ressource] = (prix_unitaire, quantite_utilisee)

    prix_craft = sum([qte * prix_unitaire for prix_unitaire, qte in ressources.values()])
    prix_vente = 0
    while prix_vente is None or prix_vente <= 0:
        try:
            prix_vente = float(input("Prix de revente de l'item : "))
            if prix_vente <= 0:
                print("Veuillez entrer une valeur supérieure à 0.")
        except ValueError:
            print("Veuillez entrer un nombre.")

    prix_final = -1
    if prix_craft == 0:
        if prix_vente == 1:
            prix_final = 0
        else :
            prix_final = prix_vente - (prix_vente * 0.02) - prix_craft
    else: 
        prix_final = prix_vente - (prix_vente * 0.02) - prix_craft

    print ("La rentabilité de l'item {} est de {}.".format(nom_item,prix_final))
    print("\n" + "-" * 40 + "\n")

    try:
        with open("craft.txt", "a") as f:
            f.write("\n"+"-" * 40 + "\n")
            f.write(f"La rentabilité de l'item {nom_item} est de {prix_final:.2f} kamas.")
    except OSError as e:
        print(f"Une erreur s'est produite lors de l'écriture dans le fichier : {e}")




def calculer_prix_revente():
    # Demande les informations à l'utilisateur
    print("\n" + "-" * 40 + "\n")
    nom_item = None
    while nom_item == None or nom_item =="":
        try:
            nom_item = input("Entrez le nom de l'item (au minimum un caractère) : ")
            if nom_item == "":
                print("Aucun caractère entré.")
        except ValueError:
            print("Entrez un nom d'item.")
            
    quantite = 0
    while quantite == None or quantite <= 0:
        try:
            quantite = int(input("Quantité d'items achetés : "))
            if quantite <= 0 :
                print("Veuillez entrer une valeur supérieure à 0")
        except ValueError:
            print("Veuillez entrer un nombre.")


    prix_achat = -1
    while prix_achat == None or prix_achat < 0:
        try:
            while prix_achat<0:
                prix_achat = float(input("Prix d'achat pour 1 (entrez un nombre supérieur ou égal à 0): "))
        except ValueError:
            print("Veuillez entrer un nombre.")


    
    # Demande le prix de revente pour les options *1, *10 et *100
    prix_revente_1 = -1
    while prix_revente_1 == None or prix_revente_1 <= 0:
        try:
            while prix_revente_1 <= 0:
                prix_revente_1 = float(input("Entrez le prix de revente pour *1 (valeure supérieure à 0): "))
        except ValueError:
            print("Veuillez entrer un nombre.")


    prix_revente_10 = 0
    while prix_revente_10 == None or prix_revente_10 <= 0:
        try:
            while prix_revente_10 <= 0:
                prix_revente_10 = float(input("Entrez le prix de revente pour *10 (valeure supérieure à 0) : "))
        except ValueError:
            print("Veuillez entrer un nombre.")

    prix_revente_100 = 0
    while prix_revente_100 == None or prix_revente_100 <=0:
        try:
            while prix_revente_100 <= 0:
                prix_revente_100 = float(input("Entrez le prix de revente pour *100 (valeure supérieure à 0) : "))
        except ValueError:
            print("Veuillez entrer un nombre.")
    
    # Calcule le bénéfice pour chaque option
    if (prix_revente_1-prix_achat) <=1:
        benefice_1 = 0
    else:
        benefice_1 = prix_revente_1 * (1 - 0.02) * quantite - prix_achat * quantite


    if (prix_revente_10-prix_achat)<=1:
        benefice_10=0
    else:
        benefice_10 = prix_revente_10 * (1 - 0.02) / 10 * quantite - prix_achat * quantite

        
    if (prix_revente_100-prix_achat)<=1:
        benefice_100 = 0
    else:    
        benefice_100 = prix_revente_100 * (1 - 0.02) / 100 * quantite - prix_achat * quantite
    
    # Détermine la meilleure option de rentabilité
    meilleures_options = []
    if benefice_1 >= max(benefice_10, benefice_100):
        meilleures_options.append("*1")

    if benefice_10 >= max(benefice_1, benefice_100):
        meilleures_options.append("*10")
        
    if benefice_100 >= max(benefice_1, benefice_10):
        meilleures_options.append("*100")

    
    # Affiche les résultats

    print("\nMeilleures options de rentabilité pour {} : {}".format(nom_item, ", ".join(meilleures_options)))
    print("- *1 : bénéfice de {:.2f} kamas".format(benefice_1))
    print("- *10 : bénéfice de {:.2f} kamas".format(benefice_10))
    print("- *100 : bénéfice de {:.2f} kamas".format(benefice_100))

    print("\nUn conseil : gardez le restant en banque jusqu'à ce que le prix remonte !")

    print("\n" + "-" * 40 + "\n")

    # Stocke le résultat dans le fichier prix_revente.txt

    
    try:
        with open("prix_revente.txt", "a") as f:
            f.write("\n"+"-" * 40+"\n")
            f.write("Meilleures options de rentabilité pour {} : {}\n".format(nom_item, ", ".join(meilleures_options)))
            f.write("- *1 : bénéfice de {:.2f} kamas\n".format(benefice_1))
            f.write("- *10 : bénéfice de {:.2f} kamas\n".format(benefice_10))
            f.write("- *100 : bénéfice de {:.2f} kamas\n".format(benefice_100))
            f.write("Un conseil : gardez le restant en banque jusqu'à ce que le prix remonte")
    except OSError as e:
        print(f"Une erreur s'est produite lors de l'écriture dans le fichier : {e}")

if __name__ == '__main__':
    while True:
        print("Que voulez-vous faire ?")
        print("1 - Calculer la rentabilité d'un item crafté")
        print("2 - Entrer des items ainsi que leur prix. La date d'achat est mise à la date du jour")
        print("3 - Calculer le prix de revente d'un item")
        print("4 - Lister toutes les dragodindes du jeu")
        print("0 - Quitter")

        choix = input("Entrez votre choix : ")

        if choix == "1":
            calculer_rentabilite()
        elif choix == "2":
            achat_date_prix()        
        elif choix == "3":
            calculer_prix_revente()
        elif choix == "4":
            print("Types de tri")
            print("1 - ID (ordre croissant)")
            print("2 - ID (ordre déroissant)")
            print("3 - Type (ordre alphabétique)")
            print("4 - Type (ordre alphabétique inversé)")
            print("5 - Parent 1 (ordre alphabétique)")
            print("6 - Parent 1 (ordre alphabétique inversé)")
            print("7 - Parent 2 (ordre alphabétique)")
            print("8 - Parent 2 (ordre alphabétique inversé)")
            print("9 - Type de parchemin(ordre alphabétique)")
            print("10 - Type de parchemin (ordre alphabétique inversé)")

            tri = input("Choisissez l'ordre de tri : ")
            afficher_all_DD_console(tri)
        elif choix == "0":
            break

        else:
            print("Choix invalide.")
        
        input("Appuyez sur une touche pour continuer...")
        os.system('cls' if os.name == 'nt' else 'clear')


# © FERMON Romain Jean Marcel Patrick