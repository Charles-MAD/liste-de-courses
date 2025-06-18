# Programme qui permet de gérer une liste de courses ou de manipuler une liste de courses
# La gestion des listes, Utilisation des boucles, de l'interface utilisateur
import sys


# while True:
liste_courses = []
while True:
    liste_operations = [
        "Ajouter un élément à la liste",
        "Retirer un élément de la liste", 
        "Afficher la liste", 
        "Vider la liste", 
        "Quitter"
    ]
    print("\nChoisissez parmi les 5 options suivantes :")
    for i, item in enumerate(liste_operations, start=1): # enumerate() permet d'afficher un élément de la liste et son indice.
        print(f"{i}: {item}")
    choix = input("Votre choix : ") # input() renvoie toujours une chaîne de caractère

    # Vérifie si c'est un nombre entre 1 et 5
    if choix.isdigit():
       choix = int(choix)
    else:
        print("Veuillez entrer un nombre entre 1 et 5.")
        continue
    if choix == 1:
        nom_element_ajoute = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        # Vérifie si la chaîne entrée n'est pas vide
        if nom_element_ajoute == "" and nom_element_ajoute.isdigit():
            print("Veuillez entrer un nom valide.")
        else:
            liste_courses.append(nom_element_ajoute) # append() Permet d'ajouter un élément dans la liste
            print(f"L'élément {nom_element_ajoute} a bien été ajouté à la liste.")
    elif choix == 2:
        nom_element_retire = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
        if not nom_element_retire in liste_courses:
            print(f"L'élément {nom_element_retire} ne se trouve pas dans la liste.")
        else:
            liste_courses.remove(nom_element_retire) # remove() : permet de supprimer un élément de la liste
            print(f"L'élément {nom_element_retire} a bien été supprimé de la liste.")
    elif choix == 3:
        # Vérifie d'abord si la liste existe avant d'afficher son contenu
        if not liste_courses:
            print("Votre liste est vide")
        else:
           print("Voici le contenu de votre liste :")
           for i, item in enumerate(liste_courses, start=1): # enumerate() : permet de numérer automatiquement les éléments d'une liste
            print(f"{i}. {item}")
    elif choix == 4:
        # Option de confirmation avant de vider la liste
        confirmation = input("Êtes-vous sûr de vouloir supprimer la liste ? oui/non : ")
        if confirmation == 'oui':
            liste_courses.clear() # La méthode clear() permet de vider une liste d'élément
            print("La liste a été vidée.")
        else:
            print("Action annulée.")
    elif choix == 5:        
        print("À bientôt !")
        sys.exit()
    else:
        print("Veuillez entrer un **nombre entre 1 et 5**")