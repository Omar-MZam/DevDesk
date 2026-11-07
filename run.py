from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Bienvenido a DevDesk - Sistema de soporte tecnico"

if __name__ == "__main__":
    app.run(debug=True)