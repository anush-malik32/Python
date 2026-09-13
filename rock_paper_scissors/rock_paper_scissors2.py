import random

from flask import Flask, render_template, request, session

app = Flask(__name__)

app.secret_key = "rock-paper-scissors-secret"

@app.route("/")
def home():
    session["players_score"] = 0
    session["computers_score"] = 0
    session["total_matches"] = 10

    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():
    players_choice = request.form["choice"]

    choices = ["Rock", "Paper", "Scissors"]

    computers_choice = random.choice(choices)

    result = ""

    if players_choice == "Rock":

        if computers_choice == "Paper":
            result = "Winner is computer"
            session["computers_score"] += 1

        elif computers_choice == "Rock":
            result = "Tie"

        elif computers_choice == "Scissors":
            result = "Winner is player"
            session["players_score"] += 1

    if players_choice == "Paper":

        if computers_choice == "Scissors":
            result = "Winner is computer"
            session["computers_score"] += 1

        elif computers_choice == "Paper":
            result = "Tie"

        elif computers_choice == "Rock":
            result = "Winner is player"
            session["players_score"] += 1

    if players_choice == "Scissors":

        if computers_choice == "Rock":
            result = "Winner is computer"
            session["computers_score"] += 1

        elif computers_choice == "Scissors":
            result = "Tie"

        elif computers_choice == "Paper":
            result = "Winner is player"
            session["players_score"] += 1

    session["total_matches"] -= 1

    final_result = ""

    if session["total_matches"] == 0:

        if session["computers_score"] > session["players_score"]:
            final_result = "The winner of this game is the computer! Better luck next time!"

        elif session["players_score"] > session["computers_score"]:
            final_result = "The winner of this game is you! Great job, you beat the computer!"

        elif session["players_score"] == session["computers_score"]:
            final_result = "You and the computer tied! Great job!"

    return render_template("index.html", players_choice=players_choice, computers_choice=computers_choice, result=result, players_score=session["players_score"], computers_score=session["computers_score"], total_matches=session["total_matches"], final_result=final_result)
if __name__ == "__main__":
    app.run(debug=True)