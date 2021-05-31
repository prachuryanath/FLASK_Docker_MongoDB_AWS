"""
All communication between server/server, server/browser, 
browser/browser is done through TEXT    *TCP*

IMAGE :
[
    123 125 126 127
    124 125 126 127
]   
JSON :
{
    "field 1":"abc",
    "field2":"def"
}
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hi_there_everyone():
    return "Home page"

@app.route('/add_two_nums', methods=["POST", "GET"])
def add_two_nums():
    # Get x and y from the posted data
    dataDict = request.get_json()
    if "y" not in dataDict:
        return "ERROR", 305
    x = dataDict["x"]
    y = dataDict["y"]
    # Add x and y
    z = x + y
    #Prepare a JSON
    retJSON = {
        "z":z
    }
    #return jsonify(map_prepared)
    return jsonify(retJSON), 200

@app.route('/bye')
def hello_world():
    jfun = {
    "field 1":"abc",
    "field2": 4,
    "boolean":1,
    "array1":[1,2,3,4, "abc"],
    "array2":[    
        {
        "field1": 123
        },
        {
            "field2" : "This is a string"
        },
    ],
    "array of nested arrays":[
        {   
            "nested array":{
                "field1":1,
                "name":"Elfarouk"            
            }
        }
    ]
    }
    return jsonify(jfun)

if __name__ == "__main__":
    app.run(debug=True)