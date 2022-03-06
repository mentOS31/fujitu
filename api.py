from flask import Flask, jsonify
 
app = Flask(__name__)
 
@app.route('/data/', method=["PUT"])
def put_user():
    user = request.json["user_id"]
    password = request.json["password"]
    return jsonify({'message': 'Hello world'})
 
 
if __name__ == "__main__":
    app.run()
