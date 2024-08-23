from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_docker():
    return 'Hello World, this is a simple flask app'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')