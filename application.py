from flask import Flask
import requests
app = Flask(__name__)

url = "https://ipinfo.io/"

@app.route('/')
def hello_world():
    response = requests.get(url)
    print(response.text)
    return 'Hello, World!'

#if __name__ == '__main__':
#    app.run(host='0.0.0.0')