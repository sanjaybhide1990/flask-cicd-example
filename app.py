from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/test-route')
def test_route():
    return "Route is working!!"

@app.route('/testing-jenkins')
def check_pipeline():
    return 'Pipeline is triggered'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8081)