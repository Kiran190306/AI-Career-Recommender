from flask import Flask, render_template, request
import random

app = Flask(__name__)

careers = {
    "Programming": ["Software Developer", "Data Scientist", "AI Engineer"],
    "Design": ["UI/UX Designer", "Graphic Designer", "Game Designer"],
    "Business": ["Business Analyst", "Product Manager", "Marketing Specialist"],
    "Hardware": ["Embedded Engineer", "IoT Developer", "Robotics Engineer"]
}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/recommend', methods=['POST'])
def recommend():
    skill = request.form['skill']
    if skill in careers:
        job = random.choice(careers[skill])
        return render_template("result.html", skill=skill, job=job)
    else:
        return render_template("result.html", skill=skill, job="No suggestion found, try again!")

if __name__ == '__main__':
    app.run(debug=True)

