from flask import Flask, render_template, request
import sys
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def all_routes(path):
    print(str(path) + "|" + str(request.headers.get("Azurejwt")) + "|" + str(request.headers.get("User-Agent")))
    return render_template('index.html')

