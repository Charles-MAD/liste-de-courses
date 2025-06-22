# Programme qui permet de gérer une liste de courses (To Do List)ou de manipuler une liste de courses
# La gestion des listes, Utilisation des boucles, de l'interface utilisateur
# import sys


# while True:
liste_courses = []
liste_operations = [
        "Ajouter un élément à la liste",
        "Retirer un élément de la liste", 
        "Afficher la liste", 
        "Vider la liste", 
        "Quitter",
]
separator = "-" * 25


while True:
    print(separator)
    print("\nChoisissez parmi les 5 options suivantes :")
    for i, element in enumerate(liste_operations, start=1): # enumerate() permet d'afficher un élément de la liste et son indice.
        print(f"{i}: {element}")# input() renvoie toujours une chaîne de caractère
    # Vérifie si c'est un nombre entre 1 et 5
    choice = input("Votre choix : ")
    if choice.isdigit(): 
       choice = int(choice) 
    else: 
        print("Veuillez entrer un nombre entre 1 et 5.")
        continue # On ne va pas exécuter tout le code qui vient après lui, on va revenir au niveau de la boucle
    if choice == 1:
        element = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        # Vérifie si la chaîne entrée n'est pas vide
        if element == "" and element.isdigit():
            print("Veuillez entrer un nom valide.")
        else:
            liste_courses.append(element) # append() Permet d'ajouter un élément dans la liste
            print(f"L'élément {element} a bien été ajouté à la liste.")
    elif choice == 2:
        element = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
        if not element in liste_courses:
            print(f"L'élément {element} ne se trouve pas dans la liste.")
        else:
            liste_courses.remove(element) # remove() : permet de supprimer un élément de la liste
            print(f"L'élément {element} a bien été supprimé de la liste.")
    elif choice == 3: 
        # Vérifie d'abord si la liste existe avant d'afficher son contenu
        if not liste_courses: 
            print("Votre liste est vide") 
        else:
           print("Voici le contenu de votre liste :") 
           for i, element in enumerate(liste_courses, start=1): # enumerate() : permet de numérer automatiquement les éléments d'une liste
            print(f"{i}. {element.capitalize()}") 
    elif choice == 4: 
        # Option de confirmation avant de vider la liste
        confirmation = input("Êtes-vous sûr de vouloir supprimer la liste ? oui/non : ")
        if confirmation == 'oui': 
            liste_courses.clear() # La méthode clear() permet de vider une liste d'élément
            print("La liste a été vidée.") 
        else:
            print("Action annulée.")
    elif choice == 5:
        print("Votre liste de courses est prête.")        
        print("À bientôt !") 
        break
        # sys.exit() 
    else:
        print("Veuillez entrer un **nombre entre 1 et 5**") 
print(separator)
# Les noms de variables doivent être explicites