from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World !"

@app.route('/hithere')
def hi_there_everyone():
    # prepare a response for the request that came to /hithere
    return "I just hit /hithere"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80)