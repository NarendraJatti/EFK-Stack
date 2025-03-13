from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Path where the username will be stored (mounted volume in Docker)
log_file_path = "/var/lib/docker/usernames.log"

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    
    # Store the username in the log file
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"Username: {username}\n")
    
    return f"Hello, {username}! Your login was successful."

if __name__ == '__main__':
    # Ensure the log file path exists in Docker
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
    app.run(host='0.0.0.0', port=5000)
