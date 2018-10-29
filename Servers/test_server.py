from flask import Flask, request, redirect
# from flask_restful import Resource, Api
from flask import jsonify
import json


app = Flask(__name__)

@app.route("/test", methods=['POST','GET'])
def testing():
	if request.method == 'POST':
		return(jsonify({"Name":"Israa", "Email":"asmer@gmial.com", "Mobile":"0111111110"}))
	else:
		return(jsonify({"Name":"Israa", "Email":"asmer@gmial.com", "Mobile":"0111111110"}))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
