# importing modules
from flask import Flask, render_template
import datetime
from datetime import date


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def calculate_weeks_left(life_expectancy, age):
    return (life_expectancy - age) * 52

def calculate_weeks_passed(age):
    return age * 52

# declaring app name
app = Flask(__name__)

# making list of pokemons

life_expectancy = 78
date_of_birth = datetime.datetime(1988, 8, 24)





# defining home page
@app.route('/')
def homepage():
    # returning index.html and list
    # and length of list to html page
    age = calculate_age(date_of_birth)
    today = datetime.datetime.now().strftime("%d/%m/%Y")

    weeks_passed = calculate_weeks_passed(age)
    weeks_left = calculate_weeks_left(life_expectancy, age)
    timestamp = datetime.datetime.now()

    return render_template("index.html", weeks_passed = weeks_passed, weeks_left = weeks_left, date_of_birth=date_of_birth, life_expectancy=life_expectancy, age=age, date=today, timestamp=timestamp)

if __name__ == '__main__':

    # running app
    app.run(use_reloader = True, debug = True)
