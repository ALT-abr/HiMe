import matplotlib.pyplot as plt
from database import connection

def graphe_progression():
    conn, c = connection()

    c.execute("SELECT type_quiz, score_quiz, date_quiz FROM quiz")
    list = c.fetchall()
 
    if not list:
        print("vous avvez pas joue un quiz !")

    type, score, date = list

    plt.plot(date, score, label = type)

    plt.title("Mon graphe")
    plt.xlabel("Temps")
    plt.ylabel("Score")
    plt.legend()
    plt.show()

    conn.close()
