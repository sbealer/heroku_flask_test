from flask import Flask
import google_test
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

# @app.route('/auth')
# def auth():
#     return 'Something else'
if __name__ == '__main__':
    app.run()
