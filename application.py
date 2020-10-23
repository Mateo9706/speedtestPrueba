from flask import Flask, request
import requests

app = Flask(__name__)

url = "https://ipinfo.io/"
url2 = "https://librespeed.org/"

@app.route('/ip')
def hello_world():
    endpoint = "/json"
    client_ip = request.environ.get('HTTP_X_FORWARDED_FOR')
    print(client_ip)
    response = requests.get(url+client_ip+endpoint)
    print(response.text)
    return response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0')