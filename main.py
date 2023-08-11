from flask import Flask,render_template,url_for,redirect,request,jsonify 

app = Flask(__name__)
@app.route("/")
def index():

      return render_template("index.html")
@app.route("/CodeGenerator")
def codegenerator():
       
      return render_template("code_generator.html")
@app.route("/Sensordata")
def sensor_datacode():
      return render_template("sensor_dashboard.html")

if __name__ == "__main__":

       app.run(debug=True,threaded=True,host="0.0.0.0",port=5899)
