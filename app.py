from flask import Flask

# Create a Flask web application
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # Run the app on port 5000
    app.run(host='0.0.0.0', port=5000)
