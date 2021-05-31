from flask import Flask, render_template, request
import sys
app = Flask(__name__)

@app.route("/")
def hello():
    print(str(request.headers.get("Azurejwt")) + "|" + str(request.headers.get("User-Agent")))
    return render_template('index.html')

