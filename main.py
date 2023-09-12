
def demander_reponse(min, max):
    reponse_str = input(f"Votre réponse (entre {min} et {max}): ")
    try:
        reponse_int = int(reponse_str)
        if min <= reponse_int <= max:
            return reponse_int
        print(f"ERREUR: vous devez renseigner un chiffre entre {min} et {max}!")
    except:
        print("ERREUR: veuillez renseigner uniquement des chiffres!")
    return demander_reponse(min, max)


def poser_question(question):
    choix = question[1]
    taille_choix_reponse = len(choix)

    print(question[0])
    for i in range(taille_choix_reponse):
        print(f"{i+1} {choix[i]}")

    print("---------------")
    reponse_correct = False
    reponse_int = demander_reponse(1, len(choix))
    if choix[reponse_int-1] == question[2]:
        print("Bonne réponse")
        reponse_correct = True
    else:
        print("Mauvaise réponse")
    print()
    return reponse_correct


def lancer_questionnaire(questions):
    score = 0
    for question in questions:
        if poser_question(question):
            score+=1
    print(f"Votre score est de {score}/{len(questionnaire)}")

#   ----------------------------------------------------------


questionnaire = (
    ("Quelle est la capitale de la France ? ", ("Paris", "Lyon", "Bordeaux", "Lille"), "Paris"),
    ("Quelle est la capitale de l'Italie ? ", ("Venise", "Londres", "Rome", "Turin"), "Rome"),
    ("Quelle est la capitale de l'Espagne ? ", ("Porto", "Madrid", "Talinn", "Berlin"), "Madrid"),
    ("Quelle est la capitale de l'Allemagne ? ", ("Berlin", "Madrid", "Copenhague", "Amsterdam"), "Berlin")
)

print("-----QCM-----")
lancer_questionnaire(questionnaire)
