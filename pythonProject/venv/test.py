from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    print ('this is a test')
    return 'hello test'
if __name__ == '__main__':
    app.run()