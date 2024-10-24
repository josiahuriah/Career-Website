from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bimini, Bahamas',
    'salary': 'BSD $68,000.00'
  },
  {
    'id': 2,
    'title': 'Front End Engineer',
    'location': 'Remote',
    'salary': 'BSD $48,000.00'
  },
  {
    'id': 3,
    'title': 'Data Analyst',
    'location': 'Exuma, Bahamas',
    'salary': 'BSD $64,000.00'
  },
  {
    'id': 4,
    'title': 'Back End Engineer',
    'location': 'Remote',
  }
]

@app.route("/")
def hello_world():
  return render_template("home.html",
                         jobs=JOBS,
                        company_name = "Josiah")

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)