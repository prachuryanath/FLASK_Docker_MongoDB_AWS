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
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
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