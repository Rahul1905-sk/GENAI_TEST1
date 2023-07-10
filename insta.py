 
from flask import Flask, request
app = Flask(__name__)

dist = {}

@app.route('/create', method=['POST'])
def create_post():
    ob = request.get_json()
    dist['username'] = ob.username
    dist['caption'] = ob.caption

    return 'post created'

@app.route('/read', method=['GET'])
def read_post():

    return print(dist)

@app.route('/delete/<int:user_id>', method=['DELETE'])
def delete_post():
    if dist.id == id: 
        dist.remove(id)

    return print("post deleted")







if __name__ == "__main__":
    app.run()