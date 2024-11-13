import myPythonFunctions
        
def main():
    try:
        print("\n***********************************************")
        print("     ✨ BIENVENUE DANS LE JEU DE CALCULS ✨     ")
        print("   ✨ --Testez votre logique avec BODMAS!-- ✨     ")
        print("***********************************************\n")

        userName=""
        while not userName:
            userName = input("\n** Entrez votre nom : ")
            if not userName:
                print("** Le nom ne peut pas être vide. Veuillez entrer un nom valide. **")
                
        userScore = myPythonFunctions.getUserPoint(userName)
        
        if userScore == -1:
            print("\n* Bienvenue {} ! \n-- Aucun score encore, mais vous êtes ici pour commencer !".format(userName))
            userScore = 0 #changer userScore de -1 à 0
            newUser = True
        else:
            print("\n* Bonjour {} ! \n-- Votre SCORE actuel est : *{}* point(s).".format(userName, userScore))
            newUser = False
            
        # Boucle principale du jeu
        # Déclaration de la variable userChoice avec une valeur initiale de 0
        userChoice = 0
        while userChoice!='-1':
            # Demande de choix de l'utilisateur
            userChoice = input("\n--- Tapez '-1' pour quitter ou une autre touche pour jouer : ---  ")
            # Vérifie si l'utilisateur veut quitter
            if userChoice == '-1':
                myPythonFunctions.updateUserPoints(newUser, userName, userScore)
                print("________________________________________________________________________")
                print("________________________________________________________________________")
                print("\n*** À la prochaine, {} ! On espère que vous reviendrez bientôt ! ***".format(userName))
                print("\n* Votre SCORE est : *{}*".format(userScore))
                print("\n\n*******GAME OVER*******")
                break
            
            print("________________________________________________________________________")
            userScore += myPythonFunctions.generateQuestion()

    except Exception as e:
        print("**Une erreur est survenue: " + str(e))

if __name__ == "__main__":
    main()
