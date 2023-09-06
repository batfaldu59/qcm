
def poser_question(question, choix1, choix2, choix3, choix4, reponse_question):
    global score
    global nb_question
    nb_question += 1
    print(question)
    print(f"(a) {choix1}")
    print(f"(b) {choix2}")
    print(f"(c) {choix3}")
    print(f"(d) {choix4}")
    print("---------------")
    reponse = input("Votre choix: ")
    if reponse == reponse_question:
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse")
    print()


score = 0
nb_question = 0
print("-----QCM-----")
poser_question("Quelle est la capitale de la France ? ", "Paris", "Lyon", "Bordeaux", "Lille", "a")
poser_question("Quelle est la capitale de l'Italie ? ", "Venise", "Londres", "Rome", "Moscou", "c")
poser_question("Quelle est la capitale de la Belgique ? ", "Amsterdam", "Bruxelles", "Bordeaux", "Talinn", "b")
poser_question("Quelle est la capitale de l'Espagne ? ", "Paris", "Zurich", "Brugges", "Madrid", "d")
print(f"Votre score est de {score}/{nb_question}")