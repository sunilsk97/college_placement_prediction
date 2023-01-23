
from flask import Flask,jsonify,request,render_template
from project_app.utils import CollegePlacement

import config

app = Flask(__name__)


@app.route("/")  
def hello_flask():
    return render_template("home.html")
    
@app.route('/test')
def student():

    return render_template("index.html")
        
        
@app.route('/result', methods = ['POST', 'GET'])

def get_placed_not():

    if request.method == 'POST':

        result = request.form

        Age  = result['Age']
        Gender = result['Gender']
        Stream = result['Stream']
        Internships  = result['Internships']
        CGPA  = result['CGPA']
        Hostel  = result['Hostel']
        HistoryOfBacklogs = result['HistoryOfBacklogs']

        clg_place = CollegePlacement(Age,Gender,Stream,Internships,CGPA,Hostel,HistoryOfBacklogs)
        placement = clg_place.get_placed_not()
        if placement == 1:
            return render_template("index.html", placement = "Student can be placed")
        else:
            return render_template("index.html", placement = "Student can not be placed")    
    

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080,debug=True)  # server start