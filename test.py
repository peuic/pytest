from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
    zipcode = request.form['zip']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=10016,us&appid=c59b7be8f850b289aa465a88af30f040')
    json_object = r.json()
    temp_k = json_object['main']['temp']
    temp_c = (temp_k - 273.15)
    return render_template('temperature.html', temp=temp_c)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
