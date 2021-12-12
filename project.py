from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    data = "Lucas Romero"
    return jsonify({'name': data})

@app.route('/timesten/<int:num>', methods = ['GET'])
def timesten(num):
    result=num*10
    return jsonify ({"number":num, "result":result}) 


if __name__=='__main__':
    app.run(debug=True)

