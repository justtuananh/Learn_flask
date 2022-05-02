from gc import DEBUG_COLLECTABLE
from flask import Flask 


app = Flask(__name__)

@app.route('/')
def index(): 
    return "tuan anh hoc flask2"


if __name__ == "__main__": 
    app.run(debug=True)
