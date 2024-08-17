from flask import Flask, render_template, Response, redirect, session, url_for, request
from detection import generate_frames
#from sms_notificaton import send_notification
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key
app.config['DETECTION_ON'] = False 
detection = app.config['DETECTION_ON'] 

# Dummy user and admin data for demonstration
users = {'user': 'password'}
admins = {'admin': 'admin_password'}

def authenticate(username, password, role):
    if role == 'admin' and username in admins and admins[username] == password:
        return True
    elif role == 'user' and username in users and users[username] == password:
        return True
    else:
        return False

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        if authenticate(username, password, role):
            session['username'] = username
            session['role'] = role
            return redirect(url_for('index'))
        else:
            return render_template('login.html', message='Invalid credentials. Please try again.')

    return render_template('login.html')

# Remaining routes and functions...


@app.route('/index')
def index():
    if 'username' in session:
        return render_template('index.html', detection_on=app.config['DETECTION_ON'])
    else:
        return redirect(url_for('login'))
@app.route('/video_feed')
def video_feed():
    if 'username' in session:
        return Response(generate_frames(app), mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        return redirect(url_for('login'))


@app.route('/toggle_detection', methods=['POST'])
def toggle_detection():
    # if 'username' in session and session['role'] == 'admin':
      app.config['DETECTION_ON'] = not app.config['DETECTION_ON']
     # print(app.config['DETECTION_ON'])
      detection=app.config['DETECTION_ON']
      return 'Detection toggled'
    # else:
    #     return Response('You are not authorized to perform this action.', status=403)

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
