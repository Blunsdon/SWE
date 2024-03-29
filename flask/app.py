from flask import Flask

# Passes the name app as main
app = Flask(__name__)

# Sets up route with message
@app.route('/')
def hello_world():
    return 'Flask Dockerized anything good'

# if OK run lokalhost
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')