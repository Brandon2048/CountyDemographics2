from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    if 'states' in request.args:
        return render_template('main.html', states = get_state_options(counties), highest_population1 = highest_population(request.args['states'], counties))
    else:
        return render_template('main.html', states = get_state_options(counties))

def get_state_options(counties):
    states = []
    print("Render")
    for data in counties:
        if data["State"] not in states:
            states.append(data["State"])
    options = ""
    for data in states:
        options = options + Markup("<option value=\"" + data + "\">" + data + "</option>")
    return options

def highest_population(state, counties):
    name3 = counties[0]["County"]
    highpop = counties[0]["Population"]["2014 Population"]
    for data in counties:
        if data['State'] == state:
            if data["Population"]["2014 Population"]> highpop:
                name3 = data["County"]
                highpop = data["Population"]["2014 Population"]
    return name3

if __name__ == "__main__":
    app.run(debug=True)
