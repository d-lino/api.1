from flask import Flask 

app = Flask(__name__)

@app.route("/")
def bem_vindo():
    return "<h1>Seja Bem Vindo!</h1>"

if __name__ == "__main__":
    app.run(debug=true)