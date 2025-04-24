from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Parinith M'

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000)
