from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/domains')
def domains():
    return render_template('domains.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/iot-solutions')
def iot_solutions():
    return render_template('iot_solutions.html')

@app.route('/vlsi-solutions')
def vlsi_solutions():
    return render_template('vlsi_solutions.html')

@app.route('/embedded-systems')
def embedded_systems():
    return render_template('embedded_systems.html')

@app.route('/robotics')
def robotics():
    return render_template('robotics.html')

@app.route('/ai-ml')
def ai_ml():
    return render_template('ai_ml.html')

if __name__ == '__main__':
    app.run(debug=True)
