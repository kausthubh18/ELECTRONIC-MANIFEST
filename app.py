from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your own secret key

# In-memory user store (replace with a database in production)
users = {
    'Kausthubh': generate_password_hash('Kausthubh18@#')  # Username: Kausthubh, Password: Kausthubh18@#
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and check_password_hash(users[username], password):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return 'Invalid username or password'
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Other routes...
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

@app.route('/iot-blogs')
def iot_blogs():
    return render_template('iot_blogs.html')

@app.route('/vlsi-blogs')
def vlsi_blogs():
    return render_template('vlsi_blogs.html')

@app.route('/ai-ml-blogs')
def ai_ml_blogs():
    return render_template('ai_ml_blogs.html')

@app.route('/robotics-blogs')
def robotics_blogs():
    return render_template('robotics_blogs.html')

@app.route('/embedded-systems-blogs')
def embedded_systems_blogs():
    return render_template('embedded_systems_blogs.html')

@app.route('/additional-service-blogs')
def additional_service_blogs():
    return render_template('additional_service_blogs.html')

if __name__ == "__main__":
    app.run(debug=True)
