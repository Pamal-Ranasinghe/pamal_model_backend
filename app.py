#import flask module
from flask import Flask

app = Flask(__name__)

#Test route
@app.route('/')
def hello_world():
    return 'Hello World'

#Main function
if __name__ == '__main__':
    app.run()