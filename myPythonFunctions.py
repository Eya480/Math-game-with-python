import random
import os

def formatUserName(userName):
    # Strip les espaces blancs et gère les erreurs de format
    return userName.strip().capitalize()


def getUserPoint(userName):
    userName = formatUserName(userName)
    try:
        with open('userScores.txt', 'r') as file:
            for line in file:
                name, score = line.strip().split(', ')
                if formatUserName(name) == userName:
                    return int(score)
        return -1  # Si l'utilisateur n'est pas trouvé
    
    except FileNotFoundError:
        return -1  # Si le fichier n'existe pas


def updateUserPoints(newUser, userName, score):
    userName = formatUserName(userName)
    tempFile="userScores.tmp"
    if newUser:
        # Ajouter un nouvel utilisateur
        with open('userScores.txt', 'a') as file:
            file.write(userName + ", " + str(score) + "\n")
    else:
        # Mettre à jour le score d'un utilisateur existant
        with open('userScores.txt', 'r') as file, open(tempFile, 'w') as temp:
            for line in file:
                name, current_score = line.strip().split(', ')
                name=formatUserName(name)
                if name == userName:
                    temp.write(name + ", " + str(score) + "\n")
                else:
                    temp.write(line)
        
        os.remove('userScores.txt')
        os.rename(tempFile, 'userScores.txt')


                
def generateQuestion():
    operandList = [random.randint(1, 10) for _ in range(5)]# Liste des opérandes initialisée à 0
    operatorList = ["", "", "", ""]# Liste des opérateurs initialisée à vide
    operatorDict = {1: "+", 2: "-", 3: "*", 4: "**"} # Dictionnaire des opérateurs

    #Mise à jour de operandList avec des nombres aléatoires
    for i in range(len(operandList)):
        operandList[i] = random.randint(1, 10)
    
    # Mise à jour de operatorList avec des opérateurs mathématiques
    for i in range(len(operatorList)):
        operatorList[i] = operatorDict[random.randint(1, 4)]
    
    for i in range(len(operatorList)):
        operator = operatorDict[random.randint(1, 4)]  # Choisir un opérateur aléatoire
        while operator == "**" and operatorList[i-1] == "**" and i > 0:
            operator = operatorDict[random.randint(1, 4)]  # Choisir un autre opérateur
        operatorList[i] = operator

    questionString = ""
    for i in range(4):
        questionString += str(operandList[i])+str(operatorList[i])
        
    questionString += str(operandList[4])

    questionString_display = questionString.replace("**", "^")
    print("\n* ---> Question :",questionString_display)
    
    result = eval(questionString)
    while True:
        try:
            userAnswer = int(input("-- Votre réponse: "))
            if userAnswer == result:
                print("**Bonne réponse !**")
                return 1
            else:
                print("**Mauvaise réponse. La bonne réponse est *" + str(result) + "*.")
                return 0
        except ValueError:
            print("**Erreur: veuillez entrer un nombre valide.")
