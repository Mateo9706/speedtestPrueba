from flask import Flask, request, render_template
import requests


app = Flask(__name__)


url = "https://ipinfo.io/"
url2 = "https://librespeed.org/"

@app.route('/ip')
def hello_world():
    print("entra aca")
    endpoint = "/json"
    client_ip = request.environ.get('HTTP_X_FORWARDED_FOR')
    convert = client_ip.split(":")
    #print(convert)
    print(client_ip)
    response = requests.get(url+convert[0]+endpoint)
    print(response.text)
    #otro()
    return response.text


if __name__ == '__main__':
    app.run(host='0.0.0.0')