from flask import Flask
import os
#import google_test
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/auth')
def auth():
    return 'The username is: ' + os.environ['AZN_AUTH1']
if __name__ == '__main__':
    app.run()
