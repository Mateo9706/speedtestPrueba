import socket

from flask import Flask, request
import requests

app = Flask(__name__)

url = "https://ipinfo.io/"
url2 = "https://librespeed.org/"

@app.route('/ip')
def hello_world():
    #endpoint = "/json"
    #client_ip = request.environ.get('HTTP_X_FORWARDED_FOR')
    #print(client_ip)
    #response = requests.get(url+client_ip+endpoint)
    #print(response.text)
    otro()
    return "ya"#response.text

def otro():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('104.214.20.35', 8000))
    s.listen(1)
    # Estas son las variables del cliente
    conn, addr = s.accept()
    clientIP = addr  # Aquí se guarda la IP del cliente
    s.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')